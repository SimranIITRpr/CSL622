# Done By Allu Krishna Sai Teja(2015csb1005) & N Nikhil (2015csb1020)
# The code prints average number and maximum number of hops in the network
import networkx as nx

#Intializing a Graph

DG = nx.DiGraph()
DG.add_nodes_from(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','100','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34'])

#Reading the edges from the graph

f = open("pagerank.txt","r")
co=0
line = f.readline()
co=1
while line:
    co=co+1
    x ,y =line.split();
    DG.add_edge(x,y,weight=1)
    line = f.readline()
f.close()


#calculating the distance between every nodes and averaging it.


node_list=list(DG.nodes())
tot=0.00
min_hop=35
max_hop=0
for nodes in node_list :
    length=nx.single_source_shortest_path_length(DG,nodes)
    for nodes2 in node_list :
        if length[nodes2]<min_hop :
            min_hop=length[nodes2]
        
        if length[nodes2]>max_hop :
            max_hop=length[nodes2]

        tot=tot+length[nodes2]
        
n=len(node_list)  
tot=tot/(n*(n-1))

print("The average number of hops between any two persons is : " + str (tot))
print ("The max number of hops between two persons is : "+ str(max_hop))

