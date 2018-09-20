import networkx as nx					#Importing the packages.

g = nx.Graph()						#initialising the graph.

file = open("subj.txt","r")				#opening the data file
mat = []
for line in file:					#Taking every line of the file.
	flag = 0
	listSub = []
	for num in line.split(" "):			#Splitting every line and getting the data.
		node = int(num)		
		if flag == 0:
			flag = 1
			g.add_node(node)		#Adding the node.
		else:
			listSub.append(node)	
	count = 0
	vertex1 = 0
	for lists in mat:
		count = 0
		vertex1+=1
		for i in range(len(listSub)):
			if listSub[i] ==1 and lists[i]==1:
				count+=1
		if(count == 0):
			continue
		else:
			g.add_edge(vertex1,len(mat)+1,weight = count)
	mat.append(listSub)

def printPath(g,i,j):						#Finding the shortest path
	paths = nx.all_shortest_paths(g,i,j)			#Finding all the shortest path between the two points.
	count2 = 0
	listL = []
	for p in paths:						#Counting the total number of paths.
		count2+=1
		listL = p
	if(count2==1):						#Base condition for the recurrance.
		for k in listL:
			print str(k) + " ",
		return
	else:
		res = []
		maxWeight = -1
		index1 = 0
		index2 = 0
		paths = nx.all_shortest_paths(g,i,j)
		for l in paths:
			weightNode = g[l[0]][l[1]]['weight'] 		#Finding the weight of the given edge.
			if weightNode>maxWeight:			#Choosing the least weight path greedily.
				index1 = l[0]
				index2 = l[1]
				maxWeight = weightNode
		print str(index1) + " " ,				#Printing the next best path.
		printPath(g,index2,j)

for i in g.nodes():							#Finding the best possible path for each pair of node.
	for j in g.nodes():
		if i == j:						#If the source is same as destination.
			continue
		else:
			paths = nx.all_shortest_paths(g,i,j)		#Finding all the shortest path between the pair of points.
			count2 = 0
			listL = []
			for p in paths:
				count2+=1
				listL = p
			if(count2==1):					#Printing the path.
				print "Source:" + str(i)+" dest:"+str(j) + "   Path : [",
				for k in listL:
					print str(k) + " ",
				print "]"
			else:
				print "Source:" + str(i)+ " dest:" +str(j) + "   Path : [",
				printPath(g,i,j)
				print "]"
