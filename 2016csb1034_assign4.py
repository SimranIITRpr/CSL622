import networkx as nx							
import matplotlib.pyplot as plt



G=nx.karate_club_graph()		

def betweenness(G):							
	count = 0	
	betw = []
	nodes= G.number_of_nodes()
	init = 0.0
	for i in xrange(nodes):				
		betw.append([])
		for j in xrange(nodes):
			betw[i].append(init)				
	for i in range(nodes):			 
		path = nx.single_source_shortest_path(G,i)
		temp = len(path)		
		for p in range(temp): 
			temp2 = len(path[p])-1				
			for k in range(temp2):
				betw[path[p][k]][path[p][k+1]]= 1.0 + betw[path[p][k]][path[p][k+1]]
		count = count+temp
	for i in range(nodes):			
		for j in range(nodes):
			betw[i][j] = betw[i][j]/count
	return betw				




while(nx.is_connected(G)):					
	betw = betweenness(G)				
	tempx =0
	tempy = 0
	max = -1.0
	temp = G.number_of_nodes()
	for i in range(temp):
		for j in range(temp):
			if(max < betw[i][j]):			
				(tempx,tempy,max)=(i,j,betw[i][j])
	G.remove_edge(tempx,tempy)						
						
nx.draw(G,with_labels = True)	
plt.show() 