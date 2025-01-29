# coding: utf-8

"""
    DDI Keys API

    The DDI Keys application is a BloxOne DDI service for managing TSIG keys and GSS-TSIG (Kerberos) keys which are used by other BloxOne DDI applications. It is part of the full-featured, DDI cloud solution that enables customers to deploy large numbers of protocol servers to deliver DNS and DHCP throughout their enterprise network.   

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from keys.api.upload_api import UploadApi

from bloxone_client.api_client import ApiClient


class TestUploadApi(unittest.TestCase):
    """UploadApi unit test stubs"""

    def setUp(self) -> None:
        api_instance = ApiClient()
        self.api = UploadApi(api_instance)

    def tearDown(self) -> None:
        pass

    def test_upload(self) -> None:
        """Test case for upload

        Upload content to the keys service.
        """
        pass


if __name__ == '__main__':
    unittest.main()
