#finding the leader node in the out neighbours of any random node
#Group:
#Chintala Tejaswini 2016csb1036
#Aluvala Mamatha 2014csb1006
import networkx as nx
import matplotlib.pyplot as plt
from random import choice

X = nx.read_adjlist("pagerank.txt",nodetype=int,create_using=nx.DiGraph())
#print X.nodes()
#print X.edges()

random_node=choice(list(X.nodes()))

print "Random_Node:"+str(random_node)+"\nOut_Neighbors:"
print X.neighbors(random_node)

l=nx.pagerank(X)
maxnode = X.neighbors(random_node)[0] 
for i in X.neighbors(random_node):
	if(l[maxnode] <l[i] ):
		maxnode = i
print "Leader in the out neighbours:"+str(maxnode)
