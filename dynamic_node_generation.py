import time
from web3 import Web3
import subprocess
import json
import subprocess
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
		'node1' : '30301',
		'node2' : '30302',
		'node3' : '30303',
		'node4' : '30304',
		'node5' : '30305',
	}

	def __init__(self, source, dest):
		self.source = source
		self.dest = dest

		port1, port2 = self.ethports[source], self.ethports[dest]

		source_url = f'http://18.188.124.55:{str(port1)}'
		dest_url = f'http://18.188.124.55:{str(port2)}'

		# create accesses for both source and destination nodes
		self.source_access = Web3(Web3.HTTPProvider(source_url))
		self.create_new_node(self, dest)
		self.dest_access = Web3(Web3.HTTPProvider(dest_url))
	
	def create_new_node(self, nodename):
		try: 
			# eth port, rpc port, http port
			node_configs = (
				('30301', '8546', '8080' ),
				('30302', '8547', '8008' ),
				('30303', '8548', '8000' ),
				('30304', '8445', '8888' ),
				('30305', '8446', '8880') # using this as the new node set while spinning up new node. hardcoding for now.
				)
			eth_port, rpc_port, http_port = node_configs[-1]
			# nodename = f"node{i}"
			print(nodename, eth_port, rpc_port, http_port)
			#create bootstrap node for the network
			command1 = f"ssh -i '/Users/adityasalian/Desktop/Livin-the-dream/spring-2023/CS-6675/aditya.pem' ubuntu@ec2-18-188-124-55.us-east-2.compute.amazonaws.com 'nohup geth --datadir {nodename} init genesis.json &> /dev/null'"
			command2 = f"ssh -i '/Users/adityasalian/Desktop/Livin-the-dream/spring-2023/CS-6675/aditya.pem' ubuntu@ec2-18-188-124-55.us-east-2.compute.amazonaws.com 'nohup bash /home/ubuntu/final_node_generation.sh -n {nodename} -r {rpc_port} -h {http_port} -e {eth_port} &> /dev/null'"
			result1 = subprocess.Popen(command1, shell=True)#, capture_output=True, text=True)
			result2 = subprocess.Popen(command2, shell=True)#, capture_output=True, text=True)``
			# print(f'success: {i}')
		
		except Exception as e:
			print(e)

	def add_edge(self):
		try:
			# get enode of dest node
			enode = self.dest_access.geth.admin.node_info().enode

			#add the edge from the fetched enode
			self.source_access.geth.admin.add_peer(enode)
			print(f'Successfully added edge {self.source} -------- {self.dest}')
		except Exception as e:
			print(e)






if __name__ == '__main__':
	# read json file 
	'''
	{
		u:[v1,v2,v3...]
		u2: v2
	}
	'''
	# Open the file and read the contents into a string
	with open('adj_list.json', 'r') as f:
		graph_data = f.read()

	# Use the json.loads() function to convert the string to a dictionary
	adj_matrix = json.loads(graph_data)

	for source, neighbors in adj_matrix.items():
		for dest in neighbors:
			CreateLink(source,dest).add_edge()

