# coding: utf-8

"""
    IP Address Management API

    The IPAM/DHCP Application is a BloxOne DDI service providing IP address management and DHCP protocol features. The IPAM component provides visibility into and provisioning tools to manage networking spaces, monitoring and reporting of entire IP address infrastructures, and integration with DNS and DHCP protocols. The DHCP component provides DHCP protocol configuration service with on-prem host serving DHCP protocol. It is part of the full-featured, DDI cloud solution that enables customers to deploy large numbers of protocol servers to deliver DNS and DHCP throughout their enterprise network.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from ipam.models.ip_space import IPSpace


class TestIPSpace(unittest.TestCase):
    """IPSpace unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IPSpace:
        """Test IPSpace
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IPSpace`
        """
        model = IPSpace()
        if include_optional:
            return IPSpace(
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
                asm_scope_flag = 56,
                comment = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                ddns_client_update = 'client',
                ddns_conflict_resolution_mode = 'check_with_dhcid',
                ddns_domain = '',
                ddns_generate_name = True,
                ddns_generated_prefix = 'myhost',
                ddns_send_updates = True,
                ddns_ttl_percent = 1.337,
                ddns_update_on_renew = True,
                ddns_use_conflict_resolution = True,
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
                header_option_filename = '',
                header_option_server_address = '',
                header_option_server_name = '',
                hostname_rewrite_char = '-',
                hostname_rewrite_enabled = True,
                hostname_rewrite_regex = '[^a-zA-Z0-9_.]',
                id = '',
                inheritance_sources = ipam.models.ip_space_inheritance.IPSpaceInheritance(
                    asm_config = ipam.models.inherited_asm_config.InheritedASMConfig(
                        asm_enable_block = ipam.models.inherited_asm_enable_block.InheritedAsmEnableBlock(
                            action = '', 
                            display_name = '', 
                            source = '', 
                            value = ipam.models.asm_enable_block_.AsmEnableBlock (
                                enable = True, 
                                enable_notification = True, 
                                reenable_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), ), 
                        asm_growth_block = ipam.models.inherited_asm_growth_block.InheritedAsmGrowthBlock(
                            action = '', 
                            display_name = '', 
                            source = '', ), 
                        asm_threshold = ipam.models.inherited_u_int32.InheritedUInt32(
                            action = '', 
                            display_name = '', 
                            source = '', ), 
                        forecast_period = ipam.models.inherited_u_int32.InheritedUInt32(
                            action = '', 
                            display_name = '', 
                            source = '', ), 
                        history = , 
                        min_total = , 
                        min_unused = , ), 
                    ddns_client_update = ipam.models.inherited_string.InheritedString(
                        action = '', 
                        display_name = '', 
                        source = '', ), 
                    ddns_conflict_resolution_mode = ipam.models.inherited_string.InheritedString(
                        action = '', 
                        display_name = '', 
                        source = '', ), 
                    ddns_enabled = ipam.models.inherited_bool.InheritedBool(
                        action = '', 
                        display_name = '', 
                        source = '', ), 
                    ddns_hostname_block = ipam.models.inherited_ddns_hostname_block.InheritedDDNSHostnameBlock(
                        action = '', 
                        display_name = '', 
                        source = '', ), 
                    ddns_ttl_percent = ipam.models.inherited_float.InheritedFloat(
                        action = '', 
                        display_name = '', 
                        source = '', ), 
                    ddns_update_block = ipam.models.inherited_ddns_update_block.InheritedDDNSUpdateBlock(
                        action = '', 
                        display_name = '', 
                        source = '', ), 
                    ddns_update_on_renew = ipam.models.inherited_bool.InheritedBool(
                        action = '', 
                        display_name = '', 
                        source = '', ), 
                    ddns_use_conflict_resolution = , 
                    dhcp_config = ipam.models.inherited_dhcp_config.InheritedDHCPConfig(
                        abandoned_reclaim_time = , 
                        abandoned_reclaim_time_v6 = , 
                        allow_unknown = , 
                        allow_unknown_v6 = , 
                        echo_client_id = , 
                        filters = ipam.models.filter_list.FilterList(
                            action = '', 
                            display_name = '', 
                            source = '', ), 
                        filters_v6 = ipam.models.filter_list.FilterList(
                            action = '', 
                            display_name = '', 
                            source = '', ), 
                        ignore_client_uid = , 
                        ignore_list = ipam.models.ignore_item_list.IgnoreItemList(
                            action = '', 
                            display_name = '', 
                            source = '', ), 
                        lease_time = , 
                        lease_time_v6 = , ), 
                    dhcp_options = ipam.models.inherited_dhcp_option_list.InheritedDHCPOptionList(
                        action = '', ), 
                    dhcp_options_v6 = ipam.models.inherited_dhcp_option_list.InheritedDHCPOptionList(
                        action = '', ), 
                    header_option_filename = , 
                    header_option_server_address = , 
                    header_option_server_name = , 
                    hostname_rewrite_block = ipam.models.inherited_hostname_rewrite_block.InheritedHostnameRewriteBlock(
                        action = '', 
                        display_name = '', 
                        source = '', ), 
                    vendor_specific_option_option_space = ipam.models.inherited_identifier.InheritedIdentifier(
                        action = '', 
                        display_name = '', 
                        source = '', ), ),
                name = 'Example IP Space',
                tags = ipam.models.tags.tags(),
                threshold = ipam.models.utilization_threshold.UtilizationThreshold(
                    enabled = True, 
                    high = 100, 
                    low = 10, ),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                utilization = ipam.models.utilization.Utilization(
                    abandon_utilization = 56, 
                    abandoned = '', 
                    dynamic = '', 
                    free = '', 
                    static = '', 
                    total = '', 
                    used = '', ),
                utilization_v6 = ipam.models.utilization_v6.UtilizationV6(
                    abandoned = 'YQ==', 
                    dynamic = 'YQ==', 
                    static = 'YQ==', 
                    total = 'YQ==', 
                    used = 'YQ==', ),
                vendor_specific_option_option_space = ''
            )
        else:
            return IPSpace(
                name = 'Example IP Space',
        )
        """

    def testIPSpace(self):
        """Test IPSpace"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()