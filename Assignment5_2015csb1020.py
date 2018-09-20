import networkx as nx
import matplotlib.pyplot as plt
import operator

"""

We are finding path greedily using the next node with highest common value and if there is 
no path along that node we come back to that node and do it recursively using next neighbor with highest
common value.


"""


def DFSUtil(v,destination,visited,path,prev,G):
    path[v]=prev
    visited[v]= True
    
    if destination in G.neighbors(v) :
        path[destination]=prev
        return 
    
    weights={}
    
    for i in G.neighbors(v) :
        weights[i]=G[v][i]['weight']
    
    sorted_neighbors = sorted(weights.items(), key=operator.itemgetter(1),reverse=True)
    
    for i in sorted_neighbors:
        if visited[i[0]] == False:
            DFSUtil(i[0],destination,visited,path,v,G)

def DFS(v,destination,G):
    visited={}
    path={}
    for i in G.nodes():
        visited[i]=False
    DFSUtil(v,destination,visited,path,v,G)
    return path




with open("subj.txt") as subj:
    
    S = list([node.split() for node in subj ])


G = nx.Graph()
G.add_nodes_from(range(len(S)))
for i in range(len(S)) :
    for j in range(len(S)) :
        count=0
        if(i!=j)  :
            
            for x in range(len(S[i])-1):
                if (S[i][x+1]== '1' and S[j][x+1]== '1') :
                    count=count+1
            if count>0 :
                G.add_edge(i,j,weight=count)



for i in range(len(S)):
        for j in range(len(S)):
            if i!=j :
                pathdict=DFS(i,j,G)
                x=j;
                path=[]
                path.append(x)
                while pathdict[x]!=i:
                    path.append(pathdict[x])
                    x=pathdict[x]
                path.append(i)

                path.reverse()
                print("path from "+" "+str(i)+" to "+str(j)+" is "+str(path))
