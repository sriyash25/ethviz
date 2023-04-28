
<p style="color: red; font-weight: bold">>>>>>  gd2md-html alert:  ERRORs: 0; WARNINGs: 1; ALERTS: 7.</p>
<ul style="color: red; font-weight: bold"><li>See top comment block for details on ERRORs and WARNINGs. <li>In the converted Markdown or HTML, search for inline alerts that start with >>>>>  gd2md-html alert:  for specific instances that need correction.</ul>

<p style="color: red; font-weight: bold">Links to alert messages:</p><a href="#gdcalert1">alert1</a>
<a href="#gdcalert2">alert2</a>
<a href="#gdcalert3">alert3</a>
<a href="#gdcalert4">alert4</a>
<a href="#gdcalert5">alert5</a>
<a href="#gdcalert6">alert6</a>
<a href="#gdcalert7">alert7</a>

<p style="color: red; font-weight: bold">>>>>> PLEASE check and correct alert issues and delete this message and the inline alerts.<hr></p>



# **Abstract**


# The ethereum P2P network is a widely active P2P network which lays special emphasis on the anonymity of the nodes within its network. Analyzing this network for insights into metrics like its topology, network latency, etc are challenging due to two reasons- the asynchronous and decentralized communication routine followed by nodes in the network, and; the rapid growth of the Ethereum network. Furthermore, due to this opaque nature of the network, even private networks (where anonymity is not as high of a priority) is rendered opaque to the end users when they desire to interact with the network. With this project, we aim to address these two domains by- extracting insights into the underlying node discovery protocol of the ethereum network by discovering new peers in the network and plot their geographical spread, and; create a GUI for a private ethereum network to reduce the cognitive overload on the end user of the private ethereum network and enhance their user experience. 


# **Introduction**

Ethereum, a widely used P2P works at this gargantuan scale where it becomes difficult to get a holistic view of the network and its topology due to the way the nodes in the network are connected to each other. This opacity within the network is exacerbated because the nodes in the network interact with each other not only in a decentralized mechanism, but also because these interactions are asynchronous in nature. 

The Ethereum network has undergone significant growth and adoption in recent years, as evidenced by the surge in daily transaction volume from 50,000 in January 2017 to over 4 million in April 2023, and the expansion of the network's address count from 10 million in January 2018 to over 180 million in the same period. These statistics underscore the dynamic and evolving nature of the Ethereum network, which necessitates continuous efforts to analyze and understand its topology. The rapid pace of change in the network's topology poses a challenge for researchers seeking to comprehend and monitor the network in real time to derive insights into the topology and overall performance throughput of the network. 

The dynamic nature of the Ethereum network also necessitates real-time analysis to address issues related to network latency and energy consumption. With over 180 million addresses and counting, the Ethereum network is geographically distributed, and nodes may experience varying degrees of network latency. This can result in slower transaction times and hinder the network's overall performance. For instance, the average gas price on the Ethereum network has varied from around 1 gwei to over 500 gwei in recent years, according to Etherscan, which suggests congestion and inefficiencies in the network. Real-time monitoring can help identify and address these issues before they impact users and the network's overall health. Moreover, as the Ethereum network grows, so does its energy consumption. Real-time analysis can help optimize connections to nodes such that- they are geographically distributed closer to each other such that there is reduced network latency; and secondly, they are distributed across energy efficient zones

 \
With our project, we aim to shine a light on the geographical spread of the nodes within the network. Commenting on the distance between nodes and understanding how they are connected to each other is a complex task, but one that we are tackling head-on with this project. By shining a light on a portion of the Ethereum network, we aim to provide a toolkit which can be employed in the future to enhance the network's overall performance and provide valuable insights to developers and users alike.


# **Project Objectives**

Our project has two main objectives - analyzing node discovery patterns, and creating a GUI to enable ease of use for end users to interact with the ethereum network. Firstly, we aim to derive valuable network topology insights from the Ethereum network by leveraging the power of its node discovery protocol. By rapidly discovering nodes with a custom node which drops connections with these nodes instantly to connect with different newer nodes in the network, we can gain valuable insights into the network's topology, including the location of nodes and the connections between them. This will help us to better understand the dynamics of the Ethereum network and improve its overall performance.

