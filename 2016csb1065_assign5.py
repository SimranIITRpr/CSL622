import networkx as nx
import math
import matplotlib.pyplot as plt

file=open('subj.txt','r')
nodes_dic={}
for line in file:
	nodes_dic[int(line.split()[0])]=[int(x) for x in line.split()[1:]]
G=nx.Graph()
for i in nodes_dic:
	for j in nodes_dic:
		if i!=j:
			first=nodes_dic[i]
			second=nodes_dic[j]
			cal_weight=0
			for k in range(len(first)):
				if first[k]==1 and first[k]==second[k]:
					cal_weight+=1                    
                            	if cal_weight!=0:
                                	cal_weight=math.exp(-cal_weight)
                                	G.add_edge(i,j,weight=cal_weight)
for i in G.nodes():
	for j in G.nodes():
		if i!=j:
			path=nx.dijkstra_path(G,i,j) 
			print "BEST PATH :(",i,j,') is ',path
nx.draw(G,with_labels=True)
plt.show()                                
