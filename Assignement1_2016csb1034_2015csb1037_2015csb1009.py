"""
@author: Meghana Batchu(2016csb1034), Sainath Thota(2015csb1037), Yugandhar Bandi(2015csb1009)
"""

#The question is that we find the smallest ranked number node on whose removal the leader (top person after application of page rank)changes its position


import networkx as nx
import string
import matplotlib.pyplot as plt
import operator

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


	
def analyzes(filename):
	'''
	This Function Basically is the Analysis of the Leader in the Network conditioning if Leader is not friend with his neighbourhood ,in Graph Theory we remove an edge from leader-->neighbour (if any) than check if leader has lost it's position or not
	We had done this analysis For 2 level deep (e.g. On the Leader's Friend and the Friend of leader's Friend)
	Usage:   
		>>> import leader_analysis
		>>> leader_analysis.analyzes("filename")

	NOTE: if any changes to file than simply reload the python script
	'''
	G = nx.read_adjlist(filename,create_using=nx.DiGraph(), nodetype=int)
	D = nx.pagerank(G)
	leader = Cal_Leader(D)
	print("INITIAL LEADER IS : "+str(leader))
	neighbours = [m for m in G[leader]]

	# THIS SECTION DEALS WITH REMOVAL OF A FRIENDSHIP FROM THE LEADER TO ONE OF HIS FRIENDS
	# WITH REMOVAL OF THE FRIENDSHIP, THE NEW LEADER IS CALCULATED AND ALSO THE RANKING OF THE OLD LEADER IS FOUND
	print("===============================================================================")
	print("REMOVAL OF SINGLE FRIENDSHIP FROM LEADER TO HIS FRIENDS ( BUT NOT VICE VERSA )")
	print("===============================================================================")
	for n in neighbours:
		H = G.copy()
		H.remove_edge(leader,n)
		new_D = nx.pagerank(H)
		new_leader = Cal_Leader(new_D)
	
		if ( leader != new_leader ):
			sorted_x = sorted(nx.pagerank(H).items(), key=operator.itemgetter(1),reverse=True)
			sorted_x = [i[0] for i in sorted_x]
			position = sorted_x.index(leader) + 1
			print("REMOVAL OF ("+str(leader)+","+str(n)+") : THE LEADER HAS CHANGED TO : "+str(new_leader)+" : NEW POSITION OF OLD LEADER : "+str(position))
		else:
			print("REMOVAL OF ("+str(leader)+","+str(n)+") : LEADER REMAINS THE SAME")

	# THIS SECTION DEALS WITH REMOVAL OF A FRIENDSHIP FROM ONE OF THE LEADER'S FRIEND TO THEIR FRIENDS i.e. FRIENDS OF LEADER'S FRIENDS
	# WITH REMOVAL OF THE FRIENDSHIP, THE NEW LEADER IS CALCULATED AND ALSO THE RANKING OF THE OLD LEADER IS FOUND
	print("===============================================================================")
	print("REMOVAL OF SINGLE FRIENDSHIP FROM LEADER'S FRIENDS TO THEIR FRIENDS ( BUT NOT VICE VERSA )")
	print("===============================================================================")
	for n1 in neighbours:
		fof = [m for m in G[n1]]
		print("--------------------------------------")
		print("FRIENDS OF : "+str(n1))
		print("--------------------------------------")
		for n in fof:
			H = G.copy()
			H.remove_edge(n1,n)
			new_D = nx.pagerank(H)
			new_leader = Cal_Leader(new_D)
	
			if ( leader != new_leader ):
				sorted_x = sorted(nx.pagerank(H).items(), key=operator.itemgetter(1),reverse=True)
				sorted_x = [i[0] for i in sorted_x]
				position = sorted_x.index(leader) + 1
				print("REMOVAL OF ("+str(n1)+","+str(n)+") : THE LEADER HAS CHANGED TO : "+str(new_leader)+" : NEW POSITION OF OLD LEADER : "+str(position))
			else:
				print("REMOVAL OF ("+str(n1)+","+str(n)+") : LEADER REMAINS THE SAME")






	
