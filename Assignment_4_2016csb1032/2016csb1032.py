import networkx as nx 
import matplotlib.pyplot as plt 
import random

def distance_matric_creator(G): # CREATES THE SHORTEST PATH LENGTH MATRIX WITH (NODE1.NODE2) = SHORTEST DISTANCE BETWEEN THEM
	p=nx.shortest_path(G)
	distance_matrix={}
	for i in p:
		node1=int(i)
		for j in p[i]:
			if i!=j:
				node2=int(j)
				shortest_distance=len(p[i][j])-1
				if (node2,node1) not in distance_matrix:
					distance_matrix[(node1,node2)]=shortest_distance

	# for i in sorted(distance_matrix.iteritems(),key=lambda x:x[1],reverse=True):
	# 	print i[0],i[1]
	return distance_matrix

def comparator(G):  # CALULATING THE EGDE WITH HOGHEST BETWEENESS
	edge_betweeness_list={}
	distance_matrix_before=distance_matric_creator(G)

	for i in G.nodes():
		for j in G.nodes():
			if i!=j and G.has_edge(i,j) and ((int(j),int(i)) not in edge_betweeness_list):
				G.remove_edge(i,j)
				if G.has_edge(j,i):
					print "==================ERROR 2 ====================="
				distance_matrix_after=distance_matric_creator(G)
				difference={}

				for k in distance_matrix_after:
					difference[k]=distance_matrix_after[k]-distance_matrix_before[k]
				
				edge_betweeness_list[(int(i),int(j))]=0
				divisor=1
				for k in difference:
					if difference[k]>0:
						edge_betweeness_list[(int(i),int(j))]+=1
					if difference[k]<0:
						print "==================ERROR====================="
					divisor+=1
				if divisor>1:
					divisor-=1
				
				edge_betweeness_list[(int(i),int(j))]=float(edge_betweeness_list[(int(i),int(j))])/divisor
				G.add_edge(i,j)

	edge_betweeness_list=sorted(edge_betweeness_list.iteritems(),key=lambda x:x[1],reverse=True)
	
	if len(edge_betweeness_list)>=1:
		if len(edge_betweeness_list[0])>=2:
			return edge_betweeness_list[0][0],edge_betweeness_list[0][1]
	else:
		return (-1,-1),-1 # Sending Error valeues to check
def communities(G,key): # COMMUNITY ALLOCATION ON BASIS OF KEY / SPLIT
	node1=int(key[0])
	node2=int(key[1])
	G.remove_edge(node1,node2)

	comm1=[]
	comm2=[]
	ncomm=[]
	print "COMMUNITIES_BY:",node1,node2
	for i in list(G.nodes()):
		l1=[]
		l2=[]
		if nx.has_path(G,i,node1):
			l1=nx.shortest_path(G,i,node1)
		if nx.has_path(G,i,node2):
			l2=nx.shortest_path(G,i,node2)	
		if len(l1)>len(l2):
			comm1.append(i)
		elif len(l2)>len(l1):
			comm2.append(i)
		else:
			ncomm.append(i)
	
	while(len(ncomm)!=0):     # IF NODES EXSIST WHICH NEUTRAL TOWARDS OUR SPILT THEN CHOOSE RANDOMLY NODE FROM EITHER COMMUNITY AND ALLOCATE THEM COMMUNITY
		node_alloc=ncomm.pop(0)
		node1_alloc=random.choice(comm1)
		node2_alloc=random.choice(comm2)
		if nx.has_path(G,node_alloc,node1_alloc):
			l1=nx.shortest_path(G,node_alloc,node1_alloc)
		if nx.has_path(G,node_alloc,node2_alloc):
			l2=nx.shortest_path(G,node_alloc,node2_alloc)
		if len(l1)>len(l2):
			comm2.append(node_alloc)
		else:
			comm1.append(node_alloc)			

	all_communities=[]				
	all_communities.append(comm1)
	all_communities.append(comm2)
	return all_communities

def recurse(G,comm_limit):  # RECURSIVE CALLS TO FORM COMUNITIES
	if comm_limit<=0:
		return
	else:
		comm_limit-=1

	key,value=comparator(G)
	if value==-1:
		return
	print '\n',"MAX_EDGE_BETWEENESS_FOUND_FOR:",key
	all_comms=communities(G,key)
	print "COMMUNITIES_FOUND_DUE_TO_SPLIT_THROUGH:",key," ; SPLIT_LEVEL:",comm_limit+1,'\n'
	Graph_ar=[]
	das=1
	for i in all_comms:
		print "COMMUNITY ",das,' : ',i
		das+=1
		Graph_ar.append(G.subgraph(i))
	
	for i in Graph_ar:
		if len(i)<=1:
			continue
		j=nx.Graph(i)
		if nx.is_frozen(j):
			print "FROZEN_ERROR"
			continue
		recurse(j,comm_limit)


def main():
	comm_limit=1 # CURRENT COMMUNITY DIVIDER 
	G=nx.karate_club_graph()
	recurse(G,comm_limit)
	nx.draw(G,with_labels=True)
	plt.show()

main()
