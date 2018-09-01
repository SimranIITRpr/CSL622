''' 
2015CSB1117 - Shubham Dham, 2015CSB1067 - Nittin Singh, 2015CSB1065 - Narotam Singh

After running the code observe the plot.
The node marked in green has the highest node betweenness meaning it has highest probability to lie
on a randomly chosen shortest path between two vertices. The edge marked in red (between red nodes) 
has the highest edge betweenness and has bridgey nature. Removal of the green node 
or the red edge may affect the communication in a network. The main 
motive here is to show that the nodes involved in the two scenarios are not the same. It may 
seem that a node with high node betweenness should have high edge betweenness but thats not 
the case.

'''
def centralityEdgeMeasure():
    G = nx.read_adjlist('pagerank.txt',nodetype = int,create_using = nx.DiGraph())
    centralities2 = []
    centralities1 = []
    centralities1.append(nx.betweenness_centrality(G))
    diction1 = centralities1[0]
    key1, value1 = max(diction1.items(), key = lambda x:x[1])
    centralities2.append(nx.edge_betweenness_centrality(G))
    diction2 = centralities2[0]
    key2, value2 = max(diction2.items(), key = lambda x:x[1])
    color_map1 = []
    color_map2=[]
    weights=[]
    pos = nx.spring_layout(G)
    for node in G:
        if node == key1:
            color_map1.append('#228B22')
        elif node == key2[0] or node==key2[1]:
            color_map1.append('r')
        else:
            color_map1.append('b')

    for edge in G.edges():
        if edge==key2:
            color_map2.append('r')
            weights.append(7)
        else:
            color_map2.append('#000000')
            weights.append(0.5)
    nx.draw(G,pos,node_color = color_map1,edge_color=color_map2, with_labels =1,width=weights)
    plt.show()
    return key1
centralityEdgeMeasure()