import networkx as nx                   #importing packages
import matplotlib.pyplot as plt

G = nx.karate_club_graph()        #importing Zachary Karate Club

def betweenness(G):          #function for edge betweenness
	Matrix = []
	num = len(G.nodes())        #number of nodes
	for i in xrange(num):
		Matrix.append([])
		for j in xrange(num):
			Matrix[i].append(0)     #all values in matrix are initiated to 0
	count = 0
	for i in xrange(num):	
		st = nx.single_source_shortest_path(G,i)	#default function for finding shortest path
		for l in range(len(st)): 
			for m in range(len(st[l])-1):
				Matrix[st[l][m]][st[l][m+1]]+=1.0
		count = count+len(st)                        #incrementing count
	for i in range(num):
		for j in range(num):
			Matrix[i][j] = Matrix[i][j]/count          #updating matrix
	return Matrix

while(nx.is_connected(G)):       #checking if the graph is connected or not
	row = 0 
	col = 0
	Matrix = betweenness(G)          #calling the edge betweenness function
	Maximum = Matrix[0][0]
	for i in range(len(G.nodes())):
		for j in range(len(G.nodes())):
			if(Maximum < Matrix[i][j]):
				row = i
				col = j
				Maximum = Matrix[i][j]       #finding the maximum to remove it
	G.remove_edge(row,col)          #removing the edge
	
nx.draw(G,with_labels=1)
plt.show()                   #showing the graph


