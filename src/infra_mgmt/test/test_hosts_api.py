# coding: utf-8

"""
    Infrastructure Management API

    The **Infrastructure Management API** provides a RESTful interface to manage Infrastructure Hosts and Services objects.  The following is a list of the different Services and their string types (the string types are to be used with the APIs for the `service_type` field):  | Service name | Service type |   | ------ | ------ |   | Access Authentication | authn |   | Anycast | anycast |   | Data Connector | cdc |   | DHCP | dhcp |   | DNS | dns |   | DNS Forwarding Proxy | dfp |   | NIOS Grid Connector | orpheus |   | MS AD Sync | msad |   | NTP | ntp |   | BGP | bgp |   | RIP | rip |   | OSPF | ospf |    ---   ### Hosts API  The Hosts API is used to manage the Infrastructure Host resources. These include various operations related to hosts such as viewing, creating, updating, replacing, disconnecting, and deleting Hosts. Management of Hosts is done from the Cloud Services Portal (CSP) by navigating to the Manage -> Infrastructure -> Hosts tab.  ---   ### Services API  The Services API is used to manage the Infrastructure Service resources (a.k.a. BloxOne applications). These include various operations related to hosts such as viewing, creating, updating, starting/stopping, configuring, and deleting Services. Management of Services is done from the Cloud Services Portal (CSP) by navigating to the Manage -> Infrastructure -> Services tab.  ---   ### Detail APIs  The Detail APIs are read-only APIs used to list all the Infrastructure resources (Hosts and Services). Each resource record returned also contains information about its other associated resources and the status information for itself and the associated resource(s) (i.e., Host/Service status).  ---   

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from infra_mgmt.api.hosts_api import HostsApi

from bloxone_client.api_client import ApiClient


class TestHostsApi(unittest.TestCase):
    """HostsApi unit test stubs"""

    def setUp(self) -> None:
        api_instance = ApiClient()
        self.api = HostsApi(api_instance)

    def tearDown(self) -> None:
        pass

    def test_assign_tags(self) -> None:
        """Test case for assign_tags

        Assign tags for list of hosts.
        """
        pass

    def test_create(self) -> None:
        """Test case for create

        Create a Host resource.
        """
        pass

    def test_delete(self) -> None:
        """Test case for delete

        Delete a Host resource.
        """
        pass

    def test_disconnect(self) -> None:
        """Test case for disconnect

        Disconnect a Host by resource ID.
        """
        pass

    def test_list(self) -> None:
        """Test case for list

        List all the Host resources for an account.
        """
        pass

    def test_read(self) -> None:
        """Test case for read

        Get a Host resource.
        """
        pass

    def test_replace(self) -> None:
        """Test case for replace

        Migrate a Host's configuration from one to another.
        """
        pass

    def test_unassign_tags(self) -> None:
        """Test case for unassign_tags

        Unassign tag for the list hosts.
        """
        pass

    def test_update(self) -> None:
        """Test case for update

        Update a Host resource.
        """
        pass


if __name__ == '__main__':
    unittest.main()
