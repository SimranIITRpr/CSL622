'''
Question: Find the number of fake edges required to add to the least Impressive to remove him from that position.

Group members:
Piyush Pilaniya(2016csb1049)
Prinshu Kumar(2016csb1051)
Vaibhav Chopra(2016eeb1104)
'''
import networkx as nx
#import matplotlib.pyplot as plt
G = nx.read_edgelist(r"/home/prinshu/Downloads/pagerank.txt",create_using=nx.DiGraph(), nodetype = int) #Created a directed graph by reading from a file.

#removed the unnecessary nodes.
G.remove_node(35) 
G.remove_node(40)
#nx.draw(G,with_labels=1)
y = []

#for all the nodes in the graph
for i in range(33):    
      if i == 17:      #unnecessary nodes.
         continue
      p = G.in_edges(i+1)   #Getting the number of incoming edges in the graph.
      x = len(p)
      y.append(x)            #Inserting that into a list.
      
p = G.in_edges(100)          #For the extra node.
y.append(len(p))

print (y)
y.sort()                     #sorting the list
print (y)
print ("Required edges : ")
print (y[1]-y[0])           #Printing the number of required edges.

list2 = G.in_edges(y[0])    #Getting the list of incoming edges of the least impressive.
nodesList = G.nodes()
count = 0

print "The nodes to which friendship can be done are : "
for i in nodesList:          #Printing the nodes to which frienship can be done.
	if i not in list2:   #If the node is not already the friend of the least impressive person.
		print i
		count+=1
	if count==y[1]-y[0]: #If the required number is achieved.
		break
