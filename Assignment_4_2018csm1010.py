'''
By - Harsimar Singh
Roll- 2018CSM1010
Editor - Sublime Text
Compiled and Run - Command Prompt (using python)

'''

import networkx as nx
import matplotlib.pyplot as plt
import operator 

def contained_edge_in_path(p,edge):
	count=0
	#p is a 2D list 
	#i has the row vector i.e. the number of shortest paths
	for i in range (len(p) ):

	#j will loop over the ith row of p
		for j in range (len(p[i])-1):

	#path will be like [1 2 3 ...]
	#checking here two consecutive nodes that match our edge points
			if (p[i][j] == edge[0] and p[i][j+1]==edge[1]) or (p[i][j] == edge[1] and p[i][j+1]==edge[0]) : 
	#count the number of matches 			
				count+=1
	return count	

def find_edge_betweenness(G,edge):	
	countedge=0
	countall=0
	nlist=list(G.nodes())
	total=0
	for source in nlist: 
		for dest in range(source+1, len(nlist) ):
			#this loop is the brute force for choosing two nodes out of all nodes				
			
			#p has list of all the shortest paths between a source and destination
			p=list(nx.all_shortest_paths(G,source=source,target=dest))
			
			#countall has the number of all shortest paths
			countall=len(p)

			#a function that will return in how many paths the currest edge exits
			countedge=contained_edge_in_path(p,edge)
			
			#ratio is calculated here 
			ratio=countedge/countall
			
			#the previous value of betweenness is added for summation
			total=ratio+total

	#total value is returned 		
	return total

G = nx.karate_club_graph()
#this while loop will check for the edge betweeness after an edge is removed

while(nx.is_connected(G)):
#loop to calculate edge betweenness of all edges and store it in dictionary
	elist=list(G.edges())
	edgedict={}
	for edges in elist:
		edgedict[edges]=find_edge_betweenness(G,edges)
	#upto now we have calculated edge betweenness
	
	#s is a sorted dictionary of edges
	s=list(sorted(edgedict.items(),key=operator.itemgetter(1)))
	x=s.pop()
	G.remove_edge(x[0][0],x[0][1])

nx.draw(G,with_labels=True)
plt.show()
