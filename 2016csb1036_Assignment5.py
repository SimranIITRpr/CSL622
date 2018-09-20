'''

Chintala Tejaswini
2016csb1036
Assignment5 - Finding best possible paths between two nodes of a graph

'''

import networkx as nx
import matplotlib.pyplot as plt               #importing required libraries

f = open("subj.txt")                              #reading data from the file subj.txt
arr = {}                                   #dictionary storing the input data
for line in f.readlines():
	ln = line.strip()
	arr[int(ln.split()[0])] = ln.split()[1:]

nodeArray = arr.keys()                  #array of nodes
G = nx.Graph()
G.add_nodes_from(nodeArray)

def haveCommonSubject(arr1,arr2):          #function for finding whether a common subject is present or not in between two nodes
	for i in range(len(arr1)):
		if arr1[i] == arr2[i] == '1':
			return True
	return False		

for i in range(1,len(arr)):
	for j in range(i+1,len(arr)+1):             
		if haveCommonSubject(arr[i],arr[j]):
			G.add_edge(i,j)                   #adding edges of nodes having common subjects

def Path(arr,G,arr1,arr2):                  #function for finding path between two nodes
	sPath = [arr1]
	while 1:
		adj_node = list(G.neighbors(arr1))
		if arr2 in adj_node:
			sPath.append(arr2)
			break
		for p in sPath:
			if p in adj_node:
				adj_node.remove(p)
		cArray = []
		for i in adj_node:
			count = 0
			for j,k in zip(arr[arr1], arr[i]):
				if j == '1' and k == '1':
					count=count+1
			cArray.append(count)    	
		h = adj_node[ cArray.index(max(cArray)) ]
		arr1 = h
		sPath.append(h)
	return sPath                           #returning the best possible path

print("Nodes          Path")
for i in G.nodes():
	for j in G.nodes():
		if(i!=j):
			print((str(i)+"->"+str(j)+ "     path:"+str(Path(arr,G,i,j) )))      #printing paths

nx.draw(G,with_labels=1)
plt.show()                              #plotting the graph