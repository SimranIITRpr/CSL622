#! usr/bin/python
import networkx as nx
import matplotlib.pyplot as plt
import itertools

'''
Assignment 4
NAROTAM SINGH 2015CSB1065
'''

G=nx.karate_club_graph()
def calc_betweenness(): #returns the betweenness for all the edges in descending order of their betweenness
    d=dict()    #dictionary to store betweenness of each edge
    for e in G.edges():
        d[e]=0  #initialisation each betweenness to 0
    for e in G.edges():
        for u,v in list(itertools.combinations(list(G.nodes()), 2)):
            num=0;
            paths=[p for p in nx.all_shortest_paths(G,u,v)]
            for p in paths:
                for i in range(0,len(p)-1):
                    if e == (p[i],p[i+1]) or e == (p[i+1],p[i]):
                        num=num+1;
                        break;
            d[e]=d[e]+(num/len(paths))           #summing the fractions over all u,v vertices for each edge e
    d=sorted(d.items(), key=lambda x: x[1],reverse=True) #sorting the betweenness in descending order
    return d

while(nx.is_connected(G)):  #removing edges till the graph gets divided into two components
    d=calc_betweenness()    #calculating the betweenness again after removing an edge
    print("edge",d[0][0],"removed")
    G.remove_edge(*d[0][0]) #first edge in the list has the highest betweenness since it is already sorted in descending order

nx.draw(G,with_labels=1)
plt.show()
    





