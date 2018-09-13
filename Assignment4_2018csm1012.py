import networkx as nx 
import random


def length(a):
 c=0; 
 for i in a:
  c+=1
 return c


def count(p,k):
 c=0
 for i in p:
  for j in range(len(i)-1):
    if(i[j]==k[0] and i[j+1]==k[1]):
      c+=1
 return c


def Between(G):
  nodes=G.nodes()
  edges=G.edges()
  btw={}
  for y in edges:
   btw[y]=0
  for k in edges:
    for i in nodes:
      for j in nodes:
        if(nx.has_path(G,i,j)==True and i!=j):  
          p=nx.all_shortest_paths(G,i,j)
          C=0
          for x in p: 
            C+=1
          S=C
          c=0
          p=nx.all_shortest_paths(G,i,j)
          for z in p:
            for q in range(len(z)-1):
              if(z[q]==k[0] and z[q+1]==k[1]):
                c+=1
          s=c
          btw[k]+=float(s)/S
  return dict(sorted(btw.items(), key=lambda x:x[1],reverse=True))



G=nx.karate_club_graph()
while(nx.is_connected(G)==True):
 y=Between(G)
 h=list(y.keys())
 for u in h:
  G.remove_edge(h[0][0],h[0][1])
  break 
 

v=nx.connected_components(G)
for t in v:
 print(t)
 




      



