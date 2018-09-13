"""
Name- Subhranil Bagchi
Entry No.- 2018CSY0002
Assignment4 - Finding communities in a graph.
"""

import networkx as nx
import matplotlib.pyplot as plt

def shortest_paths(G):
    listNodes = list(G.nodes())
    thePaths = []
    for i in range(len(listNodes)):
        for j in range(i+1,len(listNodes)):
            allPaths = list(nx.all_shortest_paths(G,source=listNodes[i],target=listNodes[j]))
            for k in allPaths:
                if len(k)>0: thePaths.append(k)
    return(thePaths)
    
def edge_betweenness(G):
    theEdges = []
    edgeCount = []
    for i in G.edges():
        edgeCount.append([[i[0],i[1]],0])    
    for i in thePaths:
        for j in range(len(i)-1):
            theEdges.append([i[j],i[j+1]])            
    for i in edgeCount:
        for j in theEdges:
            if (((i[0][0]==j[0]) and (i[0][1]==j[1])) or ((i[0][0]==j[1]) and (i[0][1]==j[0]))):
                i[1] = i[1] + 1                
    edgeCount.sort(key = lambda x:x[1], reverse=True)
    return(edgeCount)    
    
def find_communities(G,edgeCount,count):
    for i in G.edges():
        if ((edgeCount[0][0][0]==i[0]) and (edgeCount[0][0][1]==i[1])):
            G.remove_edge(*i)
            break
    count = count + 1
    numberConnectedComponents = nx.number_connected_components(G)
    return(G,count,numberConnectedComponents)
    
#importing Zachary Karate
G = nx.karate_club_graph()
count = 0
numberConnectedComponents = nx.number_connected_components(G)
while(numberConnectedComponents==1):
    #calculating the shortest paths for each node
    thePaths = shortest_paths(G)
    #calculating edge betweenness
    edgeCount = edge_betweenness(G)
    #find communities
    [G,count,numberConnectedComponents] = find_communities(G,edgeCount,count)
    
nx.draw(G,with_labels=True)
plt.show()

connectedComponents = nx.connected_components(G)
print("The connected components are:")
for i in connectedComponents:
    print(i)
print("The number of iterations required is ", count)