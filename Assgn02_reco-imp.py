"""
CSL622: Assignment-02 

"""

"""
==============================================================================
Q. How to suggest the recommendation for any two people to become friends ? 
Q. How to check how much one person is impressed by other person ? 

==============================================================================
"""

"""
Contributors :
    Amit Kumar Chauhan (2017csz0008)  
    Abhishek Kumar (2017csz0009)

=============================================================
"""

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import math


# Function to find the intersection of two lists.
def Intersection(lst1, lst2):
    return set(lst1).intersection(lst2)


# Function to decide recommendation.
def Friend_Reco():
    print ("Enter any two nodes from 1 to " + str(N))
    x, y = [int(x) for x in input().split()]
    if (G.has_edge(x, y) == True):
        print("Node " + str(x) + " and Node " + str(y) + " are already friends!")
    else:
        s = F_arr[i-1,j-1]
        if(s >= avg):
            print("Node " + str(x) + " and Node " + str(y) + " are recommonded as friends !")
        else:
             print("Node " + str(x) + " and Node " + str(y) + " are not recommonded as friends !")
           
def Imp_Pre():
    print ("Enter any two nodes from 1 to " + str(N))
    x, y = [int(x) for x in input().split()]
    if (G.has_edge(x, y) == True):
         print("Node " + str(x) + " is impressed with node "  + str(y) + "!")
    else:
        s = I_arr[i-1,j-1]
        if(s >= avg1):
            print("Node " + str(x) + " will impress node "  + str(y) + " highly likely!")
        else:
             print("Node " + str(x) + " will not impress node "  + str(y) + " highly likely!")
   

#Creating the graph from .txt file.
G = nx.read_edgelist(r"pagerank.txt",create_using=nx.Graph(), nodetype = int)
nx.draw(G, with_labels = 1)
#plt.show()



# Getting the order of the graph.
N = G.order() 
#print (G.order())


# Finding commong number of friends and average number of common friends.
F_arr = np.zeros((N,N));
avg = 0
count = 0
   
for i in range(1, N + 1):
    for j in range(i + 1, N + 1):  
        if (G.has_edge(i, j) == True):
            pass
            #print("Node" + str(i) + "and Node" + str(j) + "are friends !") 
        else:
            list1 = list(G.neighbors(i))
            list2 = list(G.neighbors(j))
            common_list = Intersection(list1, list2) 
            #print(common_list)
            avg = avg + len(common_list)
            count = count + 1
            #print (i, j, len(common_list))
            F_arr[i-1,j-1] = len(common_list);
                
avg = math.ceil(avg/count)
print (avg)


#Enter two nodes to check the status of recommondation.
#print ("Enter any two nodes from 1 to " + str(N))
#x, y = [int(x) for x in input().split()]
#1Friend_Reco()



H = nx.read_edgelist(r"pagerank.txt",create_using=nx.DiGraph(), nodetype = int)
nx.draw(H, with_labels = 1)
#plt.show()

# Finding commong number of friends and average number of common friends.
I_arr = np.zeros((N,N));
avg1 = 0
count1 = 0
   
for i in range(1, N + 1):
    for j in range(1, N + 1):  
        if (G.has_edge(i, j) == True):
            pass
            #print("Node" + str(i) + "and Node" + str(j) + "are friends !") 
        else:
            list1 = list(H.neighbors(i))
            list2 = list(H.neighbors(j))
            common_list = Intersection(list1, list2) 
            #print(common_list)
            avg1 = avg1 + len(common_list)
            count1 = count1 + 1
            #print (i, j, len(common_list))
            I_arr[i-1,j-1] = len(common_list);
                
avg1 = math.ceil(avg1/count1)
print (avg1)

print ("Enter 1 to check friend 'Recommondation' and 2 for 'Impression Prediction' :")
c = int(input()) 
if (c == 1): 
    Friend_Reco()
elif (c == 2): 
    Imp_Pre()  




