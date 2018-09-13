import networkx as nx
#Done By : ALLU KRISHNA SAI TEJA(2015csb1005)

#this returns the edge to be removed
def remove(G):
   dict={}
   for e in G.edges():#iterating over each edge
    s=e[0]
    t=e[1]
    dict[e]=0
    num=0.0
    den=0.0
    for i in G.nodes(): # for all u
        for j in G.nodes(): # for all v
            if j!=i:
                shortest_paths=list(nx.all_shortest_paths(G,i,j))
                length=len(shortest_paths)
                den=den+length
                contain_edge=0
                for x in shortest_paths:
                 	for h in range(len(x)-1):
                 	    if x[h]==s and x[h+1]==t: # check if the edge exists in the path
                 	        num=num+1.0
    dict[e]=num/den #store the betweeness of an edge e
   list_tuples=dict.items()
   list_tuples.sort(key=lambda x:x[1],reverse=True)
   return list_tuples[0][0]

G=nx.karate_club_graph()
c=list(nx.connected_component_subgraphs(G))
l=len(c)
while l==1 :
       G.remove_edge(*remove(G))
       c=list(nx.connected_component_subgraphs(G))
       l=len(c)
       print "Number Of Components : "+str(l)
for i in c :
    print i.nodes()	