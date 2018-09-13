import random as rand
import matplotlib.pyplot as plt
import networkx as nx

# Storing the zachary file so that it can be excessed afterwards.
graph_file = "ucidata-zachary.txt"
# We are reading the edge list from given graph.
G = nx.read_edgelist(graph_file, nodetype = int)	
# We store number of nodes in n.
n = G.number_of_nodes()
# We store list of all nodes in V.
V = list(G.nodes())
# We store all the edges in E.
E =  G.edges()
# We will store the index of all element of shortest path
# in count library. 
Count = {}
# While loop is used so that when the graph is disconnected the loop
# will break.
while(nx.is_connected(G)):
	# We assign count library to be zero so that further count can
	# be added by count[] += 1
	for i in E:
		Count[(min(i[0],i[1]),max(i[0],i[1]))] = 0
	# This loop takes all the possible combination of (i,j) from all nodes.
	print(Count)
	for i in range(n):
		for j in range(i+1,n):
			X = nx.shortest_path(G,source=V[i],target=V[j])
			for k in range(len(X)-1):
				# Since in directed graph (i,j) and (j,i) are same but
				# we take smaller index first thats why p is the smaller one.
				p = min(X[k],X[k+1])
				q = max(X[k],X[k+1])
				# count is increased of index (p,q) to check betweeness.
				Count[(p,q)] += 1
	# Z is a library which will store betweeness of all edges.
	Z = []
	for i,j in Count.items():
		Z.append((j,i))

# We will sort Z so that we can remove highest betweeness edge
# and check whether the graph becomes disconnected or not.
	Z = sorted(Z)	

	x = Z.pop()
	# We will remove the edge with highest betweeness from the graph.
	if (x[1][0],x[1][1]) in E:
		G.remove_edge(x[1][0],x[1][1])
	else:
		G.remove_edge(x[1][1],x[1][0])

# Once we are out of the loop then we surely made the graph disconnected.
# Now we will draw the graph to validate our algorithm.
nx.draw(G, cmap = plt.get_cmap('jet'),with_labels = True)
plt.title("Seprating connected graph into 2 communities")
plt.show()