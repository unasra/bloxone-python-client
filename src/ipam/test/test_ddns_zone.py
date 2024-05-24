# coding: utf-8

"""
    IP Address Management API

    The IPAM/DHCP Application is a BloxOne DDI service providing IP address management and DHCP protocol features. The IPAM component provides visibility into and provisioning tools to manage networking spaces, monitoring and reporting of entire IP address infrastructures, and integration with DNS and DHCP protocols. The DHCP component provides DHCP protocol configuration service with on-prem host serving DHCP protocol. It is part of the full-featured, DDI cloud solution that enables customers to deploy large numbers of protocol servers to deliver DNS and DHCP throughout their enterprise network.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from ipam.models.ddns_zone import DDNSZone


class TestDDNSZone(unittest.TestCase):
    """DDNSZone unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DDNSZone:
        """Test DDNSZone
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DDNSZone`
        """
        model = DDNSZone()
        if include_optional:
            return DDNSZone(
                fqdn = '',
                gss_tsig_enabled = True,
                nameservers = [
                    ipam.models.ipamsvc_nameserver.ipamsvcNameserver(
                        client_principal = '', 
                        gss_tsig_fallback = True, 
                        kerberos_rekey_interval = 56, 
                        kerberos_retry_interval = 56, 
                        kerberos_tkey_lifetime = 56, 
                        kerberos_tkey_protocol = '', 
                        nameserver = '', 
                        server_principal = '', )
                    ],
                tsig_enabled = True,
                tsig_key = ipam.models.tsig_key.TSIGKey(
                    algorithm = '', 
                    comment = '', 
                    key = 'MTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTA=', 
                    name = '', 
                    protocol_name = '', 
                    secret = '', ),
                view = '',
                view_name = '',
                zone = 'dns/auth_zone/16d9158d-d0d7-48e1-9a55-087e7aa419d4'
            )
        else:
            return DDNSZone(
                zone = 'dns/auth_zone/16d9158d-d0d7-48e1-9a55-087e7aa419d4',
        )
        """

    def testDDNSZone(self):
        """Test DDNSZone"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()