Additionally, we recognize that Ethereum has certain properties that are transferable to private networks where anonymity, while important, need not be as heavily emphasized upon, as in the public network. With this in mind, we have designed a GUI to enhance the user experience of participants in a private network wherein they can add a private node of their own and connect to their peers with a simple click. The motivation behind developing this GUI was to create an interface for the end users of the private ethereum network to interact with the network without needing to understand the underlying intricacies of Ethereum and create an abstraction for them from interacting with the Go Ethereum console to conduct basic operations like connecting to peers or sending transactions. The objective of our project is to make it easy for participants to access and use and understand the network, ultimately leading to greater adoption and usage. Thus, with our project, we are taking a stride to make Ethereum as a network, more accessible and transparent to the user.


# **System Architecture**



<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image1.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image1.png "image_tooltip")


**Figure 1. System Architecture of our Project**

The System Architecture for Ethereum node discovery consists of a backend and frontend setup. The backend is composed of an AWS EC2 instance hosting a Geth Ethereum client and a Flask server responsible for setting up the node over SSH and communicating with it via HTTP. The frontend comprises a React app with Tailwind, which consumes JSON files with discovered nodes generated by the Flask server. Visualization libraries such as Chart.js, D3-geo, React-simple-maps, and React-force-graph-3d are used to visualize the nodes into graphs, which can be displayed on the frontend. This architecture enables efficient Ethereum node discovery and visualization. Figure 1 represents a high level overview of our architecture.


# **Experiments and Results**


### **System Setup**

For all the experiments (unless otherwise specified), we created a custom node for discovering new nodes in the Ethereum network. We used AWS’ t2.micro EC2 instance to set up our node for this task. The location for our client node was set to US-East (Ohio). We opted for the light mode configuration for this task due to our limitations on hardware, compute and the interest of time. We observed that our node was rapidly discovering new nodes in the network and dropping connections with them almost instantly to connect with new nodes.


### **Data Collection Methodology**

**Collecting IP Addresses: **We collect peer IP addresses by connecting to our geth node using the Web3 library and retrieving information about connected peers using the `geth.admin.peers()`function. For each peer, we extract its enode URL, which contains its IP address and port number.

**Converting IP Addresses to Geolocation: **To convert IP addresses to geolocation, we use the ipapi.co API, which provides an easy-to-use service for geolocating IP addresses. The API allows us to retrieve information about each IP address, including its country, region, city, latitude, and longitude. We use the curl command to send a request to the API for each IP address that we collect. The API returns a JSON response containing the geolocation information for the IP address. We extract the latitude and longitude from the response and store them in a dictionary along with the IP address. We also extract other useful information such as the country, region, and city for network visualization and analysis.

**Converting IP Addresses to XOR and Physical Distance: **In a peer-to-peer network, determining the distance between nodes is crucial to optimize message routing and promote efficient message propagation.We will now dresses are converted to XOR and how physical distance is calculated between nodes.

**Converting IP Addresses to XOR: **These hexadecimal values which are the enode IDs are used to calculate the XOR distance between each pair of nodes using the `xor_distance()` function. This function takes two hexadecimal enode IDs as input and returns the XOR distance between them as an integer. Our implementation uses the XOR distance metric to determine the closest nodes for routing messages based on network topology. Nodes with a smaller XOR distance are closer to each other in terms of their network topology and thus serve as more efficient routes for message propagation.

**Calculating Physical Distance between IP Addresses: **To calculate the physical distance between IP addresses, we use the Haversine formula, which accounts for the Earth's curvature. The `haversine()` function takes the latitude and longitude of two points as input and returns their great-circle distance in kilometers. Our implementation uses the physical distance metric to determine the closest nodes in terms of geographic location. Nodes with a smaller physical distance are closer to each other in terms of geographic location.


### **Experiment 1- Analyzing the Geographical Spread of Our Node Discovery Process [HARD]** \


While discovering new nodes in the network, we extracted details like the IP addresses, node IDS, and the data exchanged for these newly formed peers. We were able to discover 115 nodes in 5 minutes of our node discovery run. Figure x denotes the locations of the nodes we connected to.



<p id="gdcalert2" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image2.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert3">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image2.png "image_tooltip")


**Figure 2. Geographical Spread of Discovered Nodes**

According to Ethereum’s Kademlia protocol for node discovery, each node in the network is assigned a unique ID based on its IP address, which allows for efficient peer discovery and helps to ensure the network remains decentralized.  According to this protocol, the nodes are organized into a binary tree structure, with each node being placed in a bucket based on its distance from the node performing the search. The nodes, when asked by a node to return a peer, return a node from their peer list that is closest to the querying node’s node ID. 

