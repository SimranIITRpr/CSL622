import networkx as nx
G = nx.Graph() 
n=list()
for p in range(14):
    n.append(p+1)
G.add_nodes_from(n)
file = open("subj.txt", "r")

tuple_mat=list()

list_tuples = file.readlines()



for p in range(14):
    temp=list()
    for k in range(2,len(list_tuples[p])-1):
        if list_tuples[p][k]!=' ':
            c = list_tuples[p][k]
            c=int(c)
            temp.append(c)
    tuple_mat.append(temp)
    
weight_mat = list()

for i in range(14):
    temp=list()
    for j in range(14):
        temp.append(0)
    weight_mat.append(temp)    
        
        
for i in range(14):
    for j in range(i+1,14):
        for k in range(12):
            if tuple_mat[i][k]==1 and tuple_mat[j][k]==1:
                weight_mat[i][j]+=1


for i in range(14):
    for j in range(14):
        if weight_mat[i][j]>0:
            G.add_edge(i+1,j+1)        

print "----------------BEST PATHS BETWEEN ALL NODES----------------------"

for i in range(14):
    for j in range(i+1,14):
        ii=i+1
        jj=j+1
        if G.has_edge(ii,jj)==True:
            print "from node - ",ii,"to",jj,":",ii,"->",jj
        else:
            paths = nx.all_shortest_paths(G, ii, jj)
            path_list=list(paths)
#            if ii==11:
#                print path_list
            final=list()
            final.append(path_list[0][0])
            k=0
            while(k!=(len(path_list[0])-1)):
                val=0
                fi=0
                
                for pp in range(len(path_list)):
                    if(path_list[pp][k]==final[len(final)-1]):                
                        first= path_list[pp][k]-1
                        second = path_list[pp][k+1]-1
                        swap=0
                        if(first>second):
                            swap=1
                            temp=second
                            second = first
                            first = temp
 #                       print first," ",second    
                        if(weight_mat[first][second]>val):
                            if swap==0:
                                fi=second+1
                            else:
                                fi=first+1    
                            val=weight_mat[first][second]
                
                final.append(fi)
                k=k+1
            print "from node - ",ii,"to",jj,":",final[0],
            for inm in range(1,len(final)):
                print "->",final[inm], 
            print ""    






