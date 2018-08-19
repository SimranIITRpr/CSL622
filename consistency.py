
""" 
Q. Find the most conistent node with maximum in-degree & out-degree centrality ? 
Q. Find the assortativity index of the graph. 
Q. Next, we investigate how assortativity index is related to degree-centrality ? 
   Observation: By the removal of most-consistent node, the assortativity index increases !!   

%====================================================
Group Memebers:
Amit Kumar Chauhan (2017csz0008) 
Abhishek Kumar (2017csz0009) 

This is a temporary script file.
"""

import networkx as nx
import numpy as np 
import matplotlib.pyplot as plt

DG = nx.read_edgelist("pagerank.txt", "r", create_using=nx.DiGraph(), nodetype = int) 

#nx.draw(DG,with_labels=1) 


# Node with Maximum sum of in-degree and out-degree centrality 

print(nx.in_degree_centrality(DG)) 

print(nx.out_degree_centrality(DG))  


list_1 = list(nx.in_degree_centrality(DG).values())
list_2 = list(nx.out_degree_centrality(DG).values()) 

list_3 = [(x + y) for x, y in zip(list_1, list_2)] 
print (list_3)  

#print("Maximum of the sum of In-degree and Out-degree centrality is : ", max(list_3)) 

# Node with maxcimum sum of in-degree and out-degree 

"""
print (DG.in_degree)  
print (DG.out_degree)
print (DG.degree)  
print (sorted(DG.degree, key = lambda x:x[1], reverse= 1))

"""

degree_sequence = sorted(DG.degree, key = lambda x:x[1], reverse= 1)
#print ("Node with maximum in-degree+out-degrere is :", degree_sequence[0:1]) 

print("The most consistent node having maximum total degree & centraility is :", degree_sequence[0:1], max(list_3)) 
print("The assortativity Index is :", nx.degree_assortativity_coefficient(DG)) 

nx.draw(DG,with_labels=1) 
plt.show() 

DG.remove_node(1)  

nx.draw(DG,with_labels=1) 
plt.show() 
print("The assortativity Index is :", nx.degree_assortativity_coefficient(DG)) 

