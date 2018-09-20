import networkx as nx
import random

"""
   Dataset used :- Google Web Graph from Snap
   Link : https://snap.stanford.edu/data/web-Google.html

   Author :- Aditya Deva (2015eeb1044)
"""

def random_walk(input_web_graph)
	# Data Set of google web graph
	G = nx.read_adjlist(input_web_graph)

	# Initializing Dictionary for tracking number of visits of a node 
	visit = {}

	# Initializing count as zero for each node.
	for i in list(G.nodes()):
    		visit[i] = 0

	# Randomly choosing the node from the network
	node = random.choice(list(G.nodes()))  

	itr=10000000

	# Random walk for the given iteration.   
	for i in range(1,itr+1):
    		neighbors = [] 
    		neighbors = list(G.neighbors(node))

    		# Count increment
    		visit[node] = visit[node] + 1

    		# Teleporting the node with a probability of 0.2 or if the visited node is a terminal node
		x= random.random()
    		if len(neighbors) == 0 or x < 0.2:
        		node = random.choice(list(G.nodes()))
        		continue

    		# Probability of going to next node is 0.8 (when the above condition doesn't meet)
    		node = random.choice(neighbors)


	# list of keys of all the counted nodes
	node_list = list(visit.keys())

	# count of all the visited nodes to calculate ranks based on number of visits
	vstslst = [visit[x] for x in node_list] 

	# nodes rank by inbuilt method pagerank().
	pr = nx.pagerank(G)

	# rank value of the inbuilt pagerank
	rankval = [500*pr[x] for x in node_list]

	# plot of calculated rank with the inbuilt one
	plt.plot(ndlst,vstslst,'b--', node_list, rankval , 'r--')

if __name__ == "__main__":
	input_web_graph = "webgraph_dataset_google.txt"
	Random_Walk(input_web_graph)


    
    

