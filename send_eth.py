from web3 import Web3
import subprocess
import json
import subprocess
from collections import defaultdict
import web3
from populate_network import NodeClient
from init_network import node_configs


if __name__ == "__main__":
	'''
	# eth port, rpc port, http port
	node_configs = (
					('30301', '8546', '8080', '0x6d918f4DecDbeCfeD4123dC42b7037D1aEE4D1F9'),
					('30302', '8547', '8008', '0x86cdF72a4a4D409FCE3c0Ec241382539A96345ea'),
					('30303', '8548', '8000', '0x0B0E1a69CAA93513406AC9b7EB893f9818044d52'),
					# ('30304', '8445', '8888' ),
					)
	'''

	node_port_bindings = {
		'node1' : '8080',
		'node2' : '8008',
		'node3' : '8000',
	}

	port_miner_bindings = {
		'8080' : '0x6d918f4DecDbeCfeD4123dC42b7037D1aEE4D1F9',
		'8008' : '0x86cdF72a4a4D409FCE3c0Ec241382539A96345ea',
		'8000' : '0x0B0E1a69CAA93513406AC9b7EB893f9818044d52'
	}


	sender_port, receiver_port = node_port_bindings['node2'], node_port_bindings['node3']
	amount = 10
	# source_access = NodeClient(sender_port).geth_access
	url = f'http://18.188.124.55:{str(sender_port)}'
	source_access = Web3(Web3.HTTPProvider(url))

	def send_wei(sender, receiver, value):
		pw = "jackfruit"

		# unlocking personal account
		sender_address = Web3.to_checksum_address(sender)
		receiver_address = Web3.to_checksum_address(receiver)
		
		source_access.geth.personal.unlock_account(sender_address, pw)


		tx_params = {
			'from': sender_address,
			'to': receiver_address,
			'value': value,
		}
		tx_hash = source_access.eth.send_transaction(transaction= tx_params)
		return tx_hash


	skey,rkey = port_miner_bindings[sender_port], port_miner_bindings[receiver_port]
	proof = send_wei(sender=skey, receiver=rkey, value=amount)
	# import pdb; pdb.set_trace();
	print(proof)