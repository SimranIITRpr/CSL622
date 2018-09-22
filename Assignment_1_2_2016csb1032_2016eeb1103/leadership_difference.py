
#---2016eeb1103---2016csb1032---------

import networkx as nx
G = nx.read_edgelist("pagerank.txt",create_using=nx.DiGraph(), nodetype = int)
G.remove_node(35)
G.remove_node(40)
y = []
for i in range(33):
      if i == 17:
         continue
      p = G.in_edges(i+1)
      x = len(p)
      y.append(x)
p = G.in_edges(100)
y.append(len(p))

print (y)
y.sort()
print (y)
print ("diff in no. of friends of most and least interesting person : ")
print (y[len(y)-1]-y[0])
