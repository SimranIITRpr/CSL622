#Assignment 4
#Piyush Pilaniya
#2016csb1049


import networkx as nx
import matplotlib.pyplot as plt
#Loading inbuilt Zachary Karate network
G=nx.karate_club_graph()
total_nodes=len(G) 

#function which returns a matrix where at each index is edge betweeness
def betweeness(G):
    counter_mat=list()  #A matrix to count the number of times an edge comes in shortest paths

     #total number of nodes in graph

    #creating a matrix of total_nodes*total_nodes with all entries zero
    i=0
    while(i!=total_nodes):
        row = list()
        j=0
        while(j!=total_nodes):
            row.append(0.0)
            j=j+1
        counter_mat.append(row)
        i=i+1

    total_shortest_path = (30*29)/2 #total shortest path will be 30 choose 2


    #filling the matrix with the counter of how many times a path comes in the way of shortest path
    for i in range(total_nodes):
        list_of_paths = nx.single_source_shortest_path(G, i)
        for j in range(len(list_of_paths)):
            k=0
            while(k!=(len(list_of_paths[j])-1)):
                index1 = list_of_paths[j][k]
                index2 = list_of_paths[j][k+1]
                if index1>index2:
                    counter_mat[index2][index1]=counter_mat[index2][index1]+1
                else:
                    counter_mat[index1][index2]=counter_mat[index1][index2]+1
                k=k+1    

    #finding edge betweeness
    for i in range(total_nodes):
        for j in range(total_nodes):
            counter_mat[i][j]=counter_mat[i][j]/total_shortest_path                
    return counter_mat
#nx.is_connected(G) returns true is graph is connected

while(nx.is_connected(G)!=False):
    counter_mat = betweeness(G)
    max_val=counter_mat[0][0] #set initial max to first element
    index1=0 #first node of edge
    index2=0 #second node of edge

    for i in range(total_nodes):
        for j in range(total_nodes):
            if(counter_mat[i][j]>max_val):
                max_val=counter_mat[i][j]
                index1=i
                index2=j
    counter_mat[index1][index2]=0

    G.remove_edge(index1,index2) #removing edge with high betweeness
         
nx.draw(G,with_labels=1)    # Drawing the graph with labels 
plt.show()                    # Printing the graph