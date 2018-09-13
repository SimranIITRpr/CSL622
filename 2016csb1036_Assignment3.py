import networkx as nx
import matplotlib.pyplot as plt
import random

#Dataset downloaded from https://snap.stanford.edu/data/web-BerkStan.html
G=nx.read_edgelist("web-Stanford.txt",create_using=nx.DiGraph(),nodetype=int)
G=nx.Graph()


#for any random graph
'''G.add_nodes_from([i for i in range(1,100)])
for i in G.nodes():
	for j in G.nodes():
		r = random.randint(0,1)
		if(r==1):
			G.add_edge(i,j)'''



count={}  #Dictionary for storing the count of number of times the node gets visited
for i in G.nodes():
	count[i] = 0
c=0

#c is the number of the iteration
#perform upto 1 lakh iterations
while(c<100000):
	rn = random.choice(list(G.nodes()))   #random node from the graph chosen with probability 0.2
	while(random.random()>0.2):    #random neighbor node chosen with the probability 0.8
		if(len(list(G.neighbors(rn))) != 0):
			rn = random.choice(list(G.neighbors(rn)))
		else :
			break
		count[rn]+=1
	c+=1

print "\nThe sorted pageranks are:\n"
for key,value in sorted(count.iteritems(),key=lambda (k,v):(v,k)):
    print "%s: %s" % (key,value)
print '-------------------------------------------------------'
print "\nThe actual pageranks obtained using default function are:\n"
for key,value in sorted(nx.pagerank(G).iteritems(),key=lambda (k,v):(v,k)):
    print "%s: %s" % (key,value)

#The pagerank values in both cases may differ slightly due to the closer values of pageranks

#nx.draw(G,with_labels=1)
#plt.show()
