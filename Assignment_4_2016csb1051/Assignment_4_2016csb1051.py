import networkx as nx							#importing the packages
import random
import matplotlib.pyplot as plt

g=nx.karate_club_graph()						#making the Zachary karate club graph

def betweenness(g):							#Function to find the betweenness in the graph
	count = 0	
	res = []
	mat = []
	for i in xrange(len(g.nodes())):				#Making the matrix to store the betweenness value.
		mat.append([])
		for j in xrange(len(g.nodes())):
			mat[i].append(0.0)				#Initialising it with 0.
	for i in range(len(g.nodes())):					#Finding the shortest path between every pair of node. 
		path = nx.single_source_shortest_path(g,i)		#Function to get the shortest path.
		for p in range(len(path)): 				
			for k in range(len(path[p])-1):
				mat[path[p][k]][path[p][k+1]]+=1.0
		count = count+len(path)
	for i in range(len(g.nodes())):					#finding the betweenness.
		for j in range(len(g.nodes())):
			mat[i][j] = mat[i][j]/count
	"""for i in range(len(g.nodes())):
		for j in range(i+1,len(g.nodes())):
			list1 = nx.shortest_path(g,source=i,target=j)
			for k in range(len(list1)):
							
			res.append(list1)"""
	return mat							#returning the matrix.

while(nx.is_connected(g)):						#Remove the highest betweenness node while the graph is not disconnected.
	mat = betweenness(g)						#Calling the betweenness function.
	xx =0
	yy = 0
	maxTill = -1.0
	for i in range(len(g.nodes())):					#Finding the edge wijth highest betweenness.
		for j in range(len(g.nodes())):
			if(maxTill < mat[i][j]):			#updating the maximum value.
				xx = i
				yy = j
				maxTill = mat[i][j]
	g.remove_edge(xx,yy)						#Removing the high betweenness edge from the graph.
print "Disconnected graph edges are : "
print (g.edges())							#Printing the edges of the disconnected graph.
nx.draw(g,with_labels = 1)						#Drawing the graph.
plt.show()								#Printing the graph.
