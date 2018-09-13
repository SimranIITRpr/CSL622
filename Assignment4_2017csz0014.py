
import operator 
import networkx as nx
import matplotlib.pyplot as plt
G=nx.Graph()
G=nx.karate_club_graph()                  //for uploading karate club 


def edge_between(G):                                 //function to calculate the edge betweenness manually
    dict_edges={}
    for each in G.edges():                              //intialising dictionary edges to zero
            dict_edges[each]=0
    list_edges=[]
    total_path=0                                            
    for i in range(G.number_of_nodes()):                 
            for j in range(G.number_of_nodes()):
                    if(i!=j):
                            x=list(nx.all_shortest_paths(G,i,j))   //calculates the shortest path between all of nodes        
                            total_path=total_path+len(x)    //calculating total path length 
                            for item in dict_edges.keys():         
                                    list_edges=list(item)
                                    for m in range(len(x)):           
                                        for n in range(len(x[m])-1):
                                            if((x[m][n]==list_edges[0] and x[m][n+1]==list_edges[1]) or (x[m][n]==list_edges[1] and x[m][n+1]==list_edges[0])):
                                                    dict_edges[item]=dict_edges[item]+(1/len(x))  //calculate the edge betweeness
                            
    return dict_edges                                                




while(nx.is_connected(G)):                               //will run till the graph is connected
        m=[]
        dict_edges1=edge_between(G)
        m=list(dict_edges1.values()) 
        var=m[0]
        max=var
        for var in dict_edges1.values():
            if(max<var):                                    //calculating max of edge betweeness 
                max=var
                for j in dict_edges1.keys():
                    if(dict_edges1[j]==max):
                        print(j)
                        break
        
        if(G.has_edge(*j)):                                   //removing edges
            G.remove_edge(*j)
       
        nx.draw(G,with_labels=1)
        plt.show()
