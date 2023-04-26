from netmiko import ConnectHandler

# Define the device details
device1 = {
    "device_type": "arista_eos",
    "ip": "10.32.251.246",
    "username": "admin",
    "password": "admin",
    "port": 5000,
}

device2 = {
    "device_type": "arista_eos",
    "ip": "10.32.251.246",
    "username": "admin",
    "password": "admin",
    "port": 5007,
}

# Connect to the devices
devices = [device1, device2]

for device in devices:
    net_connect = ConnectHandler(**device)

    # Configure BGP
    bgp_commands = [
        "router bgp 65001",
        "neighbor 192.168.1.2 remote-as 65002",
        "neighbor 192.168.1.2 ebgp-multihop 2",
        "network 10.0.0.0/24",
    ]
    output = net_connect.send_config_set(bgp_commands)
    print(output)

    net_connect.disconnect()
# from netmiko import ConnectHandler
#
# net_connect = ConnectHandler(
#     device_type="cisco_xe",
#     host="cisco5.domain.com",
#     username="admin",
#     password="password"
# )
#


