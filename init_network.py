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
				('30301', '8546', '8080' ),
				('30302', '8547', '8008' ),
				('30303', '8548', '8000' ),
				('30304', '8445', '8888' ),
				)

for i in range(len(node_configs)):
	eth_port, rpc_port, http_port = node_configs[i]
	
	nodename = f"node{i}"
	print(nodename, eth_port, rpc_port, http_port)
	#create bootstrap node for the network
	command =  f"ssh -i '/Users/adityasalian/Desktop/Livin-the-dream/spring-2023/CS-6675/aditya.pem' ubuntu@ec2-18-188-124-55.us-east-2.compute.amazonaws.com 'nohup bash /home/ubuntu/final_node_generation.sh -n {nodename} -r {rpc_port} -h {http_port} -e {eth_port} &> /dev/null'"
	result = subprocess.Popen(command, shell=True)#, capture_output=True, text=True)``
	print(f'success: {i}')
	# break






# # create bootstrap node for the network
# n1, p1,p2,p3 = "node1", '8546', '8080', '30301'
# command_boot = f"ssh -i '/Users/adityasalian/Desktop/Livin-the-dream/spring-2023/CS-6675/aditya.pem' ubuntu@ec2-18-188-124-55.us-east-2.compute.amazonaws.com 'nohup bash /home/ubuntu/final_node_generation.sh -n {n1} -r {p1} -h {p2} -e {p3} &> /dev/null'"

# n1, p1,p2,p3 = "node2", '8547', '8008', '30302'
# command =  f"ssh -i '/Users/adityasalian/Desktop/Livin-the-dream/spring-2023/CS-6675/aditya.pem' ubuntu@ec2-18-188-124-55.us-east-2.compute.amazonaws.com 'nohup bash /home/ubuntu/final_node_generation.sh -n {n1} -r {p1} -h {p2} -e {p3} &> /dev/null'"

# result = subprocess.Popen(command_boot, shell=True)#, capture_output=True, text=True)
# result2 = subprocess.Popen(command, shell=True)#, capture_output=True, text=True)
# os.kill(result.pid, signal.SIGINT)
# os.kill(result2.pid, signal.SIGINT)
# raise KeyboardInterrupt("Added Bootstrap Node to the Network")


