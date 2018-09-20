import networkx as nx
import matplotlib.pyplot as plt
from itertools import permutations
G=nx.Graph()
#creating dictionary mydict and storing nodes as keys and tuples as values manually
#no reading from input
mydict=dict()
mydict={1:[1,1,1,0,0,0,0,0,0,0,0,0],
2:[1,0,1,1,0,0,0,0,0,0,0,0],
3:[1,1,0,1,0,0,0,0,0,0,0,0],
4:[1,0,0,0,1,1,1,1,0,0,0,0],
5:[0,0,0,0,0,0,0,0,1,1,0,0],
6:[0,0,1,0,0,1,0,0,0,1,0,0],
7:[0,0,0,0,0,0,0,1,1,1,0,0],
8:[1,1,0,0,1,0,0,1,0,0,0,0],
9:[0,0,0,0,0,1,0,0,0,1,0,0],
10:[0,0,0,0,0,0,0,0,1,0,0,1],
11:[1,0,1,1,0,0,0,0,0,0,0,0],
12:[0,1,0,0,0,0,1,0,1,1,0,0],
13:[0,1,0,0,0,0,0,0,1,0,1,0],
14:[0,0,0,0,0,0,0,0,1,0,0,1]}
nod=list(mydict.keys())
#creating a list of nodes from keys of mydict
G.add_nodes_from(nod)
#making a list of all possible pairings between nodes of the graph
x=list(permutations(G.nodes(),2))
c=len(x)
#one by one taking pair from x and check wether there is tuple of that pair whose vakue is 1
#counting number of tuples having value 1 and if they have such tuple then adding an edge between pair of nodes with weight n 

for y in range(c):
         j1=x[y][0]
         j2=x[y][1]
         n=0
         for w in range(12):
             if mydict[j1][w]==1 and mydict[j2][w]==1:
                 n=n+1
         if n>0:
             G.add_edge(j1,j2,weight=n)
print(G.edges()) 
nx.draw(G)
plt.show()
#drawing graph
#printing possible shortest paths    
for z in range(c):
     
      j1=x[z][0]
      j2=x[z][1]
      for p in nx.all_shortest_paths(G,source=j1,target=j2):
          print(p)
           
      

            
     
        
        
