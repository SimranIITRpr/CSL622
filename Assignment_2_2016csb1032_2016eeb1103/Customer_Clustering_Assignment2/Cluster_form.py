

# -------------2016CSB1032 Arunaksha Talukdar ----------2016eeb1103 Utkarsh Katiyar--------------


# Using Elbow methord to reduce average distance between centroid and cluster
import matplotlib.pyplot as plt
import pandas as pd # For Data Analytics
from sklearn.cluster import KMeans
import random

# Reading The datasheet through pandas
data_set=pd.read_csv('Data_final.csv')

#cor=Cordinate pair(x,y) to plot and analyse data
cor=data_set.iloc[:,[3,4]].values 



def cluster_distance(upper_limit=11):
	sum_distance=[]
	index_set=range(1,upper_limit)
	for k in index_set:
		# Creation of optimum k clusters by k-means++ optimization with no random state and storing in kmeans
		kmeans=KMeans(n_clusters=k,init='k-means++',random_state=None)
		kmeans.fit(cor) 

		sum_distance.append(kmeans.inertia_) # Sum of Squared value of distances from nearest centroid for each cluster 
	plt.plot(index_set,sum_distance)
	plt.title("Sum-Squared-Distance from centroid for nearest node")
	plt.xlabel("Number of clusters => ")
	plt.ylabel("Square sum of distance of (node,nearest_cluster)")	
	plt.show()


# Fitting k-Means to datasheet

def plot_graph(pick_cluster=4):
	kmeans=KMeans(n_clusters=pick_cluster,init='k-means++',random_state=None)
	group_belongs=kmeans.fit_predict(cor)
	# Generate Random-Color for Clusters
	def rand_color():
	    rgbl=[1.0,1.0,1.0]
	    for i in range(3):
	    	rgbl[i]=random.uniform(0,1)
	    return tuple(rgbl)

	for i in range(pick_cluster):
		plt.scatter(cor[group_belongs==i,0],cor[group_belongs==i,1],s=50,color=rand_color(),label=str('Group '+str(i)))

	plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=100,label='k-Centroids',color='yellow')
	plt.title('Group Distribution[Similar (Earning,Spending)]')
	plt.xlabel('--Earning--')
	plt.ylabel('--Spending--')
	plt.legend()
	plt.show()

def plot_function():
	i=input("DEFAULT[0] CUSTOM[1]\n")
	if(i==1):
		m=input("N.o of Clusters Required?\n")
		x=input("Calculate Variation of Cluster_distance_from local_nodes till?(eg=10)\n")
		cluster_distance(x)
		plot_graph(m)
	else:
		cluster_distance()
		plot_graph()
plot_function()		
			
