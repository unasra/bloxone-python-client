# coding: utf-8

"""
    IP Address Management API

    The IPAM/DHCP Application is a Universal DDI service providing IP address management and DHCP protocol features. The IPAM component provides visibility into and provisioning tools to manage networking spaces, monitoring and reporting of entire IP address infrastructures, and integration with DNS and DHCP protocols. The DHCP component provides DHCP protocol configuration service with on-prem host serving DHCP protocol. It is part of the full-featured, DDI cloud solution that enables customers to deploy large numbers of protocol servers to deliver DNS and DHCP throughout their enterprise network.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ipam.models.lease_address import LeaseAddress
from ipam.models.lease_range import LeaseRange
from ipam.models.lease_subnet import LeaseSubnet
from typing import Optional, Set
from typing_extensions import Self


class LeasesCommand(BaseModel):
    """
    The __LeasesCommand__ (_dhcp/leases_command_) is used to perform an action on a lease or a set of leases defined by the list of IP addresses or Subnet or Range. Host(s) owning the lease(s) must be available for this action to succeed. The command is executed asynchronously.
    """ # noqa: E501
    address: Optional[List[LeaseAddress]] = Field(
        default=None,
        description=
        "The list of IP addresses to execute the \"command\" on. It can be 1 or more IP addresses."
    )
    command: StrictStr = Field(
        description=
        "The command to perform on the lease(s).  Valid values are:  | command       | description | | :------       | ----------- | | _clear_       | Removes selected lease(s) from the DHCP server(s). This will NOT affect the client that issued the lease. | | _resend-ddns_ | Resends a request to kea-dhcp-ddns to update DNS for selected lease(s). |"
    )
    range: Optional[List[LeaseRange]] = Field(
        default=None,
        description=
        "The list of ranges to execute the \"command\" on. For now it is limited to 1 range."
    )
    subnet: Optional[List[LeaseSubnet]] = Field(
        default=None,
        description=
        "The list of subnets to execute the \"command\" on. For now it is limited to 1 subnet."
    )
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "address", "command", "range", "subnet"
    ]

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
        """Create an instance of LeasesCommand from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in address (list)
        _items = []
        if self.address:
            for _item in self.address:
                if _item:
                    _items.append(_item.to_dict())
            _dict['address'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in range (list)
        _items = []
        if self.range:
            for _item in self.range:
                if _item:
                    _items.append(_item.to_dict())
            _dict['range'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in subnet (list)
        _items = []
        if self.subnet:
            for _item in self.subnet:
                if _item:
                    _items.append(_item.to_dict())
            _dict['subnet'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LeasesCommand from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "address":
            [LeaseAddress.from_dict(_item) for _item in obj["address"]]
            if obj.get("address") is not None else None,
            "command":
            obj.get("command"),
            "range": [LeaseRange.from_dict(_item) for _item in obj["range"]]
            if obj.get("range") is not None else None,
            "subnet":
            [LeaseSubnet.from_dict(_item) for _item in obj["subnet"]]
            if obj.get("subnet") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
