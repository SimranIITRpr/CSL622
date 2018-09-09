0import networkx as nx
import random
import operator
#Data Set Downloaded from http://snap.stanford.edu/data/web-Stanford.html
DG = nx.read_edgelist("web-Stanford.txt",create_using=nx.DiGraph(), nodetype = int)
nodes=DG.number_of_nodes()
tp=0.2 # teleport probablility 
visit_counter = dict() # maps a node to number of times it gets visited
vertex=random.randrange(1,nodes+1,1)
itr=10**5 # fix 10^5 iterations for random walk 
for i in range(1,itr) :
   rand_numb = random.random()
   if visit_counter.has_key(vertex):
      visit_counter[vertex]=visit_counter[vertex]+1;
   else :
      visit_counter[vertex]=1;	
   nbds= list(DG.neighbors(vertex))
   if rand_numb>=tp and len(nbds)>0:
      vertex=random.choice(nbds)
   else :
	    vertex=random.randrange(1,nodes+1,1)
for i in range(1,nodes+1):
     if not visit_counter.has_key(i):
	  visit_counter[i]=0 # for remaining non visited nodes
Rand_walk_tupple=sorted(visit_counter.items(), key=operator.itemgetter(1),reverse=True) #sort the visited counter to get the ranks
Rand_walk_rank = [x[0] for x in Rand_walk_tupple]
page_rank=nx.pagerank(DG)
Page_walk_tupple=sorted(page_rank.items(), key=operator.itemgetter(1),reverse=True)
Page_rank = [x[0] for x in Page_walk_tupple]
print "Rank from RandWalk-Rank from Page Rank For top 50 nodes"
for i in range(0,50):
    print str(Rand_walk_rank[i])+" "+str(Page_rank[i])