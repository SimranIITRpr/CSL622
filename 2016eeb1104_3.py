import networkx as nx
import matplotlib.pyplot as plt
import random as rand
#Imported a data file from stanford website
input_graph_file = 'web-BerkStan.txt'

# Reading Graph from given data file
G = nx.read_edgelist(input_graph_file,create_using=nx.DiGraph(), nodetype = int)
# V makes list of all the nodes in G
V= list(G.nodes())
# n stores the total number of nodes present.
n=len(V)
# count makes an array of size (n+1) since numbering starts from 1 to n+1.
count=[0]*(n+1)
# It randomly chooses a node from V.
start = rand.choice(V)
# It increments the count of chosen node.
count[start]=count[start]+1
# t is teleportation probability.
t=0.2
# This for loop walks through all the nodes and jumps to random node with teleportation
# probability t and stores the count in count array.
for i in range(1000000):
	x=rand.random()
	if x<t:
		start=rand.choice(V)
		count[start]=count[start]+1
	else:
		N=list(G.neighbors(start))
		if len(N) == 0:
			start=rand.choice(V)
			count[start]=count[start]+1
		else:
			start=rand.choice(N)
			count[start]=count[start]+1
P=[]
# This for loop stores the count value with its index in P.
for i in range (1,n+1):
    P.append( (count[i],i) )
# We sort the array P. 
P=sorted(P)
print(P)
Rank_by_RW=[]
# Now we store our sorted array P in Rank_by_RW
for i in range (0,n):
    Rank_by_RW.append(P[i][1])
Y=[]
Z=[]
# To compare our algorithm with pagerank algorithm, we store page rank
# algorithm result in Z.
Y=nx.pagerank(G, alpha=t)
for i in Y:
	Z.append((Y[i],i))
# We Sorted the page rank algorithm result so that we can compare it with our result. 
Z=sorted(Z)
print(Z)
Rank_by_PageRank=[]
# Now we store page rank algorithm array Z in Rank_by_PageRank
for i in range (0,n):
    Rank_by_PageRank.append(Z[i][1])

# Now we plot our algorithm of random walk versus in algorithm of in build function PageRank
# We want a straight line for our algorithm to be accurate.
plt.plot(Rank_by_RW,Rank_by_PageRank,'bo')
plt.title("Compare ranking method")
plt.xlabel("My random walk algorithm")
plt.ylabel("Page rank algorithm")
plt.show()
	
