#	Piyush Pilaniya
#	2016csb1049
# 	Assignment 3


import networkx as nx
from random import randint
import random
#import matplotlib.pyplot as plt

G=nx.read_edgelist("Wiki-Vote.txt",nodetype=int)

start=random.choice(list(G.nodes()))
counter=dict((pp,0) for pp in G.nodes())	
counter[start]=counter[start]+1

for ip in range(100000):
	out_edges = [d for d in G.neighbors(start)]
	if len(out_edges)!=0:
		val = randint(0,9)
		if val>=2:	#choosing from neighbors with probability 0.8
			next = random.choice(out_edges)
			counter[next]=counter[next]+1
			start=next
		else:
			next = random.choice(list(G.nodes()))
			counter[next]=counter[next]+1
			start=next	
	else:
		start = random.choice(list(G.nodes()))
		counter[start]=counter[start]+1				

print (counter)

pr = nx.pagerank(G, alpha=0.9) #with damping parameter 0.9 instead of default 0.85
inbuilt_pagerank=list()						
for key, value in sorted(pr.iteritems(), key=lambda (k,v): (v,k),reverse=True):
	inbuilt_pagerank.append(tup[1])

teleport_pagerank=list()
for key, value in sorted(counter.iteritems(), key=lambda (k,v): (v,k),reverse=True):
	teleport_pagerank.append(tup[1])

plt.title("Inbuilt PageRank vs Teleportation PageRank with 0.2 probability to teleport")		#Labels and Title
plt.xlabel("Pagerank")
plt.ylabel("Teleport")
plt.plot(inbuilt_pagerank,teleport_pagerank,'b',linewidth=7.0)						#Plotting the graph for comparision
plt.show()

