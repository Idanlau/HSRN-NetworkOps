from napalm import get_network_driver
import json

driver = get_network_driver('ios')
device = driver('10.32.251.246', 'admin', 'ultraconfig')
device.open()
print(json.dumps(device.get_interfaces_ip(), indent=2))
device.close()