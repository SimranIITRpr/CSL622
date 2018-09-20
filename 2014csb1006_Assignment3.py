#Name - A.Mamatha
#Entry Number - 2014CSB1006
# Calculating the pagerank - random walk
import networkx as nx
import random
import matplotlib.pyplot as plt

# The dataset used for calculating pagerank is web-Stanford.txt 
G=nx.read_edgelist("web-Stanford.txt",create_using=nx.DiGraph(), nodetype=int)  #Reading the text file 

'''G=nx.Graph()
for i in range(10):
	G.add_node(i)
								 #
i = 0                            # Created for generating a basic graph
								 #
for i in range(10):
	for j in range(10):
		if(random.random()>0.5):
			G.add_edge(i,j)
#nx.draw(G,with_labels=1)
#plt.show(G)

'''

def teleport(randNode):          # Function to move from one node to another randomly 
	if(random.random()<0.2):
		return random.choice(list(G.nodes))
	else:
		return randNode


randNode = random.choice(list(G.nodes))  # choosing a random node from a list of nodes
dictionary={}    # created a dictioanry 
for i in G.nodes():
	dictionary[i]=0

for i in range(1,100000):			# More no. of iterations for less error
	randNode=teleport(randNode)              
	if(len(list(G.neighbors(randNode)))!=0):
		randNode=random.choice(list(G.neighbors(randNode)))
	else:
		break
	dictionary[randNode]+=1

for key, value in sorted(dictionary.iteritems(), key=lambda (k,v): (v,k)):  # sorting the values for knowing the pagerank
	print "%s: %s" % (key, value)											# by using the algorithm 

for key, value in sorted(nx.pagerank(G).iteritems(), key=lambda (k,v): (v,k)):  # sorting the values for knowing the pagerank
	print "%s: %s" % (key, value)												# by using the inbuilt function for comparison