
# 2015csb1040
# Vishal Singh

'''
A weighted undirected graph is created where weight for an edge 			 	
between two nodes is set as inverse of the number of common subjects			 	
between them. This inverse is done because we need the longest(in terms of weight)
path between every pair of nodes. Hence by taking inverse, the problem changes to shortest 	 
distance which can be done easily. By taking inverse and using shortest path
we will select the edge which has more common subject

When the nodes are directly connected then we do not consider the shortest path
rather we just print the direct edge between them.

'''

import networkx as nx
import matplotlib.pyplot as plt


# Reading input data
ll=[]
with open ("subj.txt") as f:
    lines=f.readlines()
    
for line in lines:
    content=line.split()
    P=[]
    for i in content:
        P.append(int(i))
    ll.append(P)

# create graph    
G = nx.Graph()
# Since first element of each line is our node
for i in ll:
	G.add_node(int(i[0]))


# Number of subjects
s = len(ll[0]) - 1


# add weighted edges
for i in range(len(ll)):
	for j in range(i+1,len(ll)):
		weight = 0
		for k in range(1,s+1):
			if ll[i][k] == 1 and ll[j][k] == 1:
				weight += 1
		if(weight):
			G.add_edge(ll[i][0],ll[j][0],weight=1/float(weight))


# plotting weighted graph		
pos=nx.spring_layout(G)
nx.draw(G,pos,with_labels = True)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.title("Subject Network")
plt.show()


# shortest path between each edge
for i in G.nodes():
	for j in G.nodes():
		if i != j:
			print 'shortest path between node ',i,' and ',j, 'is '
			if(G.has_edge(i,j)):		# when nodes are directly connected
				print '[',i,',',j,']'
			else:
				print nx.shortest_path(G,i,j) # when nodes are not directly connected
