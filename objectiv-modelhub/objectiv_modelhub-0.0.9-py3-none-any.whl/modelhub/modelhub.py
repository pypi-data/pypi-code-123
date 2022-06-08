"""
Copyright 2021 Objectiv B.V.
"""
import re
from typing import List, Union, Dict, Tuple, Optional, cast
from typing import TYPE_CHECKING

import bach
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

from modelhub.aggregate import Aggregate
from modelhub.map import Map
from modelhub.models.logistic_regression import LogisticRegression
from modelhub.series.series_objectiv import MetaBase
from sql_models.constants import NotSet

if TYPE_CHECKING:
    from modelhub.series import SeriesLocationStack

GroupByType = Union[List[Union[str, bach.Series]], str, bach.Series, NotSet]
ConversionEventDefinitionType = Tuple[Optional['SeriesLocationStack'], Optional[str]]

TIME_DEFAULT_FORMAT = 'YYYY-MM-DD HH24:MI:SS.MS'


class ModelHub:
    """
    The model hub contains collection of data models and convenience functions that you can take, combine and
    run on Bach data frames to quickly build highly specific model stacks for product analysis and
    exploration.
    It includes models for a wide range of typical product analytics use cases.

    All models from the model hub can run on Bach DataFrames that contain data collected by the Objectiv
    tracker. To instantiate a DataFrame with Objectiv data use :py:meth:`ModelHub.from_objectiv_data`. Models
    from the model hub assume that at least the columns of a DataFrame instantiated with this method are
    available in order to run properly. These columns are:

    The model hub has two main type of functions: :py:attr:`map` and :py:attr:`aggregate`.

    * `map` functions always return a series with the same shape and index as the DataFrame they originate
      from. This ensures they can be added as a column to that DataFrame.
    * `aggregate` fuctions return aggregated data in some form from the DataFrame. Can also be accessed with
      `agg`.
    """
    def __init__(self,
                 time_aggregation: str = TIME_DEFAULT_FORMAT):
        """
        Constructor

        :param time_aggregation: Time aggregation used for aggregation models.
        """

        self._time_aggregation = time_aggregation
        self._conversion_events = cast(Dict[str, ConversionEventDefinitionType], {})

        # init metabase
        self._metabase = None

    @property
    def time_aggregation(self):
        """
        Time aggregation used for aggregation models, set when object is instantiated.
        """
        return self._time_aggregation

    @property
    def conversion_events(self):
        """
        Dictionary of all events that are labeled as conversion.

        Set with :py:meth:`add_conversion_event`
        """
        return self._conversion_events

    @staticmethod
    def _check_data_is_objectiv_data(data: bach.DataFrame):
        """
        Validates that provided DataFrame is a representation of an objectiv dataframe.
        """
        from modelhub.stack.util import check_objectiv_dataframe
        check_objectiv_dataframe(data, check_index=True, check_dtypes=True, with_md_dtypes=True)

    @staticmethod
    def _get_db_engine(db_url: Optional[str], bq_credentials_path: Optional[str] = None) -> Engine:
        """
        returns db_connection based on db_url.
        If db_url is for BigQuery, bq_credentials_path must be provided.
        """
        if db_url and re.match(r'^bigquery://.+', db_url):
            if not bq_credentials_path:
                raise ValueError('BigQuery credentials path is required for engine creation.')

            return create_engine(db_url, credentials_path=bq_credentials_path)

        import os
        db_url = db_url or os.environ.get('DSN', 'postgresql://objectiv:@localhost:5432/objectiv')
        return create_engine(db_url)

    def get_objectiv_dataframe(
        self,
        db_url: str = None,
        table_name: str = 'data',
        start_date: str = None,
        end_date: str = None,
        *,
        bq_credentials_path: Optional[str] = None,
    ):
        """
        Sets data from sql table into an :py:class:`bach.DataFrame` object.

        The created DataFrame points to where the data is stored in the sql database, makes several
        transformations and sets the right data types for all columns. As such, the models from the model hub
        can be applied to a DataFrame created with this method.

        :param db_url: the url that indicate database dialect and connection arguments. If not given, env DSN
            is used to create one. If that's not there, the default of
            'postgresql://objectiv:@localhost:5432/objectiv' will be used.
        :param table_name: the name of the sql table where the data is stored.
        :param start_date: first date for which data is loaded to the DataFrame. If None, data is loaded from
            the first date in the sql table. Format as 'YYYY-MM-DD'.
        :param end_date: last date for which data is loaded to the DataFrame. If None, data is loaded up to
            and including the last date in the sql table. Format as 'YYYY-MM-DD'.

        :param bq_credentials_path: path for BigQuery credentials. If db_url is for BigQuery engine, this
            parameter is required.

        :returns: :py:class:`bach.DataFrame` with Objectiv data.
        """
        engine = self._get_db_engine(db_url=db_url, bq_credentials_path=bq_credentials_path)
        from modelhub.stack import get_sessionized_data

        data = get_sessionized_data(
            engine=engine,
            start_date=start_date,
            end_date=end_date,
            table_name=table_name,
        )

        # sessionized data returns both series as bach.SeriesJson.
        data['global_contexts'] = data.global_contexts.astype('objectiv_global_context')
        data['location_stack'] = data.location_stack.astype('objectiv_location_stack')
        return data

    def add_conversion_event(self,
                             location_stack: 'SeriesLocationStack' = None,
                             event_type: str = None,
                             name: str = None):
        """
        Label events that are used as conversions. All labeled conversion events are set in
        :py:attr:`conversion_events`.

        :param location_stack: the location stack that is labeled as conversion. Can be any slice in of a
            :py:class:`modelhub.SeriesLocationStack` type column. Optionally use in conjunction with
            ``event_type`` to label a conversion.
        :param event_type: the event type that is labeled as conversion. Optionally use in conjunction with
            ``objectiv_location_stack`` to label a conversion.
        :param name: the name to use for the labeled conversion event. If None it will use 'conversion_#',
            where # is the number of the added conversion.
        """

        if location_stack is None and event_type is None:
            raise ValueError('At least one of conversion_stack or conversion_event should be set.')

        if not name:
            name = f'conversion_{len(self._conversion_events) + 1}'

        self._conversion_events[name] = location_stack, event_type

    def time_agg(self, data: bach.DataFrame, time_aggregation: str = None) -> bach.SeriesString:
        """
        Formats the moment column in the DataFrame, returns a SeriesString.

        Can be used to aggregate to different time intervals, ie day, month etc.

        :param data: :py:class:`bach.DataFrame` to apply the method on.
        :param time_aggregation: if None, it uses :py:attr:`time_aggregation` set from the
            ModelHub. Use any template for aggregation from:
            https://www.postgresql.org/docs/14/functions-formatting.html
            ie. ``time_aggregation=='YYYY-MM-DD'`` aggregates by date.
        :returns: SeriesString.
        """

        time_aggregation = self.time_aggregation if time_aggregation is None else time_aggregation
        return data.moment.dt.sql_format(time_aggregation).copy_override(name='time_aggregation')

    _metabase: Union[None, MetaBase] = None

    def to_metabase(self, data, model_type: str = None, config: dict = None):
        """
        Plot data in ``data`` to Metabase. If a card already exists, it will be updated. If ``data`` is a
        :py:class:`bach.Series`, it will call :py:meth:`bach.Series.to_frame`.

        Default options can be overridden using the config dictionary.

        :param data: :py:class:`bach.DataFrame` or :py:class:`bach.Series` to push to MetaBase.
        :param model_type: Preset output to Metabase for a specific model. eg, 'unique_users'
        :param config: Override default config options for the graph to be added/updated in Metabase.
        """
        if not self._metabase:
            self._metabase = MetaBase()
        return self._metabase.to_metabase(data, model_type, config)

    @property
    def map(self):
        """
        Access map methods from the model hub.

        .. autoclass:: Map
            :members:
            :noindex:

        """

        return Map(self)

    @property
    def agg(self):
        """
        Access aggregation methods from the model hub. Same as :py:attr:`aggregate`.

        .. autoclass:: Aggregate
            :members:
            :noindex:

        """

        return Aggregate(self)

    @property
    def aggregate(self):
        """
        Access aggregation methods from the model hub. Same as :py:attr:`agg`.

        .. autoclass:: Aggregate
            :members:
            :noindex:

        """
        return Aggregate(self)

    def get_logistic_regression(self, *args, **kwargs) -> LogisticRegression:
        """
        Return an instance of the :py:class:`LogisticRegression` from the model hub.

        All parameters passed to this function are passed to the constructor of the LogisticRegression
        model.
        """

        return LogisticRegression(*args, **kwargs)
