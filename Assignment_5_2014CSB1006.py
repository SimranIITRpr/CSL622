import networkx as nx
import matplotlib.pyplot as plt

Dict = {}       #Creating a dictionary

f = open("subj.txt")    #Reading the sub.txt file and storing it into the dictionary named Data
for l in f.readlines():
    Dict[int(l.strip().split()[0])] = l.strip().split()[1:]

nodes = Dict.keys()     #Creating the Graph
G = nx.Graph()
G.add_nodes_from(nodes)

def isSameSubject(N_1, N_2):    #Returns True if common subject exists between N_1 and N_2
    for i in range(len(N_1)):
        if N_1[i] == '1' and N_2[i] == '1':
            return True
    return False        


def findPath(G, Dict, source, destination):     #Returns path from N_1 to N_2 
    path = [source]
    while True:
        neighbors = list(G.neighbors(source))
        if destination in neighbors:
            path.append(destination)
            break

        for p in path:
            if p in neighbors:
                neighbors.remove(p)

        edgeWeight = []
        for i in neighbors:
            count = 0
            for p, q in zip(Dict[source], Dict[i]):
                if p == '1' and q == '1':
                    count+=1
            edgeWeight.append(count)        
        newEdge = neighbors[edgeWeight.index(max(edgeWeight)) ]
        path.append(newEdge)
        source = newEdge
    return path

dictLength = len(Dict)
#print dictLength

for i in range(1, dictLength):
    for j in range(i+1, dictLength+1):
        if isSameSubject(Dict[i], Dict[j]):
            G.add_edge(i, j)

for i in G.nodes():       #Showing the path between 
    for j in G.nodes():
        if(i!=j):
            print "Path from "+str(i)+" to "+str(j)+" is : " , str(findPath(G, Dict, i, j))

nx.draw(G, with_labels=True)   #Showing the graph with labels
plt.show()