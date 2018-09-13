import operator 
import networkx as nx
import matplotlib.pyplot as plt

def Edge_Betweennes(G) :
    
    Edgebetweeness={}
    
    for i in list(G.edges()) :
        Edgebetweeness[i]=0
        
    count=0   
    for i in list(G.nodes()) :
        
        for j in list(G.nodes()):
            
            if i!=j :
                
                all_paths=list(nx.all_shortest_paths(G, source=i, target=j))
                count=count+len(all_paths)
                for i1 in range(0,len(all_paths)) :
                    
                    for j1 in range(0,len(all_paths[i1])-1) :
                        ed=(all_paths[i1][j1],all_paths[i1][j1+1])
                        #if (ed in G.edges()):
                        for edges in list(G.edges()) :
                            if(edges[0]==all_paths[i1][j1] and edges[1]==all_paths[i1][j1+1]) :
                                  Edgebetweeness[edges]= Edgebetweeness[edges]+1   
                    
    
    for i in list(G.edges()) :
        Edgebetweeness[i]=Edgebetweeness[i]/count
    
    return Edgebetweeness

def Find_Comunnites(G) :
    while (nx.is_connected(G)):
            Betweens=Edge_Betweennes(G)
            
            j=0
            maxB=-1
            for E in list(G.edges()) :
                if(Betweens[E]>=maxB) :    
                    maxB=Betweens[E]
                    Edge=E
            x=Edge[0]
            y=Edge[1]
            #print(str(x)+" "+str(y))
            G.remove_edge(x,y)
    
    return G.edges()
    
G=nx.Graph()
G=nx.karate_club_graph()   
#nx.draw(G ,with_labels = 1) # before community seperation
#plt.show()

edgelist=Find_Comunnites(G)   
nx.draw(G ,with_labels = 1) # After community seperation
plt.show()
