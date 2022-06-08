# coding: utf-8

"""
    3Di API

    3Di simulation API (latest version: 3.0)   Framework release: 1.0.16   3Di core release: 2.0.11  deployed on:  07:33AM (UTC) on September 04, 2020  # noqa: E501

    The version of the OpenAPI document: 3.0
    Contact: info@nelen-schuurmans.nl
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class DamagePostProcessing(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        "basic_post_processing": "int",
        "cost_type": "str",
        "flood_month": "str",
        "inundation_period": "float",
        "repair_time_infrastructure": "int",
        "repair_time_buildings": "int",
    }

    attribute_map = {
        "basic_post_processing": "basic_post_processing",
        "cost_type": "cost_type",
        "flood_month": "flood_month",
        "inundation_period": "inundation_period",
        "repair_time_infrastructure": "repair_time_infrastructure",
        "repair_time_buildings": "repair_time_buildings",
    }

    def __init__(
        self,
        basic_post_processing=None,
        cost_type=None,
        flood_month=None,
        inundation_period=None,
        repair_time_infrastructure=None,
        repair_time_buildings=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """DamagePostProcessing - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._basic_post_processing = None
        self._cost_type = None
        self._flood_month = None
        self._inundation_period = None
        self._repair_time_infrastructure = None
        self._repair_time_buildings = None
        self.discriminator = None

        if basic_post_processing is not None:
            self.basic_post_processing = basic_post_processing
        self.cost_type = cost_type
        self.flood_month = flood_month
        self.inundation_period = inundation_period
        self.repair_time_infrastructure = repair_time_infrastructure
        self.repair_time_buildings = repair_time_buildings

    @property
    def basic_post_processing(self):
        """Gets the basic_post_processing of this DamagePostProcessing.  # noqa: E501


        :return: The basic_post_processing of this DamagePostProcessing.  # noqa: E501
        :rtype: int
        """
        return self._basic_post_processing

    @basic_post_processing.setter
    def basic_post_processing(self, basic_post_processing):
        """Sets the basic_post_processing of this DamagePostProcessing.


        :param basic_post_processing: The basic_post_processing of this DamagePostProcessing.  # noqa: E501
        :type: int
        """

        self._basic_post_processing = basic_post_processing

    @property
    def cost_type(self):
        """Gets the cost_type of this DamagePostProcessing.  # noqa: E501

        'min', 'avg', or 'max'  # noqa: E501

        :return: The cost_type of this DamagePostProcessing.  # noqa: E501
        :rtype: str
        """
        return self._cost_type

    @cost_type.setter
    def cost_type(self, cost_type):
        """Sets the cost_type of this DamagePostProcessing.

        'min', 'avg', or 'max'  # noqa: E501

        :param cost_type: The cost_type of this DamagePostProcessing.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and cost_type is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `cost_type`, must not be `None`"
            )  # noqa: E501
        allowed_values = ["min", "avg", "max"]  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and cost_type not in allowed_values
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `cost_type` ({0}), must be one of {1}".format(  # noqa: E501
                    cost_type, allowed_values
                )
            )

        self._cost_type = cost_type

    @property
    def flood_month(self):
        """Gets the flood_month of this DamagePostProcessing.  # noqa: E501


        :return: The flood_month of this DamagePostProcessing.  # noqa: E501
        :rtype: str
        """
        return self._flood_month

    @flood_month.setter
    def flood_month(self, flood_month):
        """Sets the flood_month of this DamagePostProcessing.


        :param flood_month: The flood_month of this DamagePostProcessing.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and flood_month is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `flood_month`, must not be `None`"
            )  # noqa: E501
        allowed_values = [
            "jan",
            "feb",
            "mar",
            "apr",
            "may",
            "jun",
            "jul",
            "aug",
            "sep",
            "oct",
            "nov",
            "dec",
        ]  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and flood_month not in allowed_values
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `flood_month` ({0}), must be one of {1}".format(  # noqa: E501
                    flood_month, allowed_values
                )
            )

        self._flood_month = flood_month

    @property
    def inundation_period(self):
        """Gets the inundation_period of this DamagePostProcessing.  # noqa: E501

        time in hours  # noqa: E501

        :return: The inundation_period of this DamagePostProcessing.  # noqa: E501
        :rtype: float
        """
        return self._inundation_period

    @inundation_period.setter
    def inundation_period(self, inundation_period):
        """Sets the inundation_period of this DamagePostProcessing.

        time in hours  # noqa: E501

        :param inundation_period: The inundation_period of this DamagePostProcessing.  # noqa: E501
        :type: float
        """
        if (
            self.local_vars_configuration.client_side_validation
            and inundation_period is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `inundation_period`, must not be `None`"
            )  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and inundation_period is not None
            and inundation_period < 1
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `inundation_period`, must be a value greater than or equal to `1`"
            )  # noqa: E501

        self._inundation_period = inundation_period

    @property
    def repair_time_infrastructure(self):
        """Gets the repair_time_infrastructure of this DamagePostProcessing.  # noqa: E501

        time in hours  # noqa: E501

        :return: The repair_time_infrastructure of this DamagePostProcessing.  # noqa: E501
        :rtype: int
        """
        return self._repair_time_infrastructure

    @repair_time_infrastructure.setter
    def repair_time_infrastructure(self, repair_time_infrastructure):
        """Sets the repair_time_infrastructure of this DamagePostProcessing.

        time in hours  # noqa: E501

        :param repair_time_infrastructure: The repair_time_infrastructure of this DamagePostProcessing.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation
            and repair_time_infrastructure is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `repair_time_infrastructure`, must not be `None`"
            )  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and repair_time_infrastructure is not None
            and repair_time_infrastructure > 240
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `repair_time_infrastructure`, must be a value less than or equal to `240`"
            )  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and repair_time_infrastructure is not None
            and repair_time_infrastructure < 1
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `repair_time_infrastructure`, must be a value greater than or equal to `1`"
            )  # noqa: E501

        self._repair_time_infrastructure = repair_time_infrastructure

    @property
    def repair_time_buildings(self):
        """Gets the repair_time_buildings of this DamagePostProcessing.  # noqa: E501

        time in hours  # noqa: E501

        :return: The repair_time_buildings of this DamagePostProcessing.  # noqa: E501
        :rtype: int
        """
        return self._repair_time_buildings

    @repair_time_buildings.setter
    def repair_time_buildings(self, repair_time_buildings):
        """Sets the repair_time_buildings of this DamagePostProcessing.

        time in hours  # noqa: E501

        :param repair_time_buildings: The repair_time_buildings of this DamagePostProcessing.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation
            and repair_time_buildings is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `repair_time_buildings`, must not be `None`"
            )  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and repair_time_buildings is not None
            and repair_time_buildings > 240
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `repair_time_buildings`, must be a value less than or equal to `240`"
            )  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and repair_time_buildings is not None
            and repair_time_buildings < 1
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `repair_time_buildings`, must be a value greater than or equal to `1`"
            )  # noqa: E501

        self._repair_time_buildings = repair_time_buildings

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DamagePostProcessing):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DamagePostProcessing):
            return True

        return self.to_dict() != other.to_dict()
