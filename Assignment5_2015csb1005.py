import networkx as nx
import operator
# this is recursion for DFS
def Rec(v,parent,p,required):
	parent[v]=p
	sort_tuple=sorted(G[v].items(), key=operator.itemgetter(1),reverse=True) #sort the neighbors by weights
	# first I will take the maximum weight neighbor
	sort_list=[x[0] for x in sort_tuple]
	for i in sort_list: 
		if i not in parent:
			Rec(i,parent,v,required)
# This will initiate DFS			
def DFS(v,parent,required):
	Rec(v,parent,-1,required)
#store input in this variable
input=[]
with open('subj.txt') as f:
	for line in f:
		input.append(line.split(" "))
#Creating the graph
G = nx.Graph()
for i in range(0,len(input)):
	for j in range(i+1,len(input)):
		inp1=input[i]
		inp2=input[j]
		count=0
		for k in range(1,len(input[i])):
			if int(inp1[k],10)==int(inp2[k],10) and int(inp1[k],10)==1:
				count=count+1
		if count!=0:		
			G.add_edge(i, j, weight=count)
for i in range(0,len(input)):
		for j in range(i+1,len(input)):
			path=[]
			dest=j
			#if destination is a neighbour of source then it is the best path
			if dest in G.neighbors(i):
				path=[i+1,j+1]
			else: #we there might be multiple paths from source to destination
				  #I will proceed with DFS considering first the neighbor with max weight
				  #as neighbor and recursively proceed with the node until I reach my destination node
				  #If I am stuck somewhere(i.e I reach an end (no further path) I will backtrack to the previous node on the stack)	
				#This parent stores the parent of each visited node in DFS
				#Also to avoid cycles I keep a parent array to avoid revisiting the same node again
				parent={}
				DFS(i,parent,j)
				while parent[j]!=-1:# append to the path until we reach the source
					path.append(j+1)
					j=parent[j]
				path.append(i+1)
				path.reverse()
			print "Best path from  "+" "+str(i+1)+" "+str(dest+1)+" "+str(path)