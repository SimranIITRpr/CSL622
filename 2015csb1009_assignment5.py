import networkx as nx
import operator
import matplotlib.pyplot as plt
data = {}
def should_add_edge(a, b):
    weight=0
    for i in range(len(b)):
        if a[i] == b[i] == '1':
            weight=weight+1
    return weight
    

def DFS_rec(src,visited,dst,parent):
	visited[src]=parent
	sorted_list=sorted(G[src].items(), key=operator.itemgetter(1),reverse=True)
	vertices=[]
	for vertex_data in sorted_list:
		vertices.append(vertex_data[0])
	if dst in vertices:
		visited[dst]=src
		return       
	else:
		for neighbor in vertices:
			if neighbor not in visited:
				DFS_rec(neighbor,visited,dst,src)


def DFS(src,parent_dict,dest): 
        DFS_rec(src,visited,dest,-1)


f = open("subj.txt")
for l in f.readlines():
    tmpData = l.strip()
    data[int(tmpData.split()[0])] = tmpData.split()[1:]

#Creating graph
nodes = data.keys()
G = nx.Graph()
G.add_nodes_from(nodes)
for i in range(1, len(data)):
    for j in range(i+1, len(data)+1):
        weight=should_add_edge(data[i], data[j])
        if  weight>0:
            G.add_edge(i, j)
            G[i][j]['weight']=weight

for src in range(1,len(data)+1):
	for dest in range(src+1,len(data)+1):
		visited={}
		#print(src,dest)
		DFS(src,visited,dest)
		path=[]
		tmp_dest=dest
		while visited[dest]!=-1:
			path.append(dest+1)
			dest=visited[dest]
		path.append(src+1)
		path.reverse()
		print "Path from  "+" "+str(src+1)+" "+str(tmp_dest+1)+" "+str(path)