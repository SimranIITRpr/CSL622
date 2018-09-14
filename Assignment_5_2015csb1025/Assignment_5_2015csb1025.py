import networkx as nx
import matplotlib.pyplot as plt

# Reading input data
fname = "subj.txt"
with open(fname) as f:
	Content = f.readlines()
	Content = [x.strip() for x in Content]

Input = []

for content in Content:
	X = content.split()
	P = []
	for i in X:
		P.append(int(i))
	Input.append(P)

# To store nodes of graph
Nodes = []

# Since first element of each line is our node
for i in Input:
	Nodes.append(i[0])

# Constructing the network
G = nx.Graph()

# Adding nodes as read
G.add_nodes_from(Nodes)

# Number of nodes
n = len(Nodes)

# Number of subjects
s = len(Input[0]) - 1

# TO store edges to be added
Edges_to_add = []

'''

	Finding out which all edges need to be added and with what weight

Here we used below function to define edge weight
	edge weight b/w u and v = (number of nodes i.e n) +  - (number of common 1's b/w u and v) 
From above edge weight function more the common subject two nodes have, lesser the weight will be
Hence more frequently that edge will be used in finding shortest path as we are aiming to use those edges frequently
'''
for i in range(n):
	for j in range(i+1,n):
		c = 0
		for k in range(1,s+1):
			if Input[i][k] == 1 and Input[j][k] == 1:
				c += 1
		if c != 0:
			Edges_to_add.append((Nodes[i],Nodes[j],n+1-c))
		
G.add_weighted_edges_from(Edges_to_add)

nx.draw(G, cmap = plt.get_cmap('jet'),with_labels = True)
plt.title("Subject Network")
plt.show()

# Storing all the nodes in a list
V = list(G.nodes())

# storing all the dges
E =  G.edges()

# To count total number of shortest paths
# passing through each edge
Count = {}

while(nx.is_connected(G)):
	# Calculating betweeness centrality
	for i in E:
		Count[i] = 0

	for i in range(len(V)):
		for j in range(i+1,len(V)):
			X = nx.shortest_path(G,source=V[i],target=V[j])
			for k in range(len(X)-1):
				p,q = min(X[k],X[k+1]),max(X[k],X[k+1])
				Count[(p,q)] += 1
	# Dividing by number of shotest paths	
	c = n*(n-1)/2
	for i in E:
		Count[i] = (Count[i]*1.0)/c

	# TO sort all the edges according to betweenes centrality
	P = []
	for i,j in Count.iteritems():
		P.append((j,i))

	P = sorted(P)	

	x = P.pop()
	print(x)
	G.remove_edge(x[1][0],x[1][1])
	
p = V[0]
X = list(nx.connected_component_subgraphs(G))
Y = X[0].nodes()
Z = X[1].nodes()
color = []
for i in V:
	if i in Y:
		color.append('blue')
	else:
		color.append('red')

nx.draw(G, cmap = plt.get_cmap('jet'),with_labels = True,node_color = color)
plt.title("Two communities detection in network")
plt.show()
