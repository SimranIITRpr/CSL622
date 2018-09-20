"""
Assignment-2(improving 2014csb1037 assignment-1)
@author: Meghana Batchu(2016csb1034), Sainath Thota(2015csb1037), Yugandhar Bandi(2015csb1009)

"""
#Initial question is to give recommendations based on number of paths when searched for a particuler person.There can be many nodes with the same person name,as we do in fb.
#The improved question is that we will give the recommendations to a person according to the number of paths to different persons and giving weights to each path according to the length. Here we are going to a depth of 5 hops


import networkx as nx
def getKey(item):
    return item[1]


X=nx.read_adjlist("pagerank.txt",nodetype=int, create_using=nx.DiGraph())
L = []
src = 1;
for each in nx.non_neighbors(X,src):
	L.append(each)

non_neighbour_tuple = ()
for each in range(len(L)):
	sum1 = 0;
	for i in range(5):
		for path in nx.all_simple_paths(X,source = src,target = L[each],cutoff = i ):
			sum1 = sum1 + len(path)*(6-len(path))
	non_neighbour_tuple = non_neighbour_tuple+((L[each],sum1),)

sorted_non_neighbour_tuple = sorted(non_neighbour_tuple, key=getKey)
#print(sorted_non_neighbour_tuple)
print ("The order of non friend recommendations at a depth of maximum 5 is : ")
for var in range(len(sorted_non_neighbour_tuple)):
	print (sorted_non_neighbour_tuple[var][0])

