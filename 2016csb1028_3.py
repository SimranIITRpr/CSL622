#dataset obtained from SNAP dataset Amazon0302.txt

import networkx as nx
import random
import matplotlib.pyplot as plt


def random_walk(G):
    di={}
    nodes = list(G.nodes())
    for k in nodes:
        di[k]=0.0
    u = random.choice(nodes)
    di[u] += 1
    cons=0
    while(cons<100000):
        nb=[m for m in G[u]]
        if(len(nb)==0):
            u=random.choice(list(G.nodes))
            di[u] += 1
        else:
            fl=random.random()
            if(fl>=0.2):
                u=random.choice(nb)
                di[u] += 1
            else:
                u=random.choice(list(G.nodes))
                di[u] += 1
        cons += 1
    return di
G = nx.read_edgelist("Amazon0302.txt",nodetype=int)

RW_points = random_walk(G)
#print(RW_points)

sorted_rw=list(sorted(RW_points.values(),reverse=True))



pr = nx.pagerank(G)
pr_sort=[]
pr_sorted = list(sorted(pr.items(), key = lambda x: x[1], reverse = True))
for each in pr_sorted:
	pr_sort.append(each[1])


plt.plot(pr_sort,sorted_rw, 'b', linewidth = 7.0)
plt.show()
