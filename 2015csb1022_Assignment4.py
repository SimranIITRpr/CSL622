import networkx as nx
import random
import matplotlib.pyplot as plt
#
'''
     Author: Pankaj Verma
     Date : 13 September 2018
    
     Required python packages: networkx

     input : Zachary karate club network

     output : plot consist of two communities
  
'''	
def find_community(input_graph_file):
    # Reading the network from text file
	G = nx.read_edgelist(input_graph_file, nodetype = int)
    # totalnumber of nodes
	num = G.number_of_nodes()
    #list of nodes
	node =list(G.nodes())
    # list of edges
	Edge_list =  G.edges()
    # list l for count the total short path across each and every edge
	l={}

	for i in Edge_list:
		l[i] = 0  # initialiaze with 0 

	while(nx.is_connected(G)):
		for i in range (num):
			for j in range (i+1,num):
				if(i!=j):
					X = nx.shortest_path(G,source=node[i],target=node[j]) # shortes path across (i,j) edges
					length = len(X) # total no of shortest path across (i,j) edge
					for k in range(1,length-1):
						m,n = min(X[k],X[k+1]),max(X[k],X[k+1])
						l[(m,n)] +=1

		total = num*(num-1)/2 # total exist shortest path in graph 
		for i in Edge_list:
			l[i] = (l[i]*1.0)/total # compuitng edge betweeness centrality

		
		l1 = []
		for i,j in l.iteritems():
			l1.append((j,i))
        # sorting all the edges according to betweenes 
		l1 = sorted(l1)	

		x = l1.pop()
		print(x)	
		G.remove_edge(x[1][0],x[1][1])

	nx.draw(G, cmap = plt.get_cmap('jet'),with_labels = True)
	plt.title("find community in Zachary Karate network")
	plt.show()	

if __name__ == "__main__":
	input_graph_file = "ucidata-zachary.txt"
	find_community(input_graph_file)
