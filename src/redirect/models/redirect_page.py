# coding: utf-8

"""
    BloxOne Redirect API

    You can configure BloxOne Threat Defense Cloud to redirect traffic to the Infoblox server that displays the default or customized redirect page. You can redirect traffic to a custom destination using custom redirects. 

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self


class RedirectPage(BaseModel):
    """
    The Redirect Page object.  When blocking users from accessing certain domains, you can redirect them to a page that delivers a default message about the action. You can also set a redirect page of your own or customize the redirect message.
    """ # noqa: E501
    content: Optional[StrictStr] = Field(
        default=None,
        description=
        "The content of the redirect page for the \"custom\" redirect type.")
    created_time: Optional[datetime] = Field(
        default=None,
        description="The time when this Redirect Page object was created.")
    redirect_ip_address: Optional[StrictStr] = Field(
        default=None, description="The redirect IPv4 address.")
    redirect_ipv6_address: Optional[StrictStr] = Field(
        default=None, description="The redirect IPv6 address.")
    smart: Optional[StrictBool] = Field(
        default=None, description="Whether the redirect type is smart")
    type: Optional[StrictStr] = Field(
        default=None,
        description=
        "The type of the redirect page that can be \"default\" or \"custom\".")
    updated_time: Optional[datetime] = Field(
        default=None,
        description="The time when this Redirect Page object was last updated."
    )
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "content", "created_time", "redirect_ip_address",
        "redirect_ipv6_address", "smart", "type", "updated_time"
    ]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['default', 'custom']):
            raise ValueError(
                "must be one of enum values ('default', 'custom')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of RedirectPage from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "created_time",
            "updated_time",
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RedirectPage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "content":
            obj.get("content"),
            "created_time":
            obj.get("created_time"),
            "redirect_ip_address":
            obj.get("redirect_ip_address"),
            "redirect_ipv6_address":
            obj.get("redirect_ipv6_address"),
            "smart":
            obj.get("smart"),
            "type":
            obj.get("type"),
            "updated_time":
            obj.get("updated_time")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj