########################################## Author::Shreyans SOni ###############################
##########################################   Date::  9/7/2018     ###############################
########################################## About::Script to Compare Teleportation and pagerank ###############################

'''
This Python Scripts is a Implementation of the Edge Betweenness Centrality algorithm.
For a betweenness value of edge we Find number of All possible shortest path(s) passing through that "edge" than divide that with total shortest paths.

	Betweenness of edge e =	sigma(u,v){containg e}/sigma(u,v)

The data-set which I have taken is Zachary Karate Network graph which is already presented in the networkx library
>> G=nx.karate_club_graph()

Details of Graph as Follows:
Name: Zachary's Karate Club
Type: Graph
Number of nodes: 34
Number of edges: 78
Average degree:   4.5882

OUTPUT: Output is The Graph Components after removing edges by ranking the Betweenness value of edges calculated. 

Usage:
NOTE:First set that how many components do you want to have by setting variable in line 34 as "no_of_comp=<whatever you want>"
>> python Assignment_4_2016csb1146.py
'''
#Importing essentials libraries
import networkx as nx
import matplotlib.pyplot as plt
import operator
import numpy


no_of_comp=2							#Set The Number of Components

#Choosing Graph
#G=nx.barbell_graph(5,0)
G = nx.karate_club_graph()
nodes=G.nodes()
edges=G.edges()


all_p_p=dict((el,0.0) for el in edges)				#hold Betweenness value for all the visited edges
################################### Function for Betweenness #######################################
def bt_ness(u,v,paths):
	'''This function takes edge (u,v) and all poosible paths between them and returns the betweenness value of that edge (u,v)'''
	var = 0							#variable to store count
	for i in paths:						#iterating each path than checking if u and v are both end point
		for j in range(len(list(i))-1):
			if u==i[j] and v==i[j+1]:
				var +=1
	for i in edges:						#iterating each edge and checking if (u,v) is an edge or not 
		if (u == i[0] and v == i[1]) or (u == i[1] and v == i[0]): 
			all_p_p[i] += var			#updating the betweenness dictionary as sigma(u,v){e}
	return len(paths)					#returnig length of path

################################################################################
for i in edges:							#For each edge calculating bt_ness and updating the Betweenness dict
	count = 0						# as sigma(u,v){e}/sigma(u,v)
	for u in G.nodes():
		for v in G.nodes():
			if u != v:
				all_p = nx.all_shortest_paths(G, u, v)		
				count += bt_ness(i[0],i[1],list(all_p))
	all_p_p[i] = float(all_p_p[i])/count
sorted_paths=list(sorted(all_p_p.items(), key=operator.itemgetter(1),reverse=True))	#sorting the bt_ness dict based on their values 
#print(sorted_paths)
#print(list(sorted(nx.edge_betweenness_centrality(G).items(), key=operator.itemgetter(1),reverse=True)))
#####################################################################################
H=G.copy()							#creating a copy of G so G is not disturbed
for each in sorted_paths:					#iterating through each betweenness value
	edge=each[0]
	u=edge[0]						#extracting nodes of edges
	v=edge[1]
	#print(u,v)
	H.remove_edge(u,v)					#removing edge of higher betweenness value first
	if(not nx.is_connected(H)):				#checking IF graph is still connected 
		subgraphs = list(nx.connected_component_subgraphs(H, copy=False))	#Components of graph
		print 'The Edge which is removed '+"("+str(u)+","+str(v)+")"+" and betweenness is "+str(each[1])
	if(no_of_comp==nx.number_connected_components(H)):	#IF no_of_comp is stisfied than plotting the comp of graph
		plt.figure("Components of graph after Removing edges")
		nx.draw(H,with_labels = True)
		plt.show()
		break
####################################################################################
