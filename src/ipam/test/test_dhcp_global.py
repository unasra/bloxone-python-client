# coding: utf-8

"""
    IP Address Management API

    The IPAM/DHCP Application is a BloxOne DDI service providing IP address management and DHCP protocol features. The IPAM component provides visibility into and provisioning tools to manage networking spaces, monitoring and reporting of entire IP address infrastructures, and integration with DNS and DHCP protocols. The DHCP component provides DHCP protocol configuration service with on-prem host serving DHCP protocol. It is part of the full-featured, DDI cloud solution that enables customers to deploy large numbers of protocol servers to deliver DNS and DHCP throughout their enterprise network.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from ipam.models.dhcp_global import DHCPGlobal


class TestDHCPGlobal(unittest.TestCase):
    """DHCPGlobal unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DHCPGlobal:
        """Test DHCPGlobal
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DHCPGlobal`
        """
        model = DHCPGlobal()
        if include_optional:
            return DHCPGlobal(
                asm_config = ipam.models.asm_config.ASMConfig(
                    asm_threshold = 56, 
                    enable = True, 
                    enable_notification = True, 
                    forecast_period = 56, 
                    growth_factor = 56, 
                    growth_type = 'percent', 
                    history = 56, 
                    min_total = 56, 
                    min_unused = 56, 
                    reenable_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                client_principal = '',
                ddns_client_update = '',
                ddns_conflict_resolution_mode = '',
                ddns_domain = '',
                ddns_enabled = True,
                ddns_generate_name = True,
                ddns_generated_prefix = '',
                ddns_send_updates = True,
                ddns_ttl_percent = 1.337,
                ddns_update_on_renew = True,
                ddns_use_conflict_resolution = True,
                ddns_zones = [
                    ipam.models.ddns_zone.DDNSZone(
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
                        zone = 'dns/auth_zone/16d9158d-d0d7-48e1-9a55-087e7aa419d4', )
                    ],
                dhcp_config = ipam.models.dhcp_config.DHCPConfig(
                    abandoned_reclaim_time = 56, 
                    abandoned_reclaim_time_v6 = 56, 
                    allow_unknown = True, 
                    allow_unknown_v6 = True, 
                    echo_client_id = True, 
                    filters = [
                        ''
                        ], 
                    filters_v6 = [
                        ''
                        ], 
                    ignore_client_uid = True, 
                    ignore_list = [
                        ipam.models.ignore_item.IgnoreItem(
                            type = 'client_hex', 
                            value = '01:23:45:67:89:AB', )
                        ], 
                    lease_time = 56, 
                    lease_time_v6 = 56, ),
                dhcp_options = [
                    ipam.models.option_item.OptionItem(
                        group = '', 
                        option_code = '', 
                        option_value = '', 
                        type = '', )
                    ],
                dhcp_options_v6 = [
                    ipam.models.option_item.OptionItem(
                        group = '', 
                        option_code = '', 
                        option_value = '', 
                        type = '', )
                    ],
                dhcp_threshold = ipam.models.dhcp_utilization_threshold.DHCPUtilizationThreshold(
                    enabled = True, 
                    high = 100, 
                    low = 0, ),
                gss_tsig_fallback = True,
                header_option_filename = '',
                header_option_server_address = '',
                header_option_server_name = '',
                hostname_rewrite_char = '',
                hostname_rewrite_enabled = True,
                hostname_rewrite_regex = '',
                id = '',
                kerberos_kdc = '',
                kerberos_keys = [
                    ipam.models.kerberos_key.KerberosKey(
                        algorithm = '', 
                        domain = '', 
                        key = 'a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z6a1b2c3d4e5f6', 
                        principal = '', 
                        uploaded_at = '', 
                        version = 56, )
                    ],
                kerberos_rekey_interval = 56,
                kerberos_retry_interval = 56,
                kerberos_tkey_lifetime = 56,
                kerberos_tkey_protocol = '',
                prefer_option_12 = True,
                remove_suffix_option_81 = True,
                server_principal = '',
                vendor_specific_option_option_space = ''
            )
        else:
            return DHCPGlobal(
        )
        """

    def testDHCPGlobal(self):
        """Test DHCPGlobal"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()