While it is claimed that the Kademlia protocol is not directly related to node location or geographic region, the distance metric used by the protocol is based on the XOR of the node IDs. We observed that the protocol does factor in the geographic distance between nodes to some extent. Nodes with similar IP addresses or in the same geographic region may have closer node IDs and be placed in the same bucket; we cannot comment on whether there is a direct relationship that we can infer. We created a module to monitor the data exchanged between our discovery node and its peer to extract draw relationships between the data exchanged and its relationship with the distance metrics specified by us.

Figure 3 highlights our findings. The X-axis of our plot represents the Euclidean distance between the nodes that we connected to (the geographical distance), while the Y-axis represents the XOR distance dictated by the Kademlia protocol. We normalized these distances in the 0-1 scale to compare both these distance metrics with a common framework. The different sized scatters on the graph indicate the size of data exchanged between nodes in this process. 



<p id="gdcalert3" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image3.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert4">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image3.png "image_tooltip")


**Figure 3. XOR vs. Euclidean Distance Plot with Data Exchange Rates**

_Observation and Inferences_

We observed that while our node was situated in Ohio, it connected to a lot of nodes located in the US and Europe. The interesting feature to note here is that Asian regions were the least likely to connect with our node during this client discovery process. Given that this region lies geographically farthest from our node, it is evident that the Kademlia protocol indeed factors in the geographical distance between nodes during node discovery. This also comments on how Kademlia is factoring network latency and throughput implicitly within the network. Another interesting observation here is the size of the bubbles in the plot here. As explained previously, these bubbles indicate the amount of data that was exchanged between our node with the node connected in a particular region. We noticed how our node exchanges the most data with nodes in the UK and Germany. It is interesting to see that the nodes located in the US were not the most likely choices for our node to connect to, which is also reflected from the size of the bubbles from our chart here. It is evident that the Kademlia protocol dictates the node to connect and exchange data with nodes which lie relatively closer to our node geographically.


<table>
  <tr>
   <td><strong>Country</strong>
   </td>
   <td><strong>Total Data Exchanged (bytes)</strong>
   </td>
   <td><strong>Number of Nodes discovered</strong>
   </td>
   <td><strong>Data Exchanged per node (bytes)</strong>
   </td>
  </tr>
  <tr>
   <td>Germany
   </td>
   <td><p style="text-align: right">
814660</p>

   </td>
   <td><p style="text-align: right">
39</p>

   </td>
   <td><p style="text-align: right">
20889</p>

   </td>
  </tr>
  <tr>
   <td>United Kingdom
   </td>
   <td><p style="text-align: right">
370155</p>

   </td>
   <td><p style="text-align: right">
12</p>

   </td>
   <td><p style="text-align: right">
30846</p>

   </td>
  </tr>
  <tr>
   <td>United States
   </td>
   <td><p style="text-align: right">
270150</p>

   </td>
   <td><p style="text-align: right">
15</p>

   </td>
   <td><p style="text-align: right">
18010</p>

   </td>
  </tr>
  <tr>
   <td>Japan
   </td>
   <td><p style="text-align: right">
198360</p>

   </td>
   <td><p style="text-align: right">
13</p>

   </td>
   <td><p style="text-align: right">
15258</p>

   </td>
  </tr>
  <tr>
   <td>France
   </td>
   <td><p style="text-align: right">
84046</p>

   </td>
   <td><p style="text-align: right">
4</p>

   </td>
   <td><p style="text-align: right">
21012</p>

   </td>
  </tr>
  <tr>
   <td>Finland
   </td>
   <td><p style="text-align: right">
59789</p>

   </td>
   <td><p style="text-align: right">
6</p>

   </td>
   <td><p style="text-align: right">
9965</p>

   </td>
  </tr>
  <tr>
   <td>Singapore
   </td>
   <td><p style="text-align: right">
30617</p>

   </td>
   <td><p style="text-align: right">
5</p>

   </td>
   <td><p style="text-align: right">
6123</p>

   </td>
  </tr>
  <tr>
   <td>Turkey
   </td>
   <td><p style="text-align: right">
28892</p>

   </td>
   <td><p style="text-align: right">
1</p>

   </td>
   <td><p style="text-align: right">
28892</p>

   </td>
  </tr>
  <tr>
   <td>Switzerland
   </td>
   <td><p style="text-align: right">
21220</p>

   </td>
   <td><p style="text-align: right">
2</p>

   </td>
   <td><p style="text-align: right">
