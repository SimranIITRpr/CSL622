'''
CSL622 ASSIGNMENT 5
Paras Kumar
201CSB1047
'''

import networkx as nx

Data = {}

#Returns true if there is a common subject
def is_common_subject(a, b):
	for i in range(len(a)):
		if a[i] == b[i] == '1':
			return True
	return False		

#returns the best path
def find_best_path(G, Data, src, dest):
	path = [src]
	while True:
		neighbors = list(G.neighbors(src))
		if dest in neighbors:
			path.append(dest)
			break
		for p in path:
			if p in neighbors:
				neighbors.remove(p)
		weight = []
		for i in neighbors:
			count = 0
			for p, q in zip(Data[src], Data[i]):
				if p == '1' and q is '1':
					count+=1
			weight.append(count)    	
		best = neighbors[ weight.index(max(weight)) ]
		path.append(best)
		src = best
	return path

#Main Function

#loading Data
f = open("subj.txt")
for l in f.readlines():
	tmpData = l.strip()
	Data[int(tmpData.split()[0])] = tmpData.split()[1:]

#Creating graph
nodes = Data.keys()
G = nx.Graph()
G.add_nodes_from(nodes)

for i in range(1, len(Data)):
	for j in range(i+1, len(Data)+1):
		if is_common_subject(Data[i], Data[j]):
			G.add_edge(i, j)

#Printing best paths 
print("%-15s %s" % ("Start ->  End", "Best Path"))  

for i in G.nodes():
	for j in G.nodes():
		if(i!=j):
			print("%-15s %s" % (str(i)+"     ->   "+str(j), str(find_best_path(G, Data, i, j) )))  
			