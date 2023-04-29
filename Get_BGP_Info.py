from napalm import get_network_driver


devices = {"eos":"10.32.251.246", "ios":"10.32.251.246"}

for key in devices:
    print(key, '->', devices[key])
    driver = get_network_driver(key)

    device = driver(hostname=devices[key], username='admin', password='')
    device.open()

    bgp_neighbors = device.get_bgp_neighbors()

    print(bgp_neighbors)

    device.close()
