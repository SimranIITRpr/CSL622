#@Rakesh Kumar Meena, 2018csm1017
#Dataset['subj.txt'] is taken from CSE IIT ROPAR
#Problem- find the best path between given students with the help of subject taken by student.

#first column reprsent students[1,2,3,...,14] and and each student have option to chose 12 subject represent in binary form   
#here 1 means subject is taken by student and 0 means subject not taken by student.

#import files
import networkx as nx
import matplotlib.pyplot as plt 

#create a empty undirected graph.
G=nx.Graph()

#store given file data  in data list  
data = []
for line in open('subj.txt'):
    data.append(line.split())

#If you wana print it just uncommit below print statment.    
#print(data)

#########---LOGIC----###########
# If the nodes are directly connected by an edge, that would be the best path.
#Else consider the following some scenario according given problem statment:
#Output may vary if there are exists more then two best node ->here is possible.

#Here we plot an edge between to nodes if there is any common subjetc between them
#alongth with i take  weight that store  as weight in Graph represent bond strength (more weight ,more tight bond strength)
#for best path we choose tightest bond from all bonds.

for i in range(len(data)):
	for j in range(i,len(data)):
		if(i!=j):

			weight=0
			for k in range(1,13):
				if(int(data[i][k])==int(data[j][k])==1):
					weight=weight+1

			if(weight>=1):
				s,d=int(data[i][0]),int(data[j][0])
				G.add_edge(s,d, weight=weight)

#Desired Output
print("Best path between node")
for i in range(1,15):
	for j in range(j,15):
		if(i!=j):
			print("(",i,"-",j,") =",nx.shortest_path(G,source=i,target=j))
###PLOT GRAPH##

color_map = []
for node in G:
    if node <10:
        color_map.append('blue')
    else: color_map.append('green')      
plt.title('Student Connectivity')
nx.draw(G,with_labels=True,edge_color='r',node_color=color_map)
print(plt.show())
