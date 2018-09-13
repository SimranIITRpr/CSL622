# Nitin Gandhi
# 2016csb1045

import networkx as nx
import matplotlib.pyplot as plt

G = nx.karate_club_graph()

print("Nodes: ", G.number_of_nodes())
print("Edges: ", G.number_of_edges())

"""
def doit():
	dic_val = nx.edge_betweenness_centrality(G)
	dic_val = sorted(dic_val.items(), key=lambda x: x[1], reverse = True)
	return list(dic_val)
"""


def edge_betweenness(n1, n2):
	count = 0
	for i in G.nodes():
		for j in G.nodes():
			if(i != j):
				paths = nx.all_shortest_paths(G, i, j)
				paths = list(paths)
				for path in paths:
					for k in range(len(path)-1):
						if(path[k] == n1 and path[k+1] == n2):
							count += 1
	return count
				


def doit():
	Edge = {}
	for i in G.edges():
		Edge[i] = edge_betweenness(i[0], i[1])
	
	Edge = sorted(Edge.items(), key=lambda x: x[1], reverse = True)
	return list(Edge)

while(nx.is_connected(G)):
	dic_val = doit()
	#print("==============================")
	#print(dic_val[0][0][0], dic_val[0][0][1])
	print("Removing... (",dic_val[0][0][0], "---", dic_val[0][0][1],")")
	#print("==============================")
	#print(dic_val)
	G.remove_edge(dic_val[0][0][0], dic_val[0][0][1])


print("\nShowing Connected Components...\n")
conn = nx.connected_components(G)
for element in conn:
	print(element)
