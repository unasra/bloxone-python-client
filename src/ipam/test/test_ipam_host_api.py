# coding: utf-8

"""
    IP Address Management API

    The IPAM/DHCP Application is a BloxOne DDI service providing IP address management and DHCP protocol features. The IPAM component provides visibility into and provisioning tools to manage networking spaces, monitoring and reporting of entire IP address infrastructures, and integration with DNS and DHCP protocols. The DHCP component provides DHCP protocol configuration service with on-prem host serving DHCP protocol. It is part of the full-featured, DDI cloud solution that enables customers to deploy large numbers of protocol servers to deliver DNS and DHCP throughout their enterprise network.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from ipam.api.ipam_host_api import IpamHostApi


class TestIpamHostApi(unittest.TestCase):
    """IpamHostApi unit test stubs"""

    def setUp(self) -> None:
        self.api = IpamHostApi()

    def tearDown(self) -> None:
        pass

    def test_create(self) -> None:
        """Test case for create

        Create the IPAM host.
        """
        pass

    def test_delete(self) -> None:
        """Test case for delete

        Move the IPAM host to the recycle bin.
        """
        pass

    def test_list(self) -> None:
        """Test case for list

        Retrieve the IPAM hosts.
        """
        pass

    def test_read(self) -> None:
        """Test case for read

        Retrieve the IPAM host.
        """
        pass

    def test_update(self) -> None:
        """Test case for update

        Update the IPAM host.
        """
        pass


if __name__ == '__main__':
    unittest.main()