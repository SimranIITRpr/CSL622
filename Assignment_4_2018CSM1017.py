#2018CSM1017_Rakesh_Kumar_Meena#
#Communities detection of karate network using edge betweenness#
#sucessfuly find the result  after spliting graph 
#based on removing max visited coomon paths between nodes until we get two spliting Graph

#comm_detection
import networkx as nx
import matplotlib.pyplot as plt
from operator import itemgetter

#Data set from karate club.
g = nx.karate_club_graph()

#########____GRAPH_BEFORE_EDGE_BETWEENNNES_ALGO___#######
print("ORIGINAL_GRAPH_WITH_INFORMATION")
edges_sorted=sorted(nx.edges(g))
print("Edges Sorted")
print(edges_sorted)
print()
print("Number of Edges")
print(nx.number_of_edges(g))
nx.draw(g,with_labels=True)
print(plt.show())

#############FUNCTION FOR EDGE BETWEENNNESS_ALGO____#######

def fun2(graph_g):
    edges_sorted=sorted(nx.edges(graph_g))
    #print("Edges Sorted")
    #print(edges_sorted)
    #print()
    #print("Number of Edges")
    #print(nx.number_of_edges(graph_g))

    #Find Shortest path between all Nodes.
    shortest_path_list=[]
    for i in g.nodes():
        for j in g.nodes():
            if(i!=j):
                shortest_path=nx.shortest_path(g,source=i,target=j)
                shortest_path_list.append(shortest_path)
    #print("shortest Path Between all edges")
    #print(shortest_path_list)
    #print()
    #print("Number of Shortest Path Between all Nodes",len(shortest_path_list))
    #print()

###############___________Count the edges visiting by any two node for its shortest path________#############
    result_list=[]
    for i in range(len(edges_sorted)):
        list11=edges_sorted[i]
        count1=0
        for j in range(len(shortest_path_list)):
            list22=shortest_path_list[j]
            count=0
            jj=0
            for ii in range(len(list11)):
                iii=ii+jj
                for jj in range((iii),len(list22)):
                    if(count==2):
                        break
                    elif(list11[ii]==list22[jj]):
                        count=count+1
                        break
                    elif(count==2):
                        break
                    else:
                        #print("hi")
                        count=0

            if(count==2):
                count1=count1+1
        #print(count1)
        result_list.append((list11,count1))
        #print(result_list)
        #print(sub_list1)
        #print()
    sort_sublist1=sorted(result_list,key=lambda x:x[1],reverse=True)
    #print("Coomon edges visted number during shortest path--INCREASING ORDER--")
    #print(sort_sublist1)
    #print()
    #print("Total Number of common edges",len(sort_sublist1))


    for i in range(len(sort_sublist1)):
        for j in edges_sorted:

            if(sort_sublist1[i][0]==j):
                graph_g.remove_edge(j[0],j[1])
                is_graph_g_connected=nx.is_connected(graph_g)

                if(is_graph_g_connected==True):
                    fun2(graph_g)
                elif(is_graph_g_connected==False):

                    print("AFTER_SPLITTING_GRAPH_WITH_INFORMATION ( ONLY in TWO GRAPH )")
                    edges_sorted=sorted(nx.edges(graph_g))
                    print("Edges Sorted")
                    print(edges_sorted)
                    print()
                    print("Number of Edges")
                    print(nx.number_of_edges(graph_g))
                    nx.draw(graph_g,with_labels=True,node_color=g)
                    print(plt.show())
                    exit()
##########_______CALLING_FUNCTION_________############
fun2(g)
