'''	Ganesh Prasad - 2018csm1008
	Rakesh meena - 2018csm1017
	Jeevan Kumar - 2018csm1012

Problem: Given a network of friendships, we have to determine the pagerank of the network.
Solution: Algorithm used:
	Random walk(discussed for assignment 3) where from a node a random node is selected from its neighbors and
this is done for a large number of walks.
A counter is maintained stating how many a times a node has been walked through, if it has a lot of incoming nodes counter value for that node
will be higher'''


import networkx as nx
import matplotlib.pyplot as plt
import random

G = nx.read_edgelist(r"pagerank.txt",create_using=nx.DiGraph(), nodetype = int)
nodess = G.nodes()

# counter that keeps record of how many times a node has been visited
count = {el:0 for el in G.nodes()}

# randomly selects a node from the nodes list
rand_node = random.choice(list(nodess))

#gets all the neighbours of the random node
successors = [successor for successor in G.successors(rand_node)]

# random walk is performed for a huge number
for times in range(100000):
	if len(successors) != 0:
		rand_node = random.choice(successors)
		count[rand_node] = count[rand_node] +1
	else:
		rand_node = random.choice(list(nodess))
		count[rand_node] = count[rand_node] +1
	successors =[successor for successor in G.successors(rand_node)]

print count

nx.draw(G,with_labels = True)
plt.show()
