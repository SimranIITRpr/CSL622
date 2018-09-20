import networkx as nx
import random
import matplotlib.pyplot as plt

#
'''
     Author: Pankaj Verma
     Date : 06 September 2018
    
     Required python packages: networkx

     Required dataset link : https://snap.stanford.edu/data/wiki-Vote.html
  
'''
def Random_Walk(input_graph_file):
	
	G = nx.read_edgelist(input_graph_file,create_using=nx.DiGraph(), nodetype = int)
   
	n = G.number_of_nodes()
	print(n)
    
	itr = 10000
	l={}
	for i in list(G.nodes()):
		l[i]=0;

	random_node = random.choice(list(G.nodes())) ## choose a random starting node for random walk

	for j in range(1,itr+1):
		curr_node = random_node
		l[curr_node] = l[curr_node] + 1
		x=random.random()
		if (x >= 0.8): # go to neighbour node
			N = list(G.neighbors(curr_node))
			ln = len(N)
			if ln != 0:
				random_node = random.choice(N)
			elif ln==0:
				random_node = random.choice(list(G.nodes()))
		elif(x <= 0.2) :
			random_node = random.choice(list(G.nodes()))		
	
	
	
	
	ndlst = list(l.keys())
	vstslst = [l[x] for x in ndlst]
	pageRank = nx.pagerank(G) 
	rankval = [500*pageRank[x] for x in ndlst] 
	plt.plot(ndlst,vstslst,'b--', ndlst, rankval , 'r--')

if __name__ == "__main__":
	input_graph_file = "Wiki-Vote.txt"
	Random_Walk(input_graph_file)

