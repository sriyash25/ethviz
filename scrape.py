import time
from web3 import Web3
import subprocess
import json

# connect to geth node
w3 = Web3(Web3.HTTPProvider('http://18.221.34.181:8080'))

# create empty set to store nodes
nodes = set()
nodesip = set()
# Initialize an empty dictionary to store the geolocation data for each IP address
geolocation_data = {}

# repeat for 60 iterations (1 minute)
for i in range(60):
    # get peer info
    peers = w3.geth.admin.peers()

    # check each peer for uniqueness
    for peer in peers:
        if peer['enode'] not in nodes:
            nodes.add(peer['enode'])
            # Find the index of the '@' and ':' characters
            at_index = peer['enode'].index('@')
            colon_index = peer['enode'].rindex(':')
            # Extract the substring between the '@' and ':' characters
            ip = peer['enode'][at_index+1:colon_index]
            nodesip.add(ip)

    # wait for 1 second
    time.sleep(1)

print(nodesip)
print(nodes)
# Loop over the IP addresses and look up the geolocation for each one
for ip_address in nodesip:
    print("api call for", ip_address)
    # Run the curl command and capture the output
    output = subprocess.check_output(['curl', f'https://ipapi.co/{ip_address}/json/?key=v08FW1K7j9eNiegEi4rMvTTvB8QP6YodFPe1VdiiYbPoCHEosR'])

    # Parse the JSON response
    data = json.loads(output)
    print(data)

    # Extract the latitude and longitude from the response
    latitude = data['latitude']
    longitude = data['longitude']

    # Add the geolocation data to the dictionary
    geolocation_data[ip_address] = [longitude, latitude]

# Write the output to a JSON file
with open('./public/latlong.json', 'w') as f:
    json.dump(geolocation_data, f, indent=4)
