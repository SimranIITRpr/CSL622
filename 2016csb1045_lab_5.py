"""
Nitin Gandhi
2016csb1045
"""
import networkx as nx

dictionary = {}


def intersection(a, b):
	for i in range(len(a)):
		if a[i] == b[i] == '1':
			return True
	return False	

def get_graph(dictionary):
	G = nx.Graph()
	nodes = dictionary.keys()
	for k in nodes:
		G.add_node(k)
	for i in range(1, len(dictionary)):
		for j in range(i+1, len(dictionary)+1):
			if(intersection(dictionary[i], dictionary[j])):
				G.add_edge(i, j)
	return G


def show(G):
	for i in G.nodes():
		for j in G.nodes():
			if(i != j):
				l = path_finder(G, dictionary, i, j)
				print(str(i),"     ->   ",str(j), "  ====> " ,str(l), "----------------------------------------> ", len(l))
	


def path_finder(G, dictionary, src, dest):
	path = [src]
	while True:
		neighbours = list(G.neighbors(src))
		if dest in neighbours:
			path.append(dest)
			break
		for p in path:
			if p in neighbours:
				neighbours.remove(p)
		weight = []
		for i in neighbours:
			counter = 0
			for one, two in zip(dictionary[src], dictionary[i]):
				if one == '1' and two is '1':
					counter = counter + 1
			weight.append(counter)    	
		best = neighbours[weight.index(max(weight))]
		path.append(best)
		src = best
	return path



if __name__ == "__main__":
	with open("subj.txt") as f:
		for line in f:
			k = line.strip().split()
			dictionary[int(k[0])] = k[1:]
	G = get_graph(dictionary)
	print("start   - >  End   ====>         PATH                 PATH_LENGTH")
	print("-----------------------------------------------------------------------")
	show(G)
	

			
