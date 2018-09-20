"""
   Assignment 3 :- Random Walk implementation and rank comparison of the ranks
   calculated from Random Walk and from inbuilt pagerank method.

   Dataset used :- Google Web Graph from Snap
   Link to Dataset used :- https://snap.stanford.edu/data/web-Google.html
    
   Submitted By :- Abhishek Sharma (2015eeb1043)
"""

import networkx as nx
import random

# Loaded the graph from given adjacency list txt file of Google Web Graph dataset from Snap.
G = nx.read_adjlist('webgraph_dataset_google.txt')

# Created empty dictionary to keep track of count of individual nodes. 
count = {}

# Assigned the values for all nodes as 0 initially.
for i in list(G.nodes()):
    count[i] = 0

# curr_node will be the current node in the Random Walk from where we have to move further
# to its neighbors or teleport.
# It is initialized with some random node from the nodes of the Graph G.
curr_node = random.choice(list(G.nodes()))  

# Random walk will happen until this loop ends.   
for i in range(10000000):
    # Below list will keep the neighbors of curr_node.
    neighbors = [] 
    neighbors = list(G.neighbors(curr_node))

    # curr_node count is increased by 1 in the dictionary as it is visited in walk.
    count[curr_node] += 1

    # Below condition checks that if nodes has no neighbors and it also teleports when
    # with probability 0.2.
    if len(neighbors) == 0 or random.random() < 0.2:
        curr_node = random.choice(list(G.nodes()))
        continue

    # If control reaches here it means that teleport didn't happen and curr_node
    # will get assigned to one of the neighbors randomly.
    curr_node = random.choice(neighbors)

# Finally sorted the dictionary by values and saved it in sorted_count as list of tuples.    
sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)

# Getting the first element of tuples from sorted_count which will be the nodes in decreasing
# order of their ranks.
nodes_rank = [i[0] for i in sorted_count]

# Below we get the nodes rank by using inbuilt method pagerank().
pr = nx.pagerank(G)
     
sorted_pr = sorted(pr.items(), key=lambda x: x[1], reverse=True)

# Below list contains the nodes in decreasing order of their ranks by using pagerank().
page_rank = [i[0] for i in sorted_pr]

# Printed the ranks of nodes from both the methods.
print(nodes_rank) # Random Walk Ranks
print(page_rank)  # Pagerank Ranks 



    
    

