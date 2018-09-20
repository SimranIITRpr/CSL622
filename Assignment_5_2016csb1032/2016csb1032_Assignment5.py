import networkx as nx
import matplotlib.pyplot as plt

def data_gain():
        nodes_tuple={}
        with open('subj.txt','r') as f:
                for line in f:
                        state=1
                        node_id=-9999
                        tuple_list=[]
                        for word in line.split():
                               if state==1:
                                state=0
                                node_id=int(word) 
                               else:
                                tuple_list.append(int(word)) 
                        nodes_tuple[node_id]=tuple_list
        # for k in nodes_tuple:
        #        print k,nodes_tuple[k]
        
        return nodes_tuple                        

def caller():
        nodes_tuple=data_gain()
        G=nx.Graph()
        for node1 in nodes_tuple:
                for node2 in nodes_tuple:
                        if node1!=node2 and G.has_edge(node1,node2)==False:
                            if (G.has_node(node1)==False):
                                G.add_node(node1)
                            if (G.has_node(node2)==False):
                                G.add_node(node2)    
                            list_1=nodes_tuple[node1]
                            list_2=nodes_tuple[node2]
                            cal_weight=0
                            for i in range(len(list_1)):
                                if list_1[i]==1 and list_1[i]==list_2[i]:
                                        #print node1,node2,i
                                        cal_weight+=1                    
                            if cal_weight!=0:
                                cal_weight=1.0/float(cal_weight)
                                G.add_edge(node1,node2,weight=cal_weight)
                               
        return G     


def main():
        G=caller()
        for node1 in G.nodes():
                for node2 in G.nodes():
                        if node1!=node2 and nx.has_path(G,node1,node2):
                                if G.has_edge(node1,node2):
                                	path=nx.shortest_path(G,node1,node2)
                                	print "Best_path_(COMMON_SUBJECT)_for:(",node1,node2,') is ',path
                                else:
	                                path=nx.dijkstra_path(G,node1,node2) 
	                                # Distances are calculated as sums of weighted edges traversed which in inversly propotional to common courses enrolled for a given edge
	                                print "Best_path_(MAX_OVERLAP)_for:(",node1,node2,') is ',path

                        else:
                                if node1!=node2:
                                        print node1,node2

        nx.draw(G,with_labels=True)
        plt.show()
main()                                
