import networkx as nx
G=nx.karate_club_graph()
print("Loaded Zachary Karate Network")
mat=[]

for ii in range(34):
    temp=[]
    for mm in range(34):
        temp.append(0)
    mat.append(temp)



for i in range(34):
    #print '\nfor ',i,'th node:'    
    vv = nx.single_source_shortest_path(G, i)
    #print(vv)
    #print("\n\n")

    for mm in range(len(vv)):
        for jj in range(len(vv[mm])-1):
            first=vv[mm][jj]
            second=vv[mm][jj+1]

            mat[first][second]=mat[first][second]+1
'''
for lp in range(34):
    print lp ,'th the node',mat[lp],'\n'    
'''
total=0.0
for ii in range(34):
    for jj in range(34):
        total=total+mat[ii][jj]


for pp in range(34):
    for vv in range(pp+1,34):
        mat[pp][vv]=mat[pp][vv]+mat[vv][pp]

for pp in range(34):
    for vv in range(0,pp):
        mat[pp][vv]=0



finalmat=list()
for ii in range(34):
    temp=[]
    for mm in range(34):
        temp.append(0.0)
    finalmat.append(temp)

for ii in range(34):
    for jj in range(34):
        bb= float(mat[ii][jj])
        finalmat[ii][jj]=bb/total


print ("Total edges when the graph was connected = ",G.number_of_edges())
while(nx.is_connected(G)!=False):
    maxi=finalmat[0][0]
    fir=0
    sec=0
    for ii in range(34):
        for jj in range(34):
            if(finalmat[ii][jj]>maxi):
                maxi=finalmat[ii][jj]
                fir=ii
                sec=jj
    #print(fir,sec,"\n\n\n")
    finalmat[fir][sec]=0

    G.remove_edge(fir,sec)
    
    
#print (nx.is_connected(G))
print ("After removing nodes, total edges = ",G.number_of_edges())   