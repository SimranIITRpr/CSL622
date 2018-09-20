import networkx as nx
import matplotlib.pyplot as plt
import random as rand

# We will store our grap in G
G=nx.Graph()
# It stores the data of given text file subj.txt
# in array
with open('subj.txt') as f:
    array = [[int(x) for x in line.split()] for line in f]

# n stores the total number of nodes
n=len(array)

# m stores number of subjects.

m=len(array[0])
print n
print m

# c stores the list of keys in array.
c=list(array.keys())

# This 3 loops iterates all possible pairs of students
# and if we found a subject common then it adds an edge
# in graph G between that pair of node.
for i in range(0,n-1):
	for j in range(i+1,n):
		for k in range(1,m):
			if(array[i][k] + array[j][k] == 2):
				G.add_edge(i+1,j+1)
				break

# It plots the graph.
nx.draw(G, cmap = plt.get_cmap('jet'),with_labels = True)
plt.title("Seprating connected graph into 2 communities")
plt.show()

# This loop finds the shortest path between any two nodes
# and prints it.

for x in itertools.combinations(c,2):
    s=[]
    t=0
    for p in nx.all_shortest_paths(G,source=x[0],target=x[1]):
        if G[p[0]][p[1]]['weight']>t:
            t=G[p[0]][p[1]]['weight']
            s=p
    fin.append(s)
for i in fin:
    print(i)


