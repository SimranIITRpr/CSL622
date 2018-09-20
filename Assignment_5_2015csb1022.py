
'''
     Author: Pankaj Verma
     Date : 20 September 2018
    
     Required python packages: networkx

     Required input file : "subj.txt"
  
'''


import networkx as nx
import matplotlib.pyplot as plt

def overall_best_path(G, labels, start, end):
	path = [start]
	while True:
		child = list(G.neighbors(start))   # list of all neighbors of start vertex
		if end in child:               # if end vertex is not child of start vertex 
			path.append(end)            # then add in path list
			break
		for v in path:                   #if end vertex is not child of start vertex  
			if v in child:               
				child.remove(v)           # then remove start from path list
		weight = []                      
		for i in child:                  # look for every child of start vertex
			count = 0
			for p, q in zip(labels[start], labels[i]):
				if p == '1' and q is '1':
					count+=1              # increment count 
			weight.append(count)          # add count in weight list	
		best = child[ weight.index(max(weight)) ]   # find max weight of path
		path.append(best)
		start = best
	return path




# read file from input file "subj.txt"

with open("subj.txt") as infile:
	labels = [point.strip() for point in infile.readlines()]
	labels = {int(point.split()[0]):point.split()[1:] for point in labels} # store all input as an dictionary of every node with corresponding labels
	nodes = labels.keys()  # list of exist node

x = len(labels)

G = nx.Graph()  # creating a graph
G.add_nodes_from(nodes) # add nodes in graph
for i in range(1,x):
	for j in range(i+1, x+1):
		for(label_i,label_j) in zip(labels[i],labels[j]):
			if label_i == '1' and label_j == '1':            
				if not G.has_edge(i,j):
					G.add_edge(i,j, weight=1)              
				else:
					weight = G [i][j]['weight']
					G.remove_edge(i,j)
					G.add_edge(i,j,weight = 1/(weight + 1)) 


print("%s    %s" % ("Start ->  End", "Overall Best Path")) 
for i in G.nodes():
	for j in G.nodes():
		if(i!=j):
			print("%s    %s" % (str(i)+"     ->   "+str(j), str(overall_best_path(G, labels, i, j) )))  