'''	Ganesh Prasad - 2018csm1008
	Rakesh meena - 2018csm1017
	Jeevan Kumar - 2018csm1012

Problem: Given a network of friendships, we have to find the nodes(persons) with most and least friendly neighbourhood.
Solution: We take a node and find its adjacent nodes(a list say j) which are also impressed by the node.
	Now for every node in j we get a total number of mutually impressed friends, which after dividing by len(j)
	we arrived at an average treated as a factor to decide whose neighbourhood is friendly or not.'''


import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_edgelist(r"pagerank.txt",create_using=nx.DiGraph(), nodetype = int)

nx.draw(G,with_labels = True)
plt.show()


# Find total Number of mutually impressed friends of a node
def num_of_mutually_impressed_nodes(G,node):
	list_successors = G.successors(node)
	total_num = 0
	for successor_node in list_successors:
		if (G.has_edge(successor_node,node)):
			total_num = total_num+1;
	return total_num

# Returns a list of mutually impressed friends for a node
def mutually_impressed_nodes(G,node):
	list_successors = G.successors(node)
	node_list = []
	for successor_node in list_successors:
		if(G.has_edge(successor_node,node)):
			node_list.append(successor_node)
	return node_list


#Calculates the factor for measurement
def friendly_neighbourhood(G):
	final_data = {}
	nodes = G.nodes()
	for each in nodes:
		total_index = 0
		for successor_node in mutually_impressed_nodes(G,each):
			total_index = total_index + num_of_mutually_impressed_nodes(G,successor_node)
		final_data[each]=total_index/float(len(mutually_impressed_nodes(G,each)))
	return final_data


#prints the node which has most and the least friendly neighbourhood
def print_most_and_least_friendly_neighbourhood(neighbourhood_index):
	nodes = neighbourhood_index.keys()
	indices = neighbourhood_index.values()
	most_friendly = nodes[indices.index(max(indices))]
	least_friendly = nodes[indices.index(min(indices))]
	print most_friendly,"has the most friendly neighbourhood"
	print least_friendly,"has the least friendly neighbourhood"


f = friendly_neighbourhood(G)
print("The mapping:")
print f
print_most_and_least_friendly_neighbourhood(f)
	
