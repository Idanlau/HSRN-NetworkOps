from napalm import get_network_driver

driver = get_network_driver('ios')
device = driver('192.0.2.2', 'username', 'password')

device.open()

# Load the BGP configuration
bgp_config = {
    'asn': 65002,
    'router_id': '192.0.2.2',
    'neighbors': {
        '192.0.2.1': {
            'remote_as': 65001,
            'password': 'neighbor_password',
            'update_source': 'Loopback0',
            'prefix_list_in': 'prefix-list-in',
            'prefix_list_out': 'prefix-list-out',
            'route_map_in': 'route-map-in',
            'route_map_out': 'route-map-out',
            'ebgp_multihop': 2,
            'send_community': True,
            'default_originate': True,
        }
    },
    'address_family': {
        'ipv4': {
            'neighbors': {
                '192.0.2.1': {
                    'activate': True,
                    'route_reflector_client': False,
                }
            }
        }
    }
}

# Push the BGP configuration
device.load_merge_candidate(config=str(bgp_config))
diffs = device.compare_config()

if diffs:
    print(diffs)
    device.commit_config()
else:
    print("No changes required.")

device.close()
