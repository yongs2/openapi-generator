# coding: utf-8

"""
    Echo Server API

    Echo Server API

    The version of the OpenAPI document: 0.1.0
    Contact: team@openapitools.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, StrictInt, StrictStr
from typing import Dict, Any
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class TestQueryStyleDeepObjectExplodeTrueObjectAllOfQueryObjectParameter(BaseModel):
    """
    TestQueryStyleDeepObjectExplodeTrueObjectAllOfQueryObjectParameter
    """
    size: Optional[StrictStr] = None
    color: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["size", "color", "id", "name"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TestQueryStyleDeepObjectExplodeTrueObjectAllOfQueryObjectParameter from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of TestQueryStyleDeepObjectExplodeTrueObjectAllOfQueryObjectParameter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in TestQueryStyleDeepObjectExplodeTrueObjectAllOfQueryObjectParameter) in the input: " + _key)

        _obj = cls.model_validate({
            "size": obj.get("size"),
            "color": obj.get("color"),
            "id": obj.get("id"),
            "name": obj.get("name")
        })
        return _obj


