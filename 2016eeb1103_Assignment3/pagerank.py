import networkx as nx						#importing networkx function
import random							#importing random function

g = nx.read_edgelist("web-Google.txt") 				#reading dataset obtained from "https://snap.stanford.edu/data/web-Google.html"

trackList= []							#Keeping track of the count of the walk.
nodes = len(g.nodes())
for i in range(nodes):						#Initialising list with 0.
	trackList.append(0)

start = random.randint(0,nodes-1)				#Generating the random number for starting the walk.

for j in range(100000):						#Iterating given times.
	while(start not in g.nodes()):
		start = random.randint(0,nodes-1)
	neighbour = [n for n in g.neighbors(start)]		#Getting list of the neighbours of the node.
	trackList[start]+=1					#Incrementing the count of the visited nodes.
	pp = random.randint(0,10);				#Generating the random integer between 0 and 9. If the value is 0 or 1 then move to a random node otherwise go to the neighbour. This ensures that probability of teleporting is 0.2.
	if pp<2 or len(neighbour)==0:				#If the random number is 0 or 1.
		 start = random.randint(0,nodes-1)		#Teleporting to a random node.
		 continue
	else:	
		x = random.randint(0,len(neighbour)-1)		#Moving to one of the neighbouring node.
	start = neighbour[x]					

no=[]
for i in range(nodes):						#Printing the obtained result.
	no.append(i)

tup = zip(no,trackList)
tup.sort(key=lambda x: x[1])					#Making the dictionary of the result.

for ut in tup:
	print ut[0],'=',ut[1]					#Printing the result.

	
print "PageRank using inbuilt function :"

u = nx.pagerank(g,p=0.2)					#using pagerank inbuilt function
list = []
for i in range(len(g.nodes())):
	list.append(u[i])
plt.plot(list1, tracklist)					#plotting manual and inbuilt functions on a graph
plt.show()							#displaying graph
