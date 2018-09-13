import networkx as nx
import matplotlib.pyplot as plt
import random as rand

count = {}
#deciding which edge to remove on the basis of betweeness centrality
def edge_to_remove(G, V, E):
	n = G.number_of_nodes()
	
	for i in E:
		count[i] = 0

	for i in range(len(V)):
		for j in range(i+1,len(V)):
			A = nx.shortest_path(G,source=V[i],target=V[j])
			for k in range(len(A)-1):
				p,q = min(A[k],A[k+1]),max(A[k],A[k+1])
				count[(p,q)] += 1
	a = n*(n-1)/2
	for i in E:
		count[i] = (count[i]*1.0)/a
	A = []
	for i,j in count.iteritems():
		A.append((j,i))

	A = sorted(A)	

	x = A.pop()
	return x

#Girvan-Newman Algorithm
def girvan(G, V, E):
	# c contains the various connected components in our graph
	c = nx.connected_component_subgraphs(G)
	l = len(c)
	# c is the no. of connected components in G
	while (l==1):
		x = edge_to_remove(G, V, E)
		G.remove_edge(x[1][0],x[1][1])
		c = nx.connected_component_subgraphs(G)
		l = len(c)
	return c



#Loading the 'Zachary Karate' network
G=nx.karate_club_graph()


V = list(G.nodes())
E = G.edges()

c = girvan(G, V, E)

#Prints the nodes of the two different communities in the network
for i in c:
	print (i.nodes())
	print ('____________________')
