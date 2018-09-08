#Name Rakesh Kumar Meena
#Roll Number 2018CSM1017
#Dataset is accessed from 'http://networkrepository.com/web-google.php'
#web-google data different types of nodes connected through directed Edges.
#here node repersent the google webpages and edges represent the link present between them.

import networkx as nx
import matplotlib.pyplot as plt
import random
import operator
from random import choice
G= nx.read_edgelist("web-google.txt",create_using=nx.DiGraph(),nodetype=int)

#counter to count no of times node visit
VistedNodecounter=0

#convert all int node to string
results = list(map(int, nx.nodes(G)))

#select a random node
random_node=choice(results)
print("total node in graph",nx.number_of_nodes(G))
print()
print("total edge in graph",G.number_of_edges())
print()
###RANDOM WALK ####
print("First Random node",random_node)

aa=nx.number_of_nodes(G)
aaa=aa**2
visitedNode={}
for i in range(aaa):
    if( random_node in visitedNode):
        visitedNode[random_node]+=1
    else:
        visitedNode[random_node]=1
        VistedNodecounter+=1
        
    if random.randint(0,10)<8:
        #find neighbors of random_node and select next random node from neigh
        x=list(G.neighbors(int(random_node)))
        if(len(x)!=0):
            random_node=random.choice(x)
            
        else:
            random_node=random.choice(results)
            
    else:
        #teleport with new node.
        random_node=random.choice(results)
rvv=[]
for k, v in sorted(visitedNode.items(), key=operator.itemgetter(1),reverse=True):
    rvv.append(k)

print()
print("Total Number of node Visited=",VistedNodecounter)
print()
####PAGE RANK####
pr=nx.pagerank(G)
pvv=[]
for kk,ll in sorted(pr.items(), key=operator.itemgetter(1),reverse=True):
    pvv.append(kk)

#comparision between random walk and page Rank
print("comparision between random walk and page Rank")
print()
print("Random Walk ------Page Rank")
for m,n in  zip(rvv,pvv):
    print(m,"  ---- ",n)

