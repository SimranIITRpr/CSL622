from __future__ import print_function
import networkx as nx
import matplotlib.pyplot as plt

#Number of communities
N = 5
G = nx.karate_club_graph()
Edges = {}

plt.figure("Original Graph")
nx.draw(G)

for i in G.edges():
	Edges[i] = 0

#Function to compute number of shortest paths passing through given edge
def betweeness(paths, u, v):
	count = 0
	for i in paths:
		for j in range(len(list(i))-1):
			if u==i[j] and v==i[j+1]:
				count +=1
	for i in G.edges():
		if (u == i[0] and v == i[1]) or (u == i[1] and v == i[0]): 
			Edges[i] += count
	return len(paths)		

#Main function
for i in G.edges():
	count = 0
	for u in G.nodes():
		for v in G.nodes():
			if u != v:
				P = nx.all_shortest_paths(G, u, v)		
				count += betweeness(list(P), i[0], i[1])
	Edges[i] = float(Edges[i])/count
	
plt.figure("Communities")

print("Betweeness                  Removed Edges")
for i in reversed(sorted((v,k) for (k,v) in Edges.items())):
	print (str(i[0])+"		"+str(i[1]))
	G.remove_edge(i[1][0], i[1][1])	
	if nx.number_connected_components(G) == N:
		break

nx.draw(G)
plt.show()
		
