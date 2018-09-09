import networkx as nx
import random
import operator
import matplotlib.pyplot as py
'''''link of the snap data set is https://snap.stanford.edu/data/wiki-Vote.html'''''
G=nx.read_edgelist('/home/iitropar/Desktop/Wiki-Vote.txt')
print nx.info(G) 
nx.draw(G,with_labels=True)
x=random.choice([i for i in range(G.number_of_nodes())])    //choosing a random node from where random walk will start
dict_counter={}                                             //maintaining dictionary counter for random node
for i in range(G.number_of_nodes()):
        dict_counter[i]=0
dict_counter[x]=1
list_n=[]                                     //maintaining the list for the nodes travelled during random walk
prob=random.random()                         //setting a random prob 
for i in range(5000000):                      // running for huge number 
        for i in range(G.number_of_nodes()): 
                if(G.has_edge(x,i)==True):         //if there is an edge between x and i then append it into list 
                        list_n.append(i)
                        print(list_n)
                else:
                        x=random.choice([i for i in range(G.number_of_nodes())])   //if no edge then choose next move randomly
                        continue
        if(prob>0.2):                             //taking prob for teleporting
          	x=random.choice([i for i in range(G.number_of_nodes())])
 	        dict_counter[x]=dict_counter[x]+1                    //increasing the dict counter
 	else:
                y=random.choice(list_n)            //if prob<0.2 choosing randomly node for teleportation
                dict_counter[y]=dict_counter[y]+1
                x=y
p=nx.pagerank(G)                   //using page rank function 
print(p)
print(dict_counter)
sorted_y=sorted(p.items(), key=operator.itemgetter(1))              //sorting the values for comparison
sorted_x = sorted(dict_counter.items(), key=operator.itemgetter(1))
print(sorted_x)
print(sorted_y)


