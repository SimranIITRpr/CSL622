"""
@author: Subhranil Bagchi, Anurag Banerjee, Harsimar Singh
"""

import networkx as netx
import matplotlib.pyplot as plt

#find adjacent_nodes
def adj_nodes(G):
    list_nodes_info = []
    node_mapped = []
    i = 0
    for u in G.nodes():
        list_nodes_info.append([])
        list_adjNodes = []
        count = 0
        for v in G.nodes():
            if G.has_edge(u,v)==True:
                count = count+1
                list_adjNodes.append(int(v))
        list_nodes_info[i].append(int(u))
        list_nodes_info[i].append(count)
        list_nodes_info[i].append(list_adjNodes)
        node_mapped.insert(i,int(u))
        i = i+1
    return(list_nodes_info,node_mapped)

#returns the page ranking factor
def page_rank(G,list_nodes_info,node_mapped):
    initial_pageRank = []
    processed_pageRank = []
    for i in range(len(list_nodes_info)):
        initial_pageRank.insert(i,1/len(list_nodes_info))
    while(len(set(initial_pageRank))!=len(initial_pageRank)):
        for i in range(len(list_nodes_info)):
            cumPR = 0
            for j in range(len(list_nodes_info[i][2])):
                node_index = node_mapped.index(list_nodes_info[i][2][j])
                cumPR = cumPR + (initial_pageRank[node_index]/list_nodes_info[node_index][1])
            processed_pageRank.insert(i,cumPR)
        initial_pageRank = processed_pageRank
    
    return(initial_pageRank)

#sorts the page fanking factors and then assign ranking to each nodes base on its importance
def ranking_assign(G,pageRank_factor,list_nodes_info):
    nodes_with_ranks = []
    for i in range(len(G.nodes())):
        nodes_with_ranks.insert(i,[pageRank_factor[i],list_nodes_info[i][0]])
    nodes_with_ranks.sort(reverse=True)
    ranking = []
    for i in (range(len(G.nodes()))):
        ranking.append([i+1,list_nodes_info[i][0]])
    return(ranking)

G = netx.read_edgelist(r"pagerank.txt",create_using=netx.DiGraph())
netx.draw_spring(G,with_labels=1,node_size=200,font_size=12)
plt.show()

list_nodes_info,node_mapped = adj_nodes(G)
pageRank_factor = page_rank(G,list_nodes_info,node_mapped)
rank = ranking_assign(G,pageRank_factor,list_nodes_info)

#prints the nodes along with ranking
for i in range(len(G.nodes())):
    print("Node: " + str(rank[i][0]) + " \tRank: " + str(rank[i][1]))
