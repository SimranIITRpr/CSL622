"""
Assignment 3: Random Walk

Code by: Subhranil Bagchi
Entry Number: 2018CSY0002

This code is of the random walk experiement over a directed graph. For a very very large
number of iterations, that is walk over a very large distance (w>>e), where w is the
walking distance and e is the number of edges in a directed graph over a v set of nodes.
Typically, random walk is suitable to be performed over a web graph.

For a small dataset, the web-edu directed graph with 3k nodes and 6k edges can be used.
The link is: http://networkrepository.com/web.php
And for a large dataset the UCBerkley and Standford one is also an option.
"""
import random
import networkx as nx
import matplotlib.pyplot as plt
import sys

#Sets a predefined recursion limit
sys.setrecursionlimit(100000000)

#Performs random walk by recursively calling itself
def random_walk(G,path_length,select_source,count_list):
    count_list[select_source] = count_list[select_source] + 1 #increases the count for that node
    if path_length!=0:
        node_successors = list(G.neighbors(select_source)) #finds neighbours
        if not node_successors:
            teleported_node = teleport(G,select_source) #calls teleportation
            random_walk(G,path_length-1,teleported_node,count_list)
        else:
            teleport_chosen = random.choice([1,0,0,0,0]) #probability of teleportation
            if teleport_chosen == 1:
                teleported_node = teleport(G,select_source) #calls teleportation
                random_walk(G,path_length-1,teleported_node,count_list)
            else:
                random_walk(G,path_length-1,random.choice(list(node_successors)),count_list)
    return(count_list)

#Performs teleportation until a different node is reached
def teleport(G,current_node):
    teleported_node = random.choice(list(G.nodes()))
    if teleported_node == current_node:
        return(teleport(G,current_node))
    else:
        return(teleported_node)

#Reads the edgelist
G = nx.read_edgelist("web.mtx",create_using=nx.DiGraph(),nodetype=int)

#Creates a dictionary to store the number of times a node is visited
count_list = {}
for itm in G.nodes():
	count_list[itm] = 0

#walk length must be very large compared to the number of edges
walk_length = (len(G.edges()))*1000

#Performs random walk
count_list = random_walk(G,walk_length,random.choice(list(G.nodes())),count_list)

#Sorts nodes in decreasing order of their visiting
count_list = sorted(count_list.items(), key=lambda x:x[1], reverse=True)

#Computes page rank using the inbuilt pagerank function
predefined_pagerank = nx.pagerank(G)

#Sorts nodes based on computed page rank
sorted_pagerank = {}
for item in predefined_pagerank:
    sorted_pagerank[item] = predefined_pagerank[item]
sorted_pagerank = sorted(sorted_pagerank.items(),key = lambda x:x[1], reverse=True)

my_pagerank = []
sorted_nodes = []
compare_nodes = []

#Compares between actual page rank and our random walk page rank
for item in count_list:
    my_pagerank.append(item[0])
for item in sorted_pagerank:
    sorted_nodes.append(item[0])
for i in range(len(sorted_nodes)):
    compare_nodes.append([my_pagerank[i],sorted_nodes[i]])

nx.draw(G,with_labels=True)
plt.show()

count = 0
for item in compare_nodes:
    if item[0]==item[1]:
        count = count + 1
	
similarity_percentage = (count/len(compare_nodes))*100

print(compare_nodes)
print("The percentage of similarity is ",similarity_percentage)