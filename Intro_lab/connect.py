from gns3fy import Gns3Connector, Project, Node, Link
import time
from pprint import pprint


SERVER_URL = "http://localhost:3080" #What server?

# Define the connector object, by default its port is 3080
server = Gns3Connector(url=SERVER_URL)


# Verify connectivity by checking the server version
print(server.get_version())

# Now obtain a project from the server
lab = Project(name="FirstLab", connector=server)
lab.get()

# Show some of its attributes
print(f"{lab.name}:-- Status {lab.status}")
# test_lab: 4b21dfb3-675a-4efa-8613-2f7fb32e76f -- Status: closed

lab.open()

print(lab.status)
# opened

for node in lab.nodes:
    node.start()
    print(f"Node: {node.name} -- Node Type: {node.node_type} -- Status: {node.status}")


# print(lab.nodes_summary())


print(lab.links_summary())

lab.create_link("PC1", "Ethernet0", "Switch1", "Ethernet0") #unable to create link
# lab.create_link("PC2", "Ethernet0", "Switch1", "Ethernet1")
#
# print(lab.links_summary())
