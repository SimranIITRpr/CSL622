'''
graph was taken from snap dataset
the link of it is:https://snap.stanford.edu/data/web-Google.txt.gz
roll no:2016csb1035
assignment 3.
'''
import networkx as nx
import matplotlib.pyplot as ply
import random
import numpy

# webgraph from snap dataset
G=nx.DiGraph() 
G = nx.read_edgelist('web-Google.txt', nodetype = int)
n = len(G.nodes())
N=list(G.nodes())
L=list(G.nodes())
#m=len(L)
print('no of nodes in graph:')
print(n)
#print(m)

#array to store ranks of all nodes
rank={}
Z={}
pr={}
for i in N:
    rank[i]=0
    Z[i]=0
    pr[i]=0
#print(len(rank))#check
current=random.choice(N)
rank[current] = 1 
#walk for 1000000 steps
#start walk
A=[1,2,3,4,5,6,7,8,9,10]
for i in range(1000000):
        p=random.choice(A)
        if(p<=2):    #teleport
               current=random.choice(N)
               #if(current==start) : current = (current+1)
               rank[current]=rank[current]+1
        else:				
               M=list(G.neighbors(current))
               if(len(M)==0):current = random.choice(N)			  
               current = random.choice(M)
               rank[current]=rank[current]+1
#print(len(rank))                   
pr = nx.pagerank(G, alpha=0.5)
#algo to sort the given lists
def sort_list(list1, list2): 
  
    zipped_pairs = zip(list2, list1) 
  
    z = [x for _, x in sorted(zipped_pairs)] 
      
    return z 
#sorting the both lists
sort_list(N,rank)
sort_list(L,pr)	
#comparing
#find the mean of differences and if it is pretty when compared to 900000 then we can say it is almost similar
for i in N:
     Z[i]=N[i]-L[i]
mean = sum(Z)/len(Z)	 
print(mean)
