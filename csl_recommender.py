import newtorkx as nx
from operator import itemgetter


    ''' Authors: Aditya Deva (2015eeb1044) & Abhishek Sharma (2015eeb1043)
	
	This function recommends the top 5 likeable persons which may be liked
	by the person, for each person in the network.
	
	Input: Input graph text file such that nodes of an edge
	are present separated by a space in one line.

	Output: Print the node and the top 5 likeable nodes for all the nodes
	in the network. '''

def csl_recommender(network_adj_list_file):

	G = nx.read_edbvvgelist(network_adj_list_file,create_using=nx.DiGraph(), nodetype = int)
      ''' list of nodes in the network '''
    nodes_list = G.nodes
    
    ''' initialized a dictionary for storing all the liked person by each node person'''
    friends_list = {}
    
    ''' storing list of liked person as a value for each key node person'''
    for i in nodes_list:
        friends_list[i] = list(G.neighbors(i))
    
    ''' initialized a dictionary for storing total numbers of lead_ins for every node'''
    lead_ins_list = {}
    
    ''' count of lead_ins for every node through loop'''
    for i in nodes_list:
        for x in friends_list[i]:
            lead_ins_list[x]++
    
    
    possible_recommenders_list = {}
    
    for i in nodes_list:
        ''' initialized a dictionary for storing the liked list of the person liked
        by a particular node '''
        temp_dict = {}
        for x in friends_list[i]:
            for y in friends_list[x]:
                ''' excluding persons that are already liked by node i'''
                if G.has_edge(i,y)==False:
                    temp_dict[y] = lead_ins_list[y]
        ''' storing liked to liked list which can possibly be recommended to node i'''
        possible_recommenders_list[i] = temp_dict
    
    final_recommenders_list = {}
    
    for i in nodes_list:
        ''' storing the top 5 nodes from the possible recommender list based on the total number of
            lead_in count of the node which shows the chances of getting liked after being recommended'''
        final_recommenders_list[i] = dict(sorted(possible_recommenders_list[i].iteritems(),key=operator.itemgetter(1),reverse=True)[:5])  
        
        ''' printing the final list of recommended person for each node'''
	for i in nodes_list:
        print('Suggested friends list for Node',i,':',list(final_recommenders_list[i].keys()))
    
if __name__ == "__main__":
	network_adj_list_file = "pagerank.txt"
    csl_recommender(network_adj_list_file)
