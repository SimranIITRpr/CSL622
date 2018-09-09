import random as ra
import networkx as nx
import operator 

#https://snap.stanford.edu/data/wiki-Vote.html - dataset link

G=nx.DiGraph()
G=nx.read_edgelist('wiki-Vote.txt',create_using=nx.DiGraph(),nodetype=int)

nodes=list(G.nodes())

count={}
for item in nodes:
	count[item]=0

rnode=ra.choice(nodes)

for i in range(1,100000000): 		
	nebor=[]						#list that will contain the neighbours
	out=(G.out_degree(rnode)) 		#checking out degree
	count[rnode]+=1

	if( out == 0 ): 				#sink node 
		p=ra.random()
		if(p<=0.2):  				#Probability of teleportation is <= 0.2
			rnode=ra.choice(nodes)	#choosing another node from graph at random and then resuming the loop
		else:
			continue; 	  
	else:
		nebor=G.neighbors(rnode) 	
		rnode=ra.choice(nebor)

sortd=sorted(count.items(),key=operator.itemgetter(1),reverse=True)

print("our random walk is ")
for i in range(100): 				# change the range to len(nodes) to get full list
	print(sortd[i][0], end=' ',sep=' ',flush=True )

print("page rank is")
pr  = dict(nx.pagerank(G))
pr2 = sorted(pr.items(),key=operator.itemgetter(1),reverse=True)
for i in range(100):  				# change the range to len(nodes) to get full list
	print(pr2[i][0], end=' ',sep=' ',flush=True )
