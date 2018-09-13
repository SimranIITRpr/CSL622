import networkx as nx

def edge_betweeness(g):
  btw_list={}
  betweeness=0
  for e in list(g.edges()):
    betweeness=0
    for u in list(g.nodes()):
      for v in list(g.nodes()):
        if(u!=v):
          s_paths=list(nx.all_shortest_paths(G,ii,jj))
          if(len(s_paths)>0):
            length=len(s_paths)
            for i in range (length):
              for j in range (length-1):
                if(s_paths[i][j] == e[0] and s_paths[i][j+1] == e[1]):
                  count = count+1
            betweeness += counter/len(s_paths)
    btw_list[e]=betweeness

g=nx.karate_club_graph()
while(nx.is_connected(g)):
  mat = nx.edge_betweenness_centrality(g)
  max_betweeness=-1
  index=0
  for E in (g.edges()):
    if(mat[E]>max_betweeness):
      edge=E
      max_betweeness=mat[E]
  g.remove_edge(edge[0],edge[1])
nx.draw(g,with_labels=1)