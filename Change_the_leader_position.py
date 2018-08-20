"""
@author: Meghana Batchu(2016csb1034), Sainath Thota(2015csb1037), Yugandhar Bandi(2015csb1009)
"""

#The question is that we find the smallest ranked number node on whose removal the leader (top person after application of page rank)changes its position


import networkx as nx
import string
import matplotlib.pyplot as plt


def getKey(item):
    return item[1]


def Cal_Leader(Dictionary_of_pageranks):
	maximum_page_rank = 0
	leader = -1
	for each in Dictionary_of_pageranks.items():
		if(each[1]>maximum_page_rank):
			maximum_page_rank = each[1]
			leader = each[0]
	return leader


G = nx.read_edgelist("pagerank.txt",create_using=nx.DiGraph(), nodetype=int)
D = nx.pagerank(G)
leader = Cal_Leader(D)
neighbour_tuple = ()
for each in nx.all_neighbors(G,leader):
	neighbour_tuple = neighbour_tuple+((each,D[each]),)
	
sorted_neighbour_tuple = sorted(neighbour_tuple, key=getKey)
flag_for_break = 0;
for var in range(len(sorted_neighbour_tuple)):
	H = G.copy()
	H.remove_node(sorted_neighbour_tuple[var][0])
	D1 = nx.pagerank(H)
	new_leader = Cal_Leader(D1)
	if(new_leader != leader):
		flag_for_break = 1
		break
	D1.clear()
	H.clear()


if(flag_for_break == 0):
	print ("Removing any single node doesn't affect the leaders position")
else:
	print ("Removing " + str(sorted_neighbour_tuple[var][0]) + " changes the leaders position")








	
