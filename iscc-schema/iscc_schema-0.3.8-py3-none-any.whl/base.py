# -*- coding: utf-8 -*-
import json

import jcs
from pydantic import BaseModel as OriginalBaseModel
from pydantic import root_validator


class BaseModel(OriginalBaseModel):
    """Overrides for autogenerated Pydantic Models"""

    class Config:
        extra = "forbid"
        validate_assignment = True
        use_enum_values = True
        orm_mode = True

    @root_validator(pre=True)
    def empty_string_to_default(cls, values):
        """Convert `empty` sting values to `None`."""
        cleaned = {}
        for k, v in values.items():
            cleaned[k] = v if v else None
        return cleaned

    def dict(self, *args, exclude_none=True, exclude_unset=True, by_alias=True, **kwargs):
        # type: (...) -> dict
        """
        Overide defaults to exclude `None` and unset values and translate aliases.

        !!! note
            This overides the default BaseModel.dict()
        """
        return super().dict(
            *args,
            exclude_none=exclude_none,
            exclude_unset=exclude_unset,
            by_alias=by_alias,
            **kwargs,
        )

    def json(self, *args, exclude_none=True, by_alias=True, **kwargs):
        # type: (...) -> str
        """
        Overide defaults to exclude empty fields and use aliases.

        The by_alias=True allows us to generate valid JSON-LD by default. It translates
        our python "_context" property to @context

        !!! note
            This overides the default BaseModel.json()
        """
        return super().json(
            *args,
            exclude_none=exclude_none,
            by_alias=by_alias,
            **kwargs,
        )

    def jcs(self):
        # type: () -> bytes
        """
        Create JCS canonicalized JSON bytestring
        """
        data = self.dict(exclude_unset=False)
        ser = jcs.canonicalize(data)
        des = json.loads(ser)
        if des != data:
            raise ValueError(f"Not canonicalizable {data} round-trips to {des}")
        return ser

    @property
    def iscc_obj(self):
        """
        :return: ISCC-CODE object if iscc_core is available else None
        :rtype: Optional[ic.Code]
        """
        try:
            import iscc_core as ic
        except ImportError:
            raise ImportError("IsccMeta.iscc_obj requires iscc_core package.")
        return ic.Code(self.iscc)
