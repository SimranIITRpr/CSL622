import networkx as nx
import matplotlib.pyplot as plt
import random as rand

# Reading the network
input_graph_file = "ucidata-zachary.txt"

# Read graph from text file directly
G = nx.read_edgelist(input_graph_file, nodetype = int)
	
# finding number of nodes in our graph
n = G.number_of_nodes()

# Storing all the nodes in a list
V = list(G.nodes())

# storing all the dges
E =  G.edges()

# To count total number of shortest paths
# passing through each edge
Count = {}

while(nx.is_connected(G)):
	# Calculating betweeness centrality
	for i in E:
		Count[i] = 0

	for i in range(len(V)):
		for j in range(i+1,len(V)):
			X = nx.shortest_path(G,source=V[i],target=V[j])
			for k in range(len(X)-1):
				p,q = min(X[k],X[k+1]),max(X[k],X[k+1])
				Count[(p,q)] += 1
	# Dividing by number of shotest paths	
	c = n*(n-1)/2
	for i in E:
		Count[i] = (Count[i]*1.0)/c

	# TO sort all the edges according to betweenes centrality
	P = []
	for i,j in Count.iteritems():
		P.append((j,i))

	P = sorted(P)	

	x = P.pop()
	print(x)
	G.remove_edge(x[1][0],x[1][1])

nx.draw(G, cmap = plt.get_cmap('jet'),with_labels = True)
plt.title("Two communities detection in Zachary Karate network")
plt.show()