10610</p>

   </td>
  </tr>
  <tr>
   <td>Netherlands
   </td>
   <td><p style="text-align: right">
14722</p>

   </td>
   <td><p style="text-align: right">
3</p>

   </td>
   <td><p style="text-align: right">
4907</p>

   </td>
  </tr>
  <tr>
   <td>Pakistan
   </td>
   <td><p style="text-align: right">
13601</p>

   </td>
   <td><p style="text-align: right">
1</p>

   </td>
   <td><p style="text-align: right">
13601</p>

   </td>
  </tr>
  <tr>
   <td>South Korea
   </td>
   <td><p style="text-align: right">
11069</p>

   </td>
   <td><p style="text-align: right">
3</p>

   </td>
   <td><p style="text-align: right">
3690</p>

   </td>
  </tr>
  <tr>
   <td>Czechia
   </td>
   <td><p style="text-align: right">
6508</p>

   </td>
   <td><p style="text-align: right">
1</p>

   </td>
   <td><p style="text-align: right">
6508</p>

   </td>
  </tr>
  <tr>
   <td>Moldova
   </td>
   <td><p style="text-align: right">
5389</p>

   </td>
   <td><p style="text-align: right">
1</p>

   </td>
   <td><p style="text-align: right">
5389</p>

   </td>
  </tr>
  <tr>
   <td>Ireland
   </td>
   <td><p style="text-align: right">
3785</p>

   </td>
   <td><p style="text-align: right">
1</p>

   </td>
   <td><p style="text-align: right">
3785</p>

   </td>
  </tr>
  <tr>
   <td>India
   </td>
   <td><p style="text-align: right">
3004</p>

   </td>
   <td><p style="text-align: right">
1</p>

   </td>
   <td><p style="text-align: right">
3004</p>

   </td>
  </tr>
  <tr>
   <td>Israel
   </td>
   <td><p style="text-align: right">
2819</p>

   </td>
   <td><p style="text-align: right">
1</p>

   </td>
   <td><p style="text-align: right">
2819</p>

   </td>
  </tr>
  <tr>
   <td>Poland
   </td>
   <td><p style="text-align: right">
2810</p>

   </td>
   <td><p style="text-align: right">
1</p>

   </td>
   <td><p style="text-align: right">
2810</p>

   </td>
  </tr>
  <tr>
   <td>Hong Kong
   </td>
   <td><p style="text-align: right">
2791</p>

   </td>
   <td><p style="text-align: right">
1</p>

   </td>
   <td><p style="text-align: right">
2791</p>

   </td>
  </tr>
  <tr>
   <td>Hungary
   </td>
   <td><p style="text-align: right">
2687</p>

   </td>
   <td><p style="text-align: right">
1</p>

   </td>
   <td><p style="text-align: right">
2687</p>

   </td>
  </tr>
  <tr>
   <td>Thailand
   </td>
   <td><p style="text-align: right">
2651</p>

   </td>
   <td><p style="text-align: right">
1</p>

   </td>
   <td><p style="text-align: right">
2651</p>

   </td>
  </tr>
  <tr>
   <td>Portugal
   </td>
   <td><p style="text-align: right">
2589</p>

   </td>
   <td><p style="text-align: right">
1</p>

   </td>
   <td><p style="text-align: right">
2589</p>

   </td>
  </tr>
  <tr>
   <td>China
   </td>
   <td><p style="text-align: right">
1523</p>

   </td>
   <td><p style="text-align: right">
1</p>

   </td>
   <td><p style="text-align: right">
1523</p>

   </td>
  </tr>
</table>


 


### **Experiment 2- Analyzing the Spread of Peer Nodes in the U.S. Based on Energy Prices [EASY]**



<p id="gdcalert4" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image4.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert5">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image4.png "image_tooltip")


**Figure 4. US States Energy Cost Plot on Discovered Nodes \
**

