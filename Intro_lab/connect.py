from gns3fy import Gns3Connector, Project, Node, Link
import time
from pprint import pprint

#Local Gns3 server
SERVER_URL = "http://localhost:3080"

# Define the connector object, by default its port is 3080
server = Gns3Connector(url=SERVER_URL)

# Verify connectivity by checking the server version
print(server.get_version())

# Now obtain a project from the server
lab = Project(name="FirstLab", connector=server)

# Show some of its attributes
lab.get()
print(f"{lab.name}:-- Status {lab.status}")

lab.open()
print(lab.status)

for node in lab.nodes:
    node.start()
    print(f"Node: {node.name} -- Node Type: {node.node_type} -- Status: {node.status}")

print(lab.links_summary())

# lab.create_link("PC1", "Ethernet0", "Switch1", "Ethernet0") #unable to create link

# print(lab.links_summary())
