'''
s.shiva 2014csb1037

prob:
    if ramesh searches for someone named suresh in facebook and there are a 
number of accounts named suresh and we have to show him the results in the 
order of how closely the ramesh and some account named suresh are related
we can calculate the closeness by calculating number of hops(or distance) 
between them but what if 2 sureshs are in the same distance from ramesh
lets say 3 hops which suresh do we show first

sol:
    we can resolve this  problem using score of strongness that means how 
strongley a node is connected to another we can calculate this by calculating
number of paths between them i am calculating the score as follows:
    score_of_strongnesss=number of paths between the nodes of length 1 *10+
                         number of paths between the nodes of length 2 *9+
                         number of paths between the nodes of length 3 *8+
                         number of paths between the nodes of length 4 *7

'''
import networkx as nx
X=nx.read_adjlist("pagerank.txt",nodetype=int, create_using=nx.DiGraph())
def scoreofstrongness(sors,targ):
 z=0
 for i in range(3):
  paths = nx.all_simple_paths(X, source=sors, target=targ, cutoff=i+1)
  lpaths = nx.all_simple_paths(X, source=sors, target=targ, cutoff=i)
  z=z+((len(list(paths))-len(list(lpaths)))*(10-i))
 return z
#eg:
print(scoreofstrongness(2,33))