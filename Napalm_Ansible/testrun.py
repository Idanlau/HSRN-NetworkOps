from napalm import get_network_driver

driver = get_network_driver('eos')

device = driver(hostname='10.32.251.246:5000', username='admin', password='my_password')
device.open()

bgp_neighbors = device.get_bgp_neighbors()

print(bgp_neighbors)

device.close()
