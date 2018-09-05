'''

Comparision of Random walk with teleportation
with Google's page rank algorithm

- Implemented Random walk with teleporation
- Used inbuilt page rank function from networkx
- Plotted ranks of nodes obtained from both the methods

'''

import networkx as nx
import matplotlib.pyplot as plt
import random as rand

'''
Setting up the probabilities, 
number of iterations, input graph
'''

# probability
p = 0.5

# number of iterations in random walk
itr = 10**6

# teleportation probability
t = 0.2

# Web google graph from snap data set
input_graph_file = 'web-Google.txt'

# Reading Graph
G = nx.read_edgelist(input_graph_file,create_using=nx.DiGraph(), nodetype = int)

# Storing all the nodes in a list
V = list(G.nodes())

# number of nodes
n = len(V)

# Dictionary to store number of times a node is visited
Count = {}

# Initializing count with zero
for i in V:
	Count[i] = 0

# Randomly picking starting node for random walk
current = rand.choice(V)

# Making count of start node 1
Count[current] = 1

for i in range(itr):
	# x to simulate teleportation probability
	x = rand.random()
	if x < t:
		# i.e. teleporte
		current	= rand.choice(V)
	else:
		# don't teleporte
		N = list(G.neighbors(current))
		if len(N) == 0:
			# If no neighbor then teleporte
			current = rand.choice(V)
		else:
			# pick a random neighbor
			current	= rand.choice(N)
	# After updating current node,
	# lets update the count of current node	
	Count[current] += 1

'''
X is a list of type (node_count,node)
Above format will amke it easy to sort
according to count and rank them :-)
'''
X = []
for i in Count:
	X.append((Count[i],i))

# Y is similar to X but for page rank!
Y = []
Z = nx.pagerank(G, alpha=t)
for i in Z:
	Y.append((Z[i],i))

# Sorting to ease the ranking
X = sorted(X)
Y = sorted(Y)

# Printing for vizualization
# Below for loop cn be commented to avoid printing
print("(Count,Node) \t (Page Rank Value, Node)")
for i in range(n):
	print(X[i],Y[i])

'''
RR will store rank of each node
i.e. RR[node_1] will give rank of node_1
RR is for random walk
PR is similarly for page rank
'''
RR = {}
PR = {}
for i in range(len(X)):
	RR[X[i][1]] = i
	PR[X[i][1]] = i

# For plotting
Rank_random_walk = []
Rank_page_rank = []

for i in V:
	Rank_random_walk.append(RR[i])
	Rank_page_rank.append(PR[i])

plt.plot(Rank_random_walk,Rank_page_rank,'ro')
plt.title("Comparing ranking method")
plt.xlabel("Rank from random walk")
plt.ylabel("Rank from pagerank")
plt.show()
