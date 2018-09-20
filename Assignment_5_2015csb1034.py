#import files
import networkx as nx
import matplotlib.pyplot as plt 

#create a empty undirected graph.
G=nx.Graph()

#store given file data  in data list  
data = []
for line in open('subj.txt'):
    data.append(line.split())
 


for i in range(len(data)):
    for j in range(i,len(data)):
        if(i!=j):

            weight=0
            for k in range(1,len(data[0])):
                if(int(data[i][k])==int(data[j][k])==1):
                    weight=weight+1

            if(weight>=1):
                weight=1/float(weight)            
                s,d=int(data[i][0]),int(data[j][0])
                G.add_edge(s,d, weight=weight) 
v=[]
v=G.nodes()

nx.draw(G, with_label = True)
plt.show()
for i in v:
    for j in v:
        if(i!=j):
            print "shortest path b/w", i,"&",j
            if(G.has_edge(i,j)):
                print i,j
            else:
                print nx.shortest_path(G,i,j)
                

                 
        
	