In this experiment, we used the extracted IP addresses of all the peer nodes discovered by our discovery node, and used the ipapi.co API to get the U.S states where we detected peers. Our second phase involved scraping the data from the Energy Information Administration’s website to fetch the energy rates (https://www.eia.gov/) for every state in the United States. Now that we had the nodes segregated by state and energy rates for each US state, we used the US Atlas CDN (https://rb.gy/h0hvr) to plot this on a map represented in Figure x. We observed that our node was more likely to connect to peers in states where the energy prices are lower (like Virginia and Texas), as compared to states where the energy prices are higher (like California and Massachusetts). As depicted in Figure x, we used a color scale from green to red where green indicates a lower energy pricing whereas red indicates a higher price. 


### **Experiment 3- Extracting the Rate of Discovery of New Nodes [MEDIUM]**

For this experiment, we decided to run our node discovery process for 5 minutes to check the rate of new nodes discovered in this duration. We decided to run this experiment for 5 minutes because we were bombarded with recurring HTTP timeout requests whenever we ran the node discovery process for more than 5 minutes. This was occuring due to the hardware restrictions imposed upon us by our EC2 instance. Running this node discovery for 5 minutes resulted in clean data collected by us without any HTTP timeout errors.  Figure x. Represents the number of nodes discovered  over the duration of our experiment while Figure y denotes the rate of new nodes sampled over the time (seconds, as specified in the X axis). Apart from a significant spike at the 150 second mark, we noticed a fairly consistent rate of discovery of these new nodes from our custom client nodes. This is an interesting plot because we observed that although the node connected to peers all across world, the rate of node discovery remained consistent, thus implying how this rate is agnostic of the Euclidean distance of our peer nodes.



<p id="gdcalert5" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image5.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert6">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image5.png "image_tooltip")


**Figure 5. Number of Nodes Discovered vs Time**



<p id="gdcalert6" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image6.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert7">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image6.png "image_tooltip")


**Figure 6. Rate of Discovered Nodes vs Time**


# **Developing a GUI for Private Ethereum Network**



<p id="gdcalert7" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image7.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert8">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image7.png "image_tooltip")


				**Fig 7. GUI for Private Ethereum Network**

We acknowledge that Ethereum exhibits certain attributes that can be transferred to private networks where confidentiality, though important, does not require the same level of emphasis as in the public network. While we worked with setting up the Private Ethereum network on the EC2 instance, we realized how cumbersome it can get to deal with commands on the Geth ethereum client for creating nodes, adding neighbors and doing transactions. Hence we decided to design a dynamic front-end for adding a neighbor to each node locally, which is then seamlessly transmitted to the EC2 instance thus reducing the friction. As the size of the network grew, we appreciated how intuitive it was to visualize the network using the GUI. Here is a link to a demo video showcasing the working of the private ethereum network- https://rb.gy/vkfbp.

For future work, we plan on integrating transactions into the GUI. We currently have a script that automates transactions within nodes and the next task is to integrate it with the GUI.


# **Challenges and Lessons Learnt**


### **Working With Ethereum Light Mode**

To introduce a new node in the Ethereum network, we opted for the light mode nodes because of hardware constraints imposed by the full Ethereum network on our devices. Furthermore, syncing the entire network on our devices would have taken weeks to sync the entire network. Using the light mode presented its own set of challenges because of two primary reasons- a Go Ethereum node running on light mode can only connect to other nodes which are running on the same Goeth version as our node, and; a merge in the Ethereum network which changed the consensus mechanism from Proof-of-Work to Proof-of-Stake required enforced nodes to follow the same consensus mechanism to form a network with each other. Furthermore, light mode is a severely underdeveloped feature by goeth. Thus, not only did this significantly reduce the pool of nodes that we could connect to, but it also made debugging harder for us to understand and debug any issues with light mode in the ethereum network. Furthermore, shoddy documentation on the light mode also proved to be a challenge for us to navigate our way through setting up experiments for our project.


### **Learning Curve With Ethereum and React \
**

As a group of students who delved into the world of Ethereum and P2P networking, we initially struggled to grasp the nuances of this rapidly evolving technology. Despite the abundance of information available on the web, the lack of comprehensive documentation made it difficult for us to understand the inner workings of Ethereum. We as a group found that keeping up with the latest updates and versions of Ethereum was also a challenge. However, setting up our benchmarks  and experiments, while debugging these issues with the ethereum network allowed us to learn the intricacies of P2P networking, which we now view as an invaluable skill set in the ever-changing landscape of computer science.

Additionally, since we planned on extracting insightful visualizations from the network for our project, we also had to learn React. We struggled to grasp its fundamental concepts such as state management, component lifecycle, and most importantly, the JSX followed by React. Furthermore, we faced issues with version compatibility since React is constantly evolving and upgrading to newer versions often results in breaking changes. We are glad to have overcome these challenges in our project.


### **Insufficient Hardware Resources**

Participating in the ethereum network initially required us to sync the entire network, which could take up months to sync and would have taken up roughly 2-3 TB of our disk space. Since none of us had this computer available locally, we considered using cloud computing resources from AWS for our project. We also overcame this challenge by running the light mode of ethereum to introduce our custom node into the network.  


# **Future Work**

**Scaling Up the Node Discovery Process**

At the moment, we currently have the infrastructure setup for discovering nodes with a single-hop. This corresponds to discovering and communicating only with the immediate neighbor. 

As future work we would like to conduct experiments with a two-hop setup, where we ideally want to build infrastructure to use the routing table information from peers to further extract their peer information. This in the future could open up possibilities of iteratively looking for peers, thus retrieving the entire graphical structure of the private ethereum network.

**Expanding to other P2P Networks**

This project was aimed at primarily extracting a variety of metrics from the Ethereum network. We gathered many useful insights ranging from analyzing the spread of peer nodes in the U.S. based on energy prices to analyzing the geographical spread of discovered nodes.

We believe that such metrics would be beneficial for other P2P networks such as Bitcoin, BitTorrent etc.


# **Conclusion**

Our project aimed to explore the Ethereum network and its underlying P2P network topology. Through our experiments and data analysis, we were able to gain insights into the network and how nodes interact with each other. We used various techniques to extract and analyze data, including geolocation, XOR distance, physical distance, and energy rates.

One of the key takeaways from our project is the importance of network topology and geographic location in the node discovery process. Our experiments showed how nodes are more likely to connect with peers that are geographically closer to them, and how the Kademlia protocol considers distance metrics based on XOR and physical distance.

We also learned about the challenges of working with Ethereum and P2P networks, including the learning curve associated with the technology, the limitations of hardware resources, and the need for efficient data extraction and analysis.

There is still much to be explored in the Ethereum network and P2P networks in general. As future work, we plan to scale up our node discovery process and further analyze the routing table information from peers to extract their peer information. We hope that our project will inspire others to delve into the world of P2P networking and contribute to the development of this technology.


# **References**

[1] Miller, Andrew, James Litton, Andrew Pachulski, Neal Gupta, Dave Levin, Neil Spring, and Bobby Bhattacharjee. "Discovering bitcoin’s public topology and influential nodes." et al (2015).

[2] Kim, Seoung Kyun, Zane Ma, Siddharth Murali, Joshua Mason, Andrew Miller, and Michael Bailey. "Measuring ethereum network peers." In Proceedings of the Internet Measurement Conference 2018, pp. 91-104. 2018.

[3] Bailey, Michael, David Dittrich, Erin Kenneally, and Doug Maughan. "The menlo report." IEEE Security & Privacy 10, no. 2 (2012): 71-75.

[4] Nakamoto, Satoshi. "Bitcoin: A peer-to-peer electronic cash system." Decentralized business review (2008): 21260.

[5] Buterin,Vitalik."Ethereumwhitepaper."GitHubrepository1(2013):22-23.

[6] Gao, Yue, Jinqiao Shi, Xuebin Wang, Qingfeng Tan, Can Zhao, and Zelin Yin. "Topology measurement and analysis on ethereum p2p network." In 2019 IEEE Symposium on Computers and Communications (ISCC), pp. 1-7. IEEE, 2019.

[7] Maeng, Soohoon, Meryam Essaid, Changhyun Lee, Sejin Park, and Hongteak Ju. "Visualization of Ethereum P2P network topology and peer properties." International Journal of Network Management 31, no. 6 (2021): e2175.

[8] Kiffer, Lucianna, Asad Salman, Dave Levin, Alan Mislove, and Cristina Nita-Rotaru. "Under the hood of the ethereum gossip protocol." In Financial Cryptography and Data Security: 25th International Conference, FC 2021, Virtual Event, March 1–5, 2021, Revised Selected Papers, Part II 25, pp. 437-456. Springer Berlin Heidelberg, 2021.

[9] Wang, Ke. "Ethereum Blockchain Visualization with Semantics." (2018).

[10] Wang, Taotao, Chonghe Zhao, Qing Yang, Shengli Zhang, and Soung Chang Liew. "Ethna: Analyzing the underlying peer-to-peer network of ethereum blockchain." IEEE Transactions on Network Science and Engineering 8, no. 3 (2021): 2131-2146.

[11] Maeng, Soohoon, Meryam Essaid, Changhyun Lee, Sejin Park, and Hongteak Ju. "Visualization of Ethereum P2P network topology and peer properties." International Journal of Network Management 31, no. 6 (2021): e2175.
