import time
from web3 import Web3
import subprocess
import json
import subprocess
from collections import defaultdict
import os
import signal

# node1 : node2
class CreateLink:
	source = None
	dest = None
	source_access = None
	dest_access = None
	peer_list = []
	# self.

	ethports = {
		'node0' : '8080',
		'node1' : '8008',
		'node2' : '8000',
		# 'node3' : '30303',
		'node4' : '8888',
		# 'node5' : '80069',
	}

	def __init__(self, source, dest, create = True):
		self.source = source
		self.dest = dest

		port1, port2 = self.ethports[source], self.ethports[dest]

		self.dest_url = f'http://18.188.124.55:{str(port2)}'
		self.dest_access = Web3(Web3.HTTPProvider(self.dest_url))
		
		

		# create accesses for both source and destination nodes
		# import pdb; pdb.set_trace();
		if create:
			self.create_new_node(self.source)
		self.source_url = f'http://18.188.124.55:{str(port1)}'
		self.source_access = Web3(Web3.HTTPProvider(self.source_url))
		
		
	
	def create_new_node(self, nodename):
		# try: 
		# eth port, rpc port, http port
		# node_configs = (
		# 	('30301', '8546', '8080' ),
		# 	('30302', '8547', '8008' ),
		# 	('30303', '8548', '8000' ),
		# 	('30304', '8445', '8888' ), # using this as the new node set while spinning up new node. hardcoding for now.
		# 	# ('30305', '8549', '80069') 
		# 	)
		node_configs = (
			('30301', '8546', '8080', '0x6d918f4DecDbeCfeD4123dC42b7037D1aEE4D1F9'),
			('30302', '8547', '8008', '0x86cdF72a4a4D409FCE3c0Ec241382539A96345ea'),
			('30303', '8548', '8000', '0x0B0E1a69CAA93513406AC9b7EB893f9818044d52'),
			('30304', '8445', '8888', '0x3135AdF27d0aE632FbedE4D8F2e78e269EaACF06')
		)
		eth_port, rpc_port, http_port, account_address = node_configs[-1]
		# nodename = f"node{i}"
		print(nodename, eth_port, rpc_port, http_port)
		#create bootstrap node for the network
		command = f"ssh -i '/Users/adityasalian/Desktop/Livin-the-dream/spring-2023/CS-6675/aditya.pem' ubuntu@ec2-18-188-124-55.us-east-2.compute.amazonaws.com 'nohup bash /home/ubuntu/final_node_generation.sh -n {nodename} -r {rpc_port} -h {http_port} -e {eth_port} -a {account_address} &> /dev/null'"
		result = subprocess.Popen(command, shell=True)

		
		# except Exception as e:
		# 	print(e)

	def add_edge(self):
		# try:
		# get enode of dest node
		# import pdb; pdb.set_trace();
		time.sleep(2)
		enode = self.source_access.geth.admin.node_info().enode
		print(enode)

		#add the edge from the fetched enode
		self.dest_access.geth.admin.add_peer(enode)
		print(f'Successfully added edge {self.source} <--------> {self.dest}')
		# except Exception as e:
		# 	print(e)


def get_new_connections(OG_GRAPH_PATH, NEW_GRAPH_CONNECTIONS_PATH):

	with open(OG_GRAPH_PATH, 'r') as f:
		original_graph = json.load(f)
		existing_nodes = set()

	for og_node in original_graph['nodes']:
		existing_nodes.add(og_node['id'])

	with open(NEW_GRAPH_CONNECTIONS_PATH, 'r') as f:
		data = json.load(f)

	new_edges = defaultdict(list)

	for node in data['links']:
		new_node = node['target']['id']
		connection = node['source']['id']

		if new_node not in existing_nodes:
			new_edges[new_node].append(connection)
	return new_edges



if __name__ == '__main__':

	og_path = 'src/data.json'
	cur_path = '/Users/adityasalian/Downloads/graph-data.json'
	adj_matrix = get_new_connections(og_path, cur_path)
	print(adj_matrix)

	# # Open the file and read the contents into a string
	# with open('adj_list.json', 'r') as f:
	# 	graph_data = f.read()

	# Use the json.loads() function to convert the string to a dictionary
	# adj_matrix = json.loads(graph_data)

	for source, neighbors in adj_matrix.items():
		for dest in neighbors:
			
			# pass create = False flag to bypass node creation.
			CreateLink(source,dest).add_edge()

