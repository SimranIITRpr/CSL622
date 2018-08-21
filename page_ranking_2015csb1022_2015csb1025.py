import networkx as nx

'''
	Author: Pankaj Verma & Pratik Chhajer
	Date: 21/08/2018

	This function finds the pagerank value for each node 
	of the network.

	Required python packages: networkx

	input: Input graph text file such that nodes of an edge
	are present separated by a space in one line.

	output: Return back a dictonary containing all the nodes
	and their pagerank value.
'''

def page_rank_algorithm(input_graph_file):

	# Read graph from text file directly
	G = nx.read_edgelist(input_graph_file,create_using=nx.DiGraph(), nodetype = int)
	
	# finding number of nodes in our graph
	n = G.number_of_nodes()

	# List of all the nodes in our graph
	Nodes = G.nodes

	# Dictionary to store pagerank of all the nodes
	# It will be updated after every iteration
	Page_Rank_Value = {}

	# A temporary dictionary to sotre pagerank
	Temp = {}

	# Initial pagerank value divided equally
	t = 1.0/n

	# Assigning equal pagerank value to all nodes
	for i in Nodes:
		Page_Rank_Value[i] = t
		Temp[i] = 0

	# Total number of iterations
	itr_total = 10000

	# index of iteration
	itr = 0

	# Absolute error to keep track of changes in each iteration
	err = 1

	# Iterate till convergence or after 10k iterations
	while(itr < itr_total and err > 1e-7):
		for i in Nodes:
			Neighbors = list(G.neighbors(i))
			p = len(Neighbors)
			for j in Neighbors:
				Temp[j] += (Page_Rank_Value[i]*1.0)/p
			if(p == 0):
				y = (Page_Rank_Value[i]*1.0)/(n-1)
				for x in Nodes:
					if x != i:
						Temp[x] += y
		
		err = 0
		for i in Nodes:
			err += abs(Page_Rank_Value[i] - Temp[i])
			Page_Rank_Value[i] = Temp[i]
			Temp[i] = 0
		itr+=1

	print("In " + str(itr) + " iterations it converges!!")

	for i in Page_Rank_Value:
		print(i,Page_Rank_Value[i])

if __name__ == "__main__":
	input_graph_file = "pagerank.txt"
	page_rank_algorithm(input_graph_file)