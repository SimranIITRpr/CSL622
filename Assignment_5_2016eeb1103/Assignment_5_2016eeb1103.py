""" Name : Utkarsh Katiyar
    Entry No. : 2016EEB1103 """

import networkx as nx				                          #importing the packages.
import matplotlib.pyplot as plt
import random

G = nx.Graph()						                            #initialising the graph.

file = open("subj.txt","r")			                      #opening the provided data file
m = []
for line in file:					                            #reading every line of the file.
	flag = 0
	S_list = []
	for num in line.split(" "):		                      #getting the data.
		node = int(num)		
		if flag == 0:
			flag = 1
			G.add_node(node)
		else:
			S_list.append(node)	
	count = 0
	vertex1 = 0
	for lists in m:					                            #adding edges as per given data and rules
		count = 0
		vertex1+=1
		for i in range(len(S_list)):
			if S_list[i] ==1 and lists[i]==1:
				count+=1
		if(count == 0):
			continue
		else:
			G.add_edge(vertex1,len(m)+1,weight = count)     #assigning weights as per common subjects taken
	m.append(S_list)

def Path(G,i,j):								                      #function to find best paths
	paths = nx.all_shortest_paths(G,i,j)		            #finding all shortest paths	using inbuilt functions
	count2 = 0
	listL = []
	for p in paths:	                                    #checking best paths as per the weights of edges connecting them
		count2+=1
		listL = p
	if(count2==1):
		for k in listL:
			print str(k) + " ",
		return
	else:
		res = []
		mWeight = -1
		index1 = 0
		index2 = 0
		paths = nx.all_shortest_paths(G,i,j)	#	
		for l in paths:
			NodeW = G[l[0]][l[1]]['weight'] 
			if NodeW>mWeight:
				index1 = l[0]
				index2 = l[1]
				mWeight = NodeW
		print str(index1) + " ",
		Path(G,index2,j)

for i in G.nodes():  # printing paths 
	for j in G.nodes():
		if i == j:
			continue
		else:
			paths = nx.all_shortest_paths(G,i,j)
			count2 = 0
			listL = []
			for p in paths:
				count2+=1
				listL = p
			if(count2==1):                                     #printing with formatting
				print "Source:" + str(i)+" dest:"+str(j) + "   Path : [", 
				for k in listL:
					print str(k) + " ",
				print "]"
			else:
				print "Source:" + str(i)+ " dest:" +str(j) + "   Path : [",
				Path(G,i,j)
				print "]"
