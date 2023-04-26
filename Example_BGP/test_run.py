import napalm
from tabulate import tabulate
from jinja2 import Environment, FileSystemLoader
import yaml


def main():
    driver_ios = napalm.get_network_driver("ios")
    driver_iosxr = napalm.get_network_driver("iosxr")
    driver_vrp = napalm.get_network_driver("ce")
    device_list = [["ios-r3", "ios", "router"],["vrp-r2", "vrp", "router"]]
    # device_list = [["ios-sw2","ios", "switch"],["iosxr-r1", "iosxr", "router"],
    # ["ios-r3", "ios", "router"],["vrp-r2", "vrp", "router"],["vrp-sw1", "vrp", "switch"]]
    network_devices = []
    for device in device_list:
        if device[1] == "ios":
            network_devices.append(
                driver_ios(
                    hostname=device[0],
                    username="codingnetworks",
                    password="Coding.Networks1"
                )
            )
        elif device[1] == "iosxr":
            network_devices.append(
                driver_iosxr(
                    hostname=device[0],
                    username="codingnetworks",
                    password="Coding.Networks1"
                )
            )
        elif device[1] == "vrp":
            network_devices.append(
                driver_vrp(
                    hostname=device[0],
                    username="codingnetworks",
                    password="Coding.Networks1"
                )
            )
    devices_table = [["hostname", "vendor", "model", "uptime", "serial_number"]]

    for device in network_devices:
        print("Connecting to {} ...".format(device.hostname))
        device.open()
        print("Getting device facts")
        device_facts = device.get_facts()
        devices_table.append([device_facts["hostname"],
                              device_facts["vendor"],
                              device_facts["model"],
                              device_facts["uptime"],
                              device_facts["serial_number"]
                              ])
        # Testing Getters
        device.load_merge_candidate(filename=None, config=get_template_config(device_facts["vendor"]))
        print("\nDiff:")
        print(device.compare_config())
        # You can commit or discard the candidate changes.
        try:
            choice = input("\nWould you like to commit these changes? [yN]: ")
        except NameError:
            choice = input("\nWould you like to commit these changes? [yN]: ")
        if choice == "y":
            print("Committing ...")
            device.commit_config()
        else:
            print("Discarding ...")
            device.discard_config()
        device.close()
        print("Done.")
    print(tabulate(devices_table, headers="firstrow"))


def get_template_config(vendor):
    # This loads data from YAML into Python dictionary
    config_data = yaml.load(open('{}_template.yml'.format(vendor)), Loader=yaml.FullLoader)
    # This line uses the current directory and loads the jinja2 template
    env = Environment(loader=FileSystemLoader('.'), trim_blocks=True, lstrip_blocks=True)
    template = env.get_template('{}_template.j2'.format(vendor))
    # Return the template with data
    print(template.render(config_data))
    return (template.render(config_data))


if __name__ == '__main__':
    main()