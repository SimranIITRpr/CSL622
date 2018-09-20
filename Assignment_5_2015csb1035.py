####################################################################
# NAME 			- SOUMYADEEP ROY
# ENTRY NO 		- 2015CSB1035
# DATASET USED 	- subj.txt
####################################################################

import networkx as nx
import string
import matplotlib.pyplot as plt
import operator
import numpy

###### FUNCTION USED

## THIS FUNCTION EXTRACTS THE SHORTEST PATHS FROM SOURCE A TO DESTNATION B
#  USING THE APPROACH PROVIDED BASED ON WEIGHT IN BETWEEN NODES

def shortest_paths(all_short_paths,strength,k):
	## VARIABLES
	# all_short_paths  	= all posiible shortest paths in between two nodes
	# strength 			= the weight matrix in between two nodes for all nodes
	# k 				= position in shortest path such that weight in between k and k-1 position is to be seen
	max_weight = 0	# Maximum weight in between a node and its neighbour
	temp = []		# Stores a list of all shortest paths between two nodes

	## (This loop gets the maximum weight in between two position)
	#   Therefore lets say all shortest paths between 1 and 5 is of length 4
	#   Lets say [ 1  2  3  5 ] [ 1  4  6  5 ] [ 1  7  8  5 ] are shortest paths
	#   Now the lets say k = 2
	#   Therefore weight in between [1,2] , [1,4] and [1,7] is seen
	#   Weights => [1,2] = 3  [1,4] = 3  [1,7] = 2
	#   Therefore max_weight = 3
	for path in all_short_paths:
		if ( strength[path[k-1]-1][path[k]-1] > max_weight ):
			max_weight = strength[path[k-1]-1][path[k]-1]

	## (This loop gets all the shortest paths in which weight is maximum for position k and k-1 in path)
	#   Therefore from previous example paths chossen for k = 2
	#   [ 1  2  3  5 ] and [ 1  4  6  5 ] since [1,2] = [1,4] = 3 = max_weight
	#   [ 1  7  8  5 ] discarded since [1,7] = 2 < max_weight
	for path in all_short_paths:
		if ( strength[path[k-1]-1][path[k]-1] == max_weight ):
			temp.append(path)

	return temp


###### MAIN PROGRAM

## VARIABLES
file = ""				# File read
line = ""				# Line in file
details = []			# A list that contains the list of lines in file where each character is seperated for a line
rows_no = 0				# No of lines in file
column_no = 0			# No of individual characters in a line
strength = []			# Weight matrix in between two nodes for all nodes
value = 0				# Helps calculate weight in between two nodes
path_length = 0			# Length of shortest path in between two nodes
all_short_paths = []	# A list that contains all the shortest paths in between two nodes

## READING FILE
file = open("subj.txt","r")

## GETTING DETAIL FROM FILE
for line in file:
	details.append(line[:-1].split(' '))

# ( updating values of variables )
rows_no = len(details)
column_no = len(details[0])
strength = [ [ 0 for i in range(0,rows_no,1)] for i in range(0,rows_no,1)]

## GETTING THE STRENGTH (WEIGHT) MATRIX
for i in range(0,rows_no-1,1):
	for j in range(i+1,rows_no,1):
		value = 0

		for k in range(1,column_no,1):
			if ((details[i][k] == '1') and (details[i][k] == details[j][k])):
				value = value + 1

		strength[i][j] = value
		strength[j][i] = value
		value = 0


for i in range(0,rows_no,1):
	print(strength[i])

## CREATING GRAPH
G = nx.Graph()

## ADDING EDGES
#  This is done by adding edges in between nodes where weight is non zero
for i in range(0,rows_no,1):
	for j in range(i+1,rows_no,1):
		if (strength[i][j] != 0):
			G.add_edge(i+1,j+1)

## GETTING THE SHORTEST PATHS IN ACCORDANCE TO THE METHOD PROVIDED
# This loop gets source node
for i in range(0,rows_no,1):
	# This loop gets destination node
	for j in range(0,rows_no,1):
		if ( i != j ):

			# (Get all the shortest paths without weight factor and also the length of shortest path)
			all_short_paths_ob = nx.all_shortest_paths(G,i+1,j+1)
			all_short_paths = [p for p in all_short_paths_ob]
			path_length = nx.shortest_path_length(G,source=i+1,target=j+1) + 1

			# ( For each position in path get the shortest path based on procedure given)
			for k in range(1,path_length,1):
				all_short_paths = shortest_paths(all_short_paths,strength,k)

			# DISPLAY
			print("NODE => "+str(i+1)+" : "+str(j+1)+" || PATH => ")
			for p in all_short_paths:
				print(p)
			print("===================================================")

# GRAPH DRAW
nx.draw(G,with_labels = True)
plt.show()

