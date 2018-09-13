import operator 
import matplotlib.pyplot as plt
import networkx as nx

# Note: Some of the code has been taken from the video lecture
def edge_to_remove(G):
	dictionary = {}
	for each in G.edges():
		dictionary[each] = 0
	
	for i in range(G.number_of_nodes()):
		for j in range(G.number_of_nodes()):
			if(i>j):
				x = list(nx.all_shortest_paths(G,i,j)) #finding the total paths between the nodes
				for k in range(len(x)):
					for p in range(len(x[k])-1):
						key = (x[k][p],x[k][p+1])
						key1 = (x[k][p+1],x[k][p])
						if key in dictionary:
							dictionary[x[k][p],x[k][p+1]] = dictionary[x[k][p],x[k][p+1]] + 1
						else:
							dictionary[x[k][p+1],x[k][p]] = dictionary[x[k][p+1],x[k][p]] + 1
	
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
nx.draw(G)
plt.show()
components = find_Communities(G)
nx.draw(G)
plt.show()
for i in components:
	print (i.nodes())
	print ('\n')
	
	

