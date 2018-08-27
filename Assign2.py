"""

 @ Author : Allu Krishna Sai Teja(2015csb1005) & N Nikhil (2015csb1020)
The code builts upon Change_the_leader_position.py by @author: Meghana Batchu(2016csb1034), Sainath Thota(2015csb1037), Yugandhar Bandi(2015csb1009)
 In that problem they find the minimum ranked node to remove to change ..
the leader in the graph what we did was we changed the problem statement to finding minimum number of new connections needed .. 
to make a given node 'x' to become the leader of the graph . we do this adding new connection between the given x and node ..
with highest pagerank if it doesnot become leader we do the same with next node with highest page rank and so on until we make ..
the given node 'x' the leader of the graph.
 

"""

import networkx as nx
import string
import matplotlib.pyplot as plt
import operator




def getKey(item):
    return item[1]


def Cal_Leader(Dictionary_of_pageranks):
    maximum_page_rank = 0
    leader = -1
    for each in Dictionary_of_pageranks.items():
        if(each[1]>maximum_page_rank):
            maximum_page_rank = each[1]
            leader = each[0]
    return leader



def Number_of_Edges_to_be_added(G,x) :
    
    D = nx.pagerank(G)
    flag_for_break = 0;
    sorted_D = sorted(D.items(), key=operator.itemgetter(1),reverse=True)
    H = G.copy()
    ans=0
	
    CLeader = Cal_Leader(D) 


    for each in sorted_D :
    
        if x== CLeader :
            flag_for_break = 1
            break
        if (each[0]!=x):
            y=each[0]
            if (~H.has_edge(x,y)):
                H.add_edge(x,y,weight=1)
                ans=ans+1
        
            if (~H.has_edge(y,x)):
                H.add_edge(y,x,weight=1)
                ans=ans+1
        
            D1 = nx.pagerank(H)
            new_leader = Cal_Leader(D1)
            if(new_leader == x):
                flag_for_break = 1
                break
            D1.clear()
        
    if flag_for_break ==1 :
        print("The number of connections to be added for node no "+ str(x)+ " to be leader is "+str(ans/2))
    else :
        print("Not Possible")
    
    

G = nx.read_edgelist("pagerank.txt",create_using=nx.DiGraph(), nodetype=int)
"""
Change the value of x to your required node that you want to become leader.
"""
x=31
Number_of_Edges_to_be_added(G,x)
