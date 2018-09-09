import networkx as nx						#importing networkx
import random							#importing random integer

g = nx.read_edgelist("web-NotreDame.txt", create_using=nx.Graph(), nodetype=int)

trackList= []							#Keeps the track of the count of the walk.
nodes = len(g.nodes())
for i in range(nodes):						#Initialising the list with 0.
	trackList.append(0)

start = random.randint(0,nodes-1)				#Generating the random number for starting the walk.

for j in range(100000):						#Iterating n times.
	while(start not in g.nodes()):
		#print "Hello"
		start = random.randint(0,nodes-1)
	#print "Hi"
	#neigh = g.neighbors(start)
	neighbour = [n for n in g.neighbors(start)]		#Getting the list of the neighbours of the node.
	trackList[start]+=1					#Incrementing the count of the visited nodes.
	pp = random.randint(0,10);				#Generating the random integer between 0 and 9. If the value is 0 or 1 then move to a random node otherwise go to the neighbour. This ensures that the probability of teleporting is 0.2.
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

for pr in tup:
	print pr[0],'=',pr[1]					#Printing the result.
print "Pagerank given by the inbuilt function."
t = nx.pagerank(g, alpha=0.2)					#Getting the inbuilt pagerank.
print t
list1 = []
for i in range(len(g.nodes())):
	list1.append(t[i])
plt.plot(list1,trackList)					#Plotting the data.
plt.show()
