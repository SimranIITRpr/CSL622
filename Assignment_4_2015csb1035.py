####################################################################
# NAME 			- SOUMYADEEP ROY
# ENTRY NO 		- 2015CSB1035
# DATASET USED 	- Inbuilt Zachary Karate Network 
####################################################################
import networkx as nx
import string
import matplotlib.pyplot as plt
import operator
import numpy

############ FUNCTIONS REQUIRED BY CODE

def Betweeness( edge_node_1, edge_node_2 , shortest_paths, edges_list, betweeness_values):
	## VARIABLES
	score = 0
	no_srt_paths = len(shortest_paths)

	## CALCULATING BETWEENESS
	for i in shortest_paths:
		for j in range(len(list(i))-1):
			if ( edge_node_1 == i[j] and edge_node_2 == i[j+1] ):
				score +=1

	betweeness_values[(edge_node_1,edge_node_2)] = score
	return betweeness_values



############ MAIN BODY OF CODE

## VARIABLES ( variables that are required )
no_nodes = 0				# Stores the no of nodes in graph
no_edges = 0				# Stores the no of edges in graph
nodes_list = []				# Contains all the nodes ( no that represents the nodes )
edges_list = []				# Contains all the edges ( pair of nodes representing a edge )
edge = ()					# Stores the information of an edge
count = 0					# Keeps track of shortest paths
components = 2				#Set The Number of Components
shortest_paths = []			# Stores information of all shortest paths from one node to another 
betweeness_values = dict()	# Stores betweeness values for all edges

## CREATING DIGRAPH ( Creating graph from inbuilt zachary karate network function )
G = nx.karate_club_graph()

# ( Also creatig a copy of the network graph for further analysis )
H = G.copy()

# ( Assigning of values related to digraph )
nodes_list = G.nodes()
edges_list = G.edges()
betweeness_values=dict( ( i, 0.0) for i in edges_list)



for i in range(0,no_edges,1):
	count = 0
	edge = edges_list[i]

	for j in range(0,no_nodes-1,1):
		for k in range(j+1,no_nodes,1):
			node_1 = nodes_list[j]
			node_2 = nodes_list[k]

			shortest_paths = nx.all_shortest_paths(G, node_1, node_2)
			betweeness_values = Betweeness( edge[0], edge[1], list(shortest_paths), edges_list, betweeness_values)	
			count = count + len(shortest_paths)
	betweeness_values[edge] = float(betweeness_values[edge])/count

sorted_paths = list(sorted(betweeness_values.items(), key=operator.itemgetter(1),reverse=True))


for each in sorted_paths:
	edge = each[0]
	node_1 = edge[0]
	node_2 = edge[1]

	H.remove_edge( node_1, node_2)
	if ( components == nx.number_connected_components(H) ):
		plt.figure("COMPONENTS IN GRAPH")
		nx.draw(H,with_labels = True)
		plt.show()
		break

