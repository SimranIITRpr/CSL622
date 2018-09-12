import networkx as nx 
import random as rn
import matplotlib.pyplot as plt 

https://snap.stanford.edu/data/wiki-Vote.html - dataset link

G = nx.read_edgelist("wiki-Vote.txt",create_using=nx.DiGraph(),nodetype = int)

n = G.number_of_nodes()
#number of nodes
tele = 0.2
 #teleporting probability

nodes = G.nodes()
#print(nodes)
    
pageRank = {}
for i in list(G.nodes()):
    pageRank[i]=0
    

rand = rn.choice(nodes)
for i in range(1,1000000):
	current = rand
	pageRank[current]+=1
	if(rn.random()<0.2):
		rand = rn.choice(nodes)

	else:
		nei = G.neighbors(current)
		if (len(nei)==0):
			rand = rn.choice(nodes)
		else:
			rand = rn.choice(nei)


sorted_count = sorted(pageRank.items(), key=lambda x: x[1], reverse=True)
nodes_rank = [i[0] for i in sorted_count]


print(nodes_rank)


pagerank = nx.pagerank(G)
pg_sort = sorted(pagerank.items(),key=lambda x: x[1], reverse=True)
page_rank = [i[0] for i in pg_sort]
print(page_rank)





