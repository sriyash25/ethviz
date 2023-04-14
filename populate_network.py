import time
from web3 import Web3
import subprocess
import json
import subprocess
import os
import signal

class NodeClient:
	geth_access = None
	peer_list = []

	def __init__(self, port):
		url = f'http://18.188.124.55:{str(port)}'

		# connect to bootstrap node
		self.geth_access = Web3(Web3.HTTPProvider(url))
	
	def get_nodeid(self):
		return self.geth_access.geth.admin.node_info().id
	
	def get_enode(self):
		enode_ = self.geth_access.geth.admin.node_info().enode
		print(enode_)
		return enode_
	
	def add_peer(self, enode):
		print(enode)
		self.geth_access.geth.admin.add_peer(enode)
		self.peer_list.append(enode)
		print('Successfully added peer')
	
	def get_peers(self):
		# self.peer_list = self.geth_access.geth.admin.peers()
		# print(f'Peers for Node: {self.peer_list}\n Length: {len(self.peer_list)}')
		return self.peer_list


if __name__ == "__main__":
	'''
	4 nodes in the network atm:

	HTTP Ports to Use:
	8080
	8008
	8000
	8888
	'''
	pc0 = NodeClient(8080)
	pc1 = NodeClient(8008)
	pc2 = NodeClient(8000)
	pc3 = NodeClient(8888)


	'''
	Graph Layout

	0 - 1,2
	1 - 0,3
	2 - 0,3
	3 - 1,2
	'''
	pc0.add_peer(pc1.get_enode())
	pc0.add_peer(pc2.get_enode())
	pc1.add_peer(pc3.get_enode())
	pc2.add_peer(pc3.get_enode())

	# pc0.get_peers()
	adj_list = {
		pc0.get_enode() : pc0.get_peers(),
		pc1.get_enode() : pc1.get_peers(),
		pc2.get_enode() : pc2.get_peers(),
		pc3.get_enode() : pc3.get_peers(),
	}
	# import pdb; pdb. set_trace();

with  open("pvtnetwork.json", "w+") as opfile:
	json.dump(adj_list, opfile)
