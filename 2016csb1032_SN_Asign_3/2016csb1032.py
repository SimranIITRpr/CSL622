import matplotlib.pyplot as plt
import networkx as nx 
import random as rd


def random_path(G,cwl,show_teleport):  # CRAWLS THE GRAPH BY TAKING RANDOM PATHS GENERATED FROM RANDOM NODES WITH PROBABILITY OF 0.2
	dictionary={} # Containging key=node , value=times visited while crawling in total
	temp=list(G.nodes())
	for i in temp:
		dictionary[i]=0 # Setting initial values to 0

	for i in range(0,cwl):  # Max Random Nodes that can be chosen to Crawl the  Graph
		
		rand_node=rd.choice(list(G.node())) 
		dictionary[rand_node]+=1  
		

		crawl_probability=rd.uniform(0,1)  # A number uniformly chosen between (0,0.2) from (0,1) has probability = 0.2

		while(crawl_probability>0.2):  # Crawls with probability 0.8
			if show_teleport:
				print "\n","Crawling_from_selected_node_with_P:",crawl_probability,"-----------------" # Probability of CRAWLING BECOMES 0.8
			rand_node=rd.choice(list(G.neighbors(rand_node)))
			dictionary[rand_node]+=1

			# Exit while loop to Choose a new node with probability 0.2 or continue crawling with probability 0.8

			crawl_probability=rd.uniform(0,1)

		if show_teleport:
				print "\n","-------------Teleporting_to_random_node_with_P:",crawl_probability	# Probability of TELEPORTING BECOMES 0.2

	max_til=0  # Higest Page Rank Calculated
	max_node=-1;	# Higest Page Rank Node

	total_visit=0
	for i in dictionary:
		total_visit+=dictionary[i]  

	print "\nCALCULATED_NODE_VISIT_RATIO_THROUGH_RANDOM_WALK_WITH_TELEPORT_PROB_OF_0.2:\n"
	rank=1
	for i in sorted(dictionary.iteritems(),key=lambda (k,v):(v,k),reverse=True): # sorted(mydict.iteritems(), key=lambda (k,v): (v,k)):
		if i[1]>0:
			print "NODE:",i[0],"	CAL_RANK:",rank,"	VISITED",i[1],"	PRECENTAGE-OF-TOTAL-VISITS:",float(i[1])/total_visit,"%";
			rank+=1
		if i[1]>max_til:
			max_til=i[1]
			max_node=i[0]

	print "\n","HIGHEST_VISITED_NODE:",max_node," TIMES_VISITED:",max_til, " PERCENTAGE_OF_VISIT:",float(max_til)/total_visit,"%";

		
def Pagerank(G):
	 pr=nx.pagerank(G,alpha=0.9)
	 print "\n","RESULTS_FROM_BUILT IN PAGE_RANK_FUNCTION","\n"
	 rank=1
	 for i in sorted(pr.items(),key=lambda x:x[1],reverse=True):
	 	print "NODE:",i[0],"	ACTUAL_RANK:",rank,"	PAGERANK:",i[1]
	 	rank+=1

def Graph_maker(filename,cwl):
	G=nx.read_edgelist(filename) 
	random_path(G,cwl,show_teleport=False) 
	Pagerank(G)	


f=input("Enter_Filename[1] OR Default[0]:	")
if f==0:
	cwl=input("ENTER_WALK_LIMIT(different_walks)[1] OR DEFAULT(50000)[0]:	")
	if cwl==1:
		cwl=input("ENTER_WALK_LIMIT: ")
		Graph_maker('stanford_web_graph.txt',cwl)
	else:
		Graph_maker('stanford_web_graph.txt',50000)
else:
	name=input("Enter_Filename(with-in ' '):	")
	cwl=input("ENTER_WALK_LIMIT(different_walks)[1] OR DEFAULT(50000)[0]:	")
	if cwl==1:
		cwl=input("ENTER_WALK_LIMIT: ")
		Graph_maker(name,cwl)
	else:
		Graph_maker(name,50000)