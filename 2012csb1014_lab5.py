import networkx as nx
import numpy as np

def findWeight(subj1, subj2):
	weight = 0;
	for x in range(0,len(subj1)):
		if (subj1[x] == 1 and subj2[x] == 1):
			weight = weight + 1
	if (weight == 0):
		return weight
	return 12 - weight;

def readFile():
  with open('subj.txt') as f:
    array = [[int(x) for x in line.split()] for line in f if not line.strip().startswith("#")]
  return array

def __main__():
	data = readFile()
	G = nx.Graph()
	noOfNodes = len(data)
	for i in range(1, noOfNodes+1):
		G.add_node(i);

	for i in range(1, noOfNodes):
		for j in range(i+1, noOfNodes+1):
			weight = findWeight(data[i-1], data[j-1])
			if (weight):
				G.add_edge(i, j, weight=weight);

	shortestPaths = list(nx.all_pairs_shortest_path(G));
	for paths in shortestPaths:
		fromNode = paths[0];
		paths = paths[1];
		for toNode in paths.keys():
			if (fromNode != toNode and len(paths[toNode]) > 1):
				print('Shortest path from node ', fromNode, ' to ', toNode, 'is: ', paths[toNode]);

__main__();
