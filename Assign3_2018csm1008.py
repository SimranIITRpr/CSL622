'''
Name: Ganesh Prasad (2018csm1008)

Assignment 3 Random walk.

dataset used: google-web.csv
source website: http://networkrepository.com/web-google.php
---This dataset contains edges between web pages ---

dataset format: csv 																							
'''

import networkx as nx
import matplotlib.pyplot as plt 
import random

''' for teleporting with probabilty'''
from numpy.random import choice 

G = nx.read_edgelist(r"web-google.csv", create_using = nx.DiGraph(), nodetype = int)

#nx.draw(G, with_labels = True)
#plt.show()

'''
	Total walks will be 3rd power of the number of nodes in the graph
'''
nodes = G.nodes()
count = {node:0 for node in nodes}

def teleporting():
	return random.choice(list(nodes))

# initially pick a random node to start with

random_node = random.choice(list(nodes))

for times in range(len(nodes)**2):
	teleport = choice([True, False], 1, p=[0.2, 0.8])
	if teleport:
		random_node = teleporting()
		count[random_node]+=1
	else:
		successors = list(G.successors(random_node))
		if len(successors) == 0:
			random_node = teleporting()
			count[random_node]+=1
		else:
			random_node = random.choice(successors)
			count[random_node]+=1

sortedcount = sorted(count.items(), key=lambda x: x[1], reverse = True)
page_rank = sorted(nx.pagerank(G).items(), key=lambda x: x[1], reverse = True)

print "pagerank using randomwalk","   -   ","pagerank using networkx function"

for (randomwalk, pgval),(pagerank, pgval) in zip(sortedcount, page_rank):
	print randomwalk,"    -     ",pagerank
