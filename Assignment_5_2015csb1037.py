import networkx as nx
import matplotlib.pyplot as plt 

G = nx.Graph()

nodes = []

with open("subj.txt", 'r') as fobj:
    for line in fobj:
        numbers = [int(num) for num in line.split()]
        G.add_node(numbers[0])
        numbers.pop(0)
        nodes.append(numbers)
  


def checkedge(a,b):
	count = 0
	for i in range(len(nodes[a-1])):
		if(nodes[a-1][i] == nodes[b-1][i] and nodes[a-1][i] == 1):
			count = count + 1
	return count


def getmax(source,neighbors,visited):
	maximum = 0;
	index = -1
	for i in range(len(neighbors)):
		if(G.get_edge_data(source,neighbors[i])['weight'] > maximum and visited[neighbors[i]] == 0):
			maximum = G.get_edge_data(source,neighbors[i])['weight']
			index = neighbors[i]
			
	return index

def findpath(a,b):
	path = [a]
	stack = [a]
	visited = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	visited[a] = 1
	while(len(stack) != 0):
		cur_source = stack[len(stack)-1]
		neighbours = list(G.neighbors(cur_source))
		if b in neighbours:
			path.append(b)
			return path
		else:
			maximum_bond_node = getmax(cur_source,neighbours,visited)
			if(maximum_bond_node != -1):
				stack.append(maximum_bond_node)
				path.append(maximum_bond_node)
				visited[maximum_bond_node] = 1
			else:
				stack.pop()
				path.pop()
	
	return path

for i in range(1,15):
	for j in range(i+1,15):
		if(checkedge(i,j) != 0):
			G.add_edge(i,j)
			G[i][j]['weight'] = checkedge(i,j)


for i in range(1,15):
	for j in range(i+1,15):
		print (findpath(i,j))




nx.draw(G,with_labels=True,edge_color='b')
plt.show()
