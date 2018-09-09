#dataset obtained from snap dataset Amazon0302
#2016csb1065_3

import networkx as nx
import random
import matplotlib.pyplot as plt
#chosing a new random node with probability 0.2 and crawling with probability 0.8
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
G = nx.read_edgelist("p2p-Gnutella08.txt")

RW_points = random_walk(G)
#print(RW_points)

sorted_rw=list(sorted(RW_points.values(),reverse=True))
print(sorted_rw)


pr = nx.pagerank(G)
pr_sorted = list(sorted(pr.items(), key = lambda x: x[1], reverse = True))
#comparing the data
plt.plot(sorted_rw,pr_sorted, 'b', linewidth = 7.0)
plt.show()
