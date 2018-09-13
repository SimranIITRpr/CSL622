#!/usr/bin/python

#2015csb1040 VISHAL SINGH

# DATASET: Wikipedia vote network
# Link - https://snap.stanford.edu/data/wiki-Vote.html
# nodes=7115
# edges=103689
# nodes in the network are users and there is an edge if
# user i voted on user j
# it can be seen that the plot b/w pagerank and randomwalk
# is almost linear.Also the values on X and Y axis are not same
# because pagerank is normalised and gives value between 0 and 1.


import networkx as nx
import matplotlib.pyplot as plt
import random as rand

G =  nx.read_edgelist("Wiki-Vote.txt",create_using=nx.DiGraph(), nodetype = int)

rank = {} #to store number of times a node is visited
for item in list(G.nodes()):
    rank[item]=0 # count initially is zero

x=rand.choice(list(G.nodes())) # randomly choose a node
rank[x]+=1

# do random walk for some iterations
for i in range(G.number_of_nodes()*100):
    p=rand.random() # random probability to teleport
 
    if p<0.2:
        x=rand.choice(list(G.nodes()))
    elif len(list(G.successors(x)))==0:# if there no neighbours of node
        x=rand.choice(list(G.nodes()))
    else: # p>=0.2 choose randomly from the neighbours
        x=rand.choice(list(G.successors(x)))
    rank[x] += 1
    
    
vislist=list(rank.values())
keylist=list(rank.keys())
pageRank = nx.pagerank(G) 
rankp = [100000*pageRank[x] for x in keylist]#pagerank value scaled up 
plt.xlabel('Random Walk')
plt.ylabel('Pagerank')
plt.plot(vislist,rankp,'b.')
plt.show()


        
    
    







