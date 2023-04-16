import subprocess



'''
ethports: 30301, 30302, 30303, 30304, 30305, 30306, 30307, 30308, 30309, 30310
rpc ports: 443, 7000, 8443, 8445, 8446, 8545, 8546, 8547, 8548, 50051, 5671, 5672      ||||||| 111, 135, 139, 445, 2049, 2100, 6000, 6666, 
http ports: 80, 81, 82, 83 ,84, 443, 8000, 8008, 80069, 8080, 80081, 8880, 8888

flags in command
1. nodename
2. ethport
3. rpc port
4. http port


./final_node_generation.sh -n node2 -r 8547 -h 8008 -e 30304

'''
# eth port, rpc port, http port
node_configs = (
				('30301', '8546', '8080', '0x6d918f4DecDbeCfeD4123dC42b7037D1aEE4D1F9'),
				('30302', '8547', '8008', '0x86cdF72a4a4D409FCE3c0Ec241382539A96345ea'),
				('30303', '8548', '8000', '0x0B0E1a69CAA93513406AC9b7EB893f9818044d52'),
				# ('30304', '8445', '8888' ),
				)

for i in range(len(node_configs)):
	eth_port, rpc_port, http_port, account_address = node_configs[i]
	
	nodename = f"node{i+1}"
	print(nodename, eth_port, rpc_port, http_port)
	#create bootstrap node for the network
	command1 = f"ssh -i '/Users/adityasalian/Desktop/Livin-the-dream/spring-2023/CS-6675/aditya.pem' ubuntu@ec2-18-188-124-55.us-east-2.compute.amazonaws.com 'nohup geth --datadir {nodename} init genesis.json &> /dev/null'"
	command1 = f"ssh -i '/Users/adityasalian/Desktop/Livin-the-dream/spring-2023/CS-6675/aditya.pem' ubuntu@ec2-18-188-124-55.us-east-2.compute.amazonaws.com 'nohup cp /home/ubuntu/.ethereum/keystore {nodename}/keystore  &> /dev/null'"
	command2 = f"ssh -i '/Users/adityasalian/Desktop/Livin-the-dream/spring-2023/CS-6675/aditya.pem' ubuntu@ec2-18-188-124-55.us-east-2.compute.amazonaws.com 'nohup bash /home/ubuntu/final_node_generation.sh -n {nodename} -r {rpc_port} -h {http_port} -e {eth_port} -a {account_address} &> /dev/null'"
	result = subprocess.Popen(command1, shell=True)#, capture_output=True, text=True)
	result = subprocess.Popen(command2, shell=True)#, capture_output=True, text=True)
	print(f'success: {nodename}')



