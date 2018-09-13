import operator 
import networkx as nx
import matplotlib.pyplot as plt

g=nx.Graph()
g=nx.karate_club_graph()  # loading karate club

def edge_betweeness(g):
	
	# initializing a matrix for storing counts of edges between the nodes x and y
	matrix = []
	
	for i in xrange(len(g.nodes)):
		matrix.append[]
		for k in xrange(len(g.nodes()):
			matrix[i].append(0.0)
	
	# Randomly choosing nodes for calculating betweeness of edges for the shortest paths between i and j
	for i in g.nodes():
		for j in g.nodes():
			if(i==j):
				continue
			
			# list of pathways between node i and j
			shortest_paths = list(nx.all_shortest_paths(g,i,j))

			# total number of shortest pathways between i and j for the calculation of edge betweeness
			l = len(shortest_paths)
			
			# Increament in the count of the edge once found in the shortest pathway list with a dividing factor of total number of 
			# shortest pathway to get the betweeness value 		
			for m in range(len(shortest_paths)):
				for n in range(len(shortest_paths[m])-1):
					matrix[shortest_paths[m][n]][shortest_paths[m][n+1]] += (1.0/(float)(l))

	return matrix


while(nx.is_connected(g)):
	# Returned matrix from the function edge betweeness
	matrix = edge_betweeness(g)
	x=0
	y=0
	# Initial value of max_betweness to get the maximum betweeness edge after comparision through the below loop
	max_betweeness = matrix[x][y]
	
	for i in range(g.nodes()):
		for j in range(g.nodes()):
			if(max_betweeness < matrix[i][j]):
				x = i
				y = j
				max_betweeness = matrix[i][j] # Iterative loop for getting the bridge edge
	
	g.remove_edge(x,y) # Removing that edge in order to disconnect the graph into two communities

nx.graph(g, with_label=1)
plt.show() # plot to visualize the formed community in the graph

