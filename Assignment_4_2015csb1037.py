import operator 
import matplotlib.pyplot as plt
import networkx as nx

# Note: Some of the code has been taken from the video lecture of Social Networks
def edge_to_remove(G):
	dictionary = {}
	for each in G.edges():
		dictionary[each] = 0
	
	for i in range(G.number_of_nodes()):
		for j in range(G.number_of_nodes()):
			if(i>j):
				paths = list(nx.all_shortest_paths(G,i,j)) #finding the total paths between the nodes
				for k in range(len(paths)):
					for p in range(len(paths[k])-1):
						key = (paths[k][p],paths[k][p+1])
						key1 = (paths[k][p+1],paths[k][p])
						if key in dictionary:
							dictionary[paths[k][p],paths[k][p+1]] = dictionary[paths[k][p],paths[k][p+1]] + 1
						else:
							dictionary[paths[k][p+1],paths[k][p]] = dictionary[paths[k][p+1],paths[k][p]] + 1
	
	max = 0
	for each in dictionary.items():
		if(each[1] > max):
			max = each[1]
			key = each[0]
				
	return key
	


def find_Communities(G):
	components = nx.number_connected_components(G)
	while(components == 1):
		G.remove_edge(*edge_to_remove(G))
		components = nx.number_connected_components(G)			
	return nx.connected_component_subgraphs(G)




"""Loading the Karate Network and finding the Communities"""
G = nx.karate_club_graph()
components = find_Communities(G)
nx.draw(G)
plt.show()
for i in components:
	print (i.nodes())
	print ('\n')
	
	

