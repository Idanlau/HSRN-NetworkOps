from gns3fy import Gns3Connector, Project, Node, Link
import time
from pprint import pprint

#Local Gns3 server
SERVER_URL = "http://10.32.251.246/"

# Define the connector object, by default its port is 3080
server = Gns3Connector(url=SERVER_URL)

# Now obtain a project from the server
lab = Project(name="BGP-Config", connector=server)

# Show some of its attributes
lab.get()
print(f"{lab.name}:-- Status {lab.status}")

lab.open()
print(lab.status)

# nodes = lab.get_nodes()
# print(nodes)
# Iterate over all nodes and delete them
# for node in nodes:
#     node_id = node["node_id"]
#     lab.delete(node_id=node_id)

# Create the router object
router1 = lab.create_node(name="Router1", template="Arista vEOS 4.29.1F")
router2 = lab.create_node(name="Router2", template="Arista vEOS 4.29.1F")
# Add interfaces to the router
interface1 = router1.add_interface(name='Ethernet0/0', ip='10.1.1.1/24')
interface2 = router1.add_interface(name='Ethernet0/1', ip='10.1.2.1/24')

# Configure BGP on the router
router1.config(['router bgp 65001',
                'neighbor 10.1.1.2 remote-as 65002',
                'neighbor 10.1.1.2 update-source Ethernet0/0',
                'network 192.168.0.0 mask 255.255.255.0'])

# Start the router
router1.start()


"""
router1.config(['router bgp 65001',: This line starts the BGP configuration for router1 with the specified ASN of 65001.

'neighbor 10.1.1.2 remote-as 65002',: This line configures the neighbor router with IP address 10.1.1.2 to use ASN 65002. This specifies which AS the neighboring router is a part of.

'neighbor 10.1.1.2 update-source Ethernet0/0',: This line specifies that the BGP updates will be sent from the Ethernet0/0 interface of the local router to the neighbor router with IP address 10.1.1.2.

'network 192.168.0.0 mask 255.255.255.0']): This line specifies that the network with the address range of 192.168.0.0 and subnet mask of 255.255.255.0 is to be advertised by the local router to its neighboring routers using BGP.
"""


