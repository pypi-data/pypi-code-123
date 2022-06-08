# curved_rail.py
# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from draftsman.classes.entity import Entity
from draftsman.classes.mixins import DoubleGridAlignedMixin, EightWayDirectionalMixin
from draftsman.warning import DraftsmanWarning

from draftsman.data.entities import curved_rails
from draftsman.data import entities

import warnings


class CurvedRail(DoubleGridAlignedMixin, EightWayDirectionalMixin, Entity):
    """
    A curved rail entity.
    """

    def __init__(self, name=curved_rails[0], **kwargs):
        # type: (str, **dict) -> None
        super(CurvedRail, self).__init__(name, curved_rails, **kwargs)

        if "collision_mask" in entities.raw[self.name]:  # pragma: no coverage
            self._collision_mask = set(entities.raw[self.name]["collision_mask"])
        else:  # pragma: no coverage
            self._collision_mask = {
                "item-layer",
                "object-layer",
                "rail-layer",
                "floor-layer",
                "water-tile",
            }

        for unused_arg in self.unused_args:
            warnings.warn(
                "{} has no attribute '{}'".format(type(self), unused_arg),
                DraftsmanWarning,
                stacklevel=2,
            )
