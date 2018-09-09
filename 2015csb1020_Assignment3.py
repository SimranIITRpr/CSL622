import networkx as nx
import random as rand
import matplotlib.pyplot as plt
import operator
DG = nx.read_edgelist("web-Google.txt", "r", create_using=nx.DiGraph(), nodetype = int) 
A=list(DG.nodes())

a=0
visited={}

for i in A :
    visited[i]=0
    
    
    
vis=rand.choice(A)
visited[vis]=1
#j=10000000
print("Running............\n")
for i in range(10000000):
    if  rand.random()<0.2:
        vis=rand.choice(A)
        visited[vis]=visited[vis]+1
    else :
        nbrs=list(DG.neighbors(vis))
        nlen=len(nbrs)
        if nlen == 0 :
            vis=rand.choice(A)
            visited[vis]=visited[vis]+1
        else :
            vis = rand.choice(nbrs)
            visited[vis]=visited[vis]+1
            
            
D1 = nx.pagerank(DG)

Randomwalk = [x[0] for x in sorted(visited.items(), key=operator.itemgetter(1),reverse=True)]
Pagerank = [x[0] for x in sorted(D1.items(), key=operator.itemgetter(1),reverse=True)]
i=0
print("RandomWalk vs Pagerank")
while i <50:
    print (str(Randomwalk[i])+" "+str(Pagerank[i]))
    i=i+1
    
# IF you see the observation you can see that the rank are nearly same.This is my observation.    