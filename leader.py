########################Authors::::Soumyadeep Roy (2015csb1035)######################
########################::Shreyans Soni (2016csb1146)::######################
########################Date::::8/19/2018######################

#Libraries To import
import networkx as nx
import matplotlib.pyplot as plt


def find_the_leader(filename,threshold):
	'''This Function takes two parameters 1st the datafile_name(in the double qoutes)
	   and 2nd the threshold (e.g. 0.5,0.01,0.1)for finding the leader in the Network
	   Usage: 
	   >> import leader
	   >> leader.find_the leader("datafile_name",0.001)
	   
	   after changing the file just reload the file'''
	#Loading datafile as a Graph named 'G'
	G=nx.read_adjlist(filename,create_using=nx.DiGraph(),nodetype=int)

	nodes=list(G.nodes())
	edges=list(G.edges())
	length= len(nodes)

	#Maintaining Two separate Lists for the Markov_Chain

	#List containing all the 1's at the beggining which we will upadate in each itiration(basically these are the weights of the node in beggining)
	prev_val=[1.0 for i in range(0,length,1)]
	next_val=[0.0 for i in range(0,length,1)]
	flag = 0

	#Iterating through each node and then after getting all his neigbours we are flowing the current weight of that node equally to other neighbours of the node doing this unless we reach our threshold
	while(True):
		pos1 = 0
		pos2 = 0
		for i in range(0,length,1):
			node = nodes[i]
			pos1 = i
			connected = [m for m in G[node]]
			l = len(connected)
			for j in range(0,l,1):
				con = connected[j]
				for k in range(0,length,1):
					if (con == nodes[k]):
						pos2 = k
						break
				next_val[pos2] = next_val[pos2] + float(prev_val[pos1]/l)
		for l in range(0,length,1):
			diff = abs(next_val[l] - prev_val[l])
			if ( diff > threshold ):
				flag = 1
				break

		#You can uncomment these lines to get the list of distribution of weight
		#print(next_val)
		#print(sum(next_val))
		if (flag == 1):
			prev_val = [next_val[x] for x in range(0,length,1)]
			next_val = [0.0 for i in range(0,length,1)]
			flag = 0
		else:
			break

	max_val = next_val[0]
	max_pos = 0

	#Finding the Position of the Max weight in the List
	for i in range(0,length,1):
		if (next_val[i] > max_val):
			max_val = next_val[i]
			max_pos = i

	#Printing the max weight and node number (position)
	print("MAXIMUM VALUE : "+str(max_val))
	print("LEADER NODE : "+str(nodes[max_pos]))
