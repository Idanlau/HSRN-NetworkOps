from napalm import get_network_driver

# Specify the device IP, username, and password
device_ip = '192.0.2.1'
username = 'admin'
password = 'password'


# Create a network driver for Arista EOS
driver = get_network_driver('eos')

# Connect to the device
device = driver(hostname=device_ip, username="admin", password="")
device.open()

# Define the BGP configuration dictionary
bgp_config1 = {
    'asn': 65001,
    'router_id': '192.0.2.1',
    'neighbors': {
        '192.0.2.2': {
            'remote_as': 65002,
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
                '192.0.2.2': {
                    'activate': True,
                    'route_reflector_client': True,
                }
            }
        }
    }
}

# Load the BGP configuration onto the device
device.load_merge_candidate(config=bgp_config1)

# Compare the candidate configuration with the current configuration
diff = device.compare_config()

# If the candidate configuration is different from the current configuration, commit the changes
if diff:
    device.commit_config()

# Disconnect from the device
device.close()
