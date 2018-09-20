# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 21:33:30 2018

@author: nittin pc
"""
import networkx as nx


# here we are reading the graph and then giving weights to the graph as per their overlap 
# the path that is returned by the best_path() is the shortest path with maximum weight
# that is first we find the shortest paths if multiple then we find one with maximum sum of weight 

def best_path(G,u,v):
    shortest_paths = list(nx.all_shortest_paths(G,u,v))
    answer_path = []
    if (len(shortest_paths) > 1):
        mx_weight = 0
        for path in shortest_paths:
            s = 0
            for i in range(0,len(path)-1):
                s+=G.get_edge_data(path[i],path[i+1])['weight']
            if mx_weight < s:
                mx_weight = s
                answer_path = path
        return answer_path    
    else: 
        return shortest_paths[0]
                
    
# this function returns the dictionary with node pair as key and the best_path as its value
  
def get_best_path_dictionary(G):
    if nx.is_connected(G) == False:
        print('Graph is not connected')
    else:      
        best_path_dictionary = {}
        for i in list(G.nodes()):
            for j in list(G.nodes()):
                if (i!=j):
                    #best_path_dictionary[i,j] = best_greedy_path(G,i,j,[])
                    best_path_dictionary[i,j] = best_path(G,i,j)
                    
    return best_path_dictionary
    

# reading the input from the file
with open(r'subj.txt','r') as f:
    content = f.readlines()
    
content = [x.strip() for x in content] 
content_list = []
for i in range(0,len(content)):
    content_list.append(list(map(int, content[i][:].split())))

G = nx.Graph()
for i in range(0,len(content_list)):
    G.add_node(content_list[i][0])
# adding weight to the edges    
for i in range(0,len(content_list)):
    for j in range(i,len(content_list)):
        if (i!=j):
            ar1 = content_list[i][1:13]
            ar2 = content_list[j][1:13]
            wt = 0
            for it in range(0,12):
                if (ar1[it] == 1 and ar2[it] == 1):
                    wt += 1
            if (wt > 0 ):
                G.add_edge(content_list[i][0],content_list[j][0],weight = wt)
                
                
Best_Path_Dictionary = get_best_path_dictionary(G)
