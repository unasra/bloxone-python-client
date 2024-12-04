# coding: utf-8

"""
    IPAM Federation API

    The DDI IPAM Federation application enables a SaaS administrator to manage multiple IPAM systems from one central control point CSP.    

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from ipam_federation.api.federated_realm_api import FederatedRealmApi

from bloxone_client.api_client import ApiClient


class TestFederatedRealmApi(unittest.TestCase):
    """FederatedRealmApi unit test stubs"""

    def setUp(self) -> None:
        api_instance = ApiClient()
        self.api = FederatedRealmApi(api_instance)

    def tearDown(self) -> None:
        pass

    def test_create(self) -> None:
        """Test case for create

        Create the federated realm.
        """
        pass

    def test_delete(self) -> None:
        """Test case for delete

        Delete federated realm.
        """
        pass

    def test_list(self) -> None:
        """Test case for list

        Retrieve federated realms.
        """
        pass

    def test_read(self) -> None:
        """Test case for read

        Retrieve the federated realm.
        """
        pass

    def test_update(self) -> None:
        """Test case for update

        Update the federated realm.
        """
        pass


if __name__ == '__main__':
    unittest.main()