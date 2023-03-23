from gns3fy import Gns3Connector, Project, Node, Link
import time


#Local Gns3 server
SERVER_URL = "http://10.32.251.246/"

# Define the connector object, by default its port is 3080
server = Gns3Connector(url=SERVER_URL)

# Now obtain a project from the server
lab = Project(name="BGP-Config", connector=server)

lab.get()
print(f"{lab.name}:-- Status {lab.status}")
print(lab.project_id)

lab.open()
print(lab.status)

nodes = lab.nodes_summary()


# Create topology nodes

"""arista = lab.create_node(name="Arista", template="Arista vEOS 4.29.1F")
sonic = lab.create_node(name="Sonic", template="Enterprise SONiC 4.0.2")
 They dont work !
"""

# Create network adapters for the nodes
arista = lab.get_node(node_id="8fd3a1d5-3501-422e-aa91-8e7a2d1212cf")
# arista_eth0 = arista.create_nic()

sonic = lab.get_node(node_id="dd1d8065-2f71-4c0e-b6ad-f6bae26d6c6d")
# sonic_eth0 = sonic.create_nic()

# Connect the network adapters
# lab.create_link(arista_eth0, sonic_eth0)

# Start the nodes
arista.start()
sonic.start()

# Wait for the nodes to fully start
time.sleep(3)

print(arista.properties)
# Configure BGP on Arista
arista.config(['enable',
               'configure terminal',
               'router bgp 65001',
               'neighbor 10.0.0.2 remote-as 65002',
               'network 192.168.1.0/24'])

# Configure BGP on Sonic
sonic.config(['sudo su',
              'configure terminal',
              'router bgp 65002',
              'neighbor 10.0.0.1 remote-as 65001',
              'network 192.168.2.0/24'])

# Display BGP neighbor information on Arista
print(arista.config(['show ip bgp neighbor']))
