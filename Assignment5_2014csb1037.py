#returns the graph of 14 students and also returns bunch of lists each list is a 
#shortest path i.e [source,...,some node,some other node,...,destination]
import networkx as nx
import matplotlib.pyplot as plt
import itertools
G=nx.Graph()
#getting data into a dictionary from the given file
a={1:[1,1,1,0,0,0,0,0,0,0,0,0],
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
b=len(a)
#getting all the nodes into c
c=list(a.keys())
#getting the tuples into d
d=list(a.values())
#adding nodes into G
G.add_nodes_from(a)
fin=[]
#this function calculates the weight of the of the function i.e no of subjects common for m,n
def we(m,n):
    q=0
    for p in range(min(len(m),len(n))):
        if m[p]==1 and n[p]==1:
            q+=1
    return q
#adding edges to G if the nodes have a common subject
for i in range(b):
    for j in range(i+1,b):
        n=we(d[i],d[j])
        if(n>0):
            G.add_edge(c[i],c[j],weight=n)
#drawing the obtained graph
nx.draw(G,with_labels = True, node_color = 'b')
plt.show()
#finding the shortest path according to number of subjects they have in common
for x in itertools.combinations(c,2):
    s=[]
    t=0
    for p in nx.all_shortest_paths(G,source=x[0],target=x[1]):
        if G[p[0]][p[1]]['weight']>t:
            t=G[p[0]][p[1]]['weight']
            s=p
    fin.append(s)
#printing all the shortest paths
for i in fin:
    print(i)