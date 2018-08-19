'''
Q.Find the best possible node to poison the graph with fake news assuming that
  a person reveals the information to a person he/she likes with some
  probability p, where 0<p<1

Soln. We have used a probabilistic approach for finding the best possible node
      using a modified BFS algorithm.

Group Memebers:
Nitin Gandhi 2016csb1045
Paras Kumar 2016csb1047
Akshat Rathore 2016csb1030

Test Run:
>>python3 poison.py 
Enter file name: 
pagerank.txt
Best node to poison the graph is: 3
'''
import collections

#represents an edge in the graph
class Edge:
	def __init__(self, one, two):
		self.a = one
		self.b = two

#Modified Breadth first Search algorithm
def BFS(vertexArray, adjList, node):
	visited = []
	for k in range(size):
		visited.append(False)
	visited[vertexArray.index(node)] = True
	q = collections.deque([])
	q.append(node)
	lst = [0 for k in range(len(vertexArray))]
	lst[vertexArray.index(node)] = 0.3;
	while(len(q) != 0):
		node = q.popleft()
		visited[vertexArray.index(node)] = True
		ind = vertexArray.index(node)
		for k in adjList[ind]:
			if(visited[vertexArray.index(k)] == False):
				visited[vertexArray.index(k)] = True
				q.append(k)
				lst[vertexArray.index(k)] = lst[ind]*0.3
	return sum(lst)

#Main Script

#list of directed edges
edgeArray = []

#list of vertices
vertexArray = []

print ("Enter file name: ")
file_name = input()
f = open(file_name)

#filling data in above two lists
for l in f:
	a = l.split(" ")
	one = int(a[0])
	two = int(a[1])
	vertexArray.append(one)
	vertexArray.append(two)
	edgeArray.append(Edge(one, two))

#removing duplicates
vertexArray = sorted(list(set(vertexArray)))
size = len(vertexArray)

#adjecency list represenataion to be used for BFS
adjList = []

#adjecency list is an array of array, so initalizing with empty lists
for i in range(size):
	adjList.append([])

#populating adjecency list
for elem in edgeArray:
	inde = vertexArray.index(elem.a)
	adjList[inde].append(elem.b)

'''
for n,k in enumerate(adjList):
	print(vertexArray[n],k)
'''
#max stores the current max probality sum for chosing a given node
max = 0

#initalizing the best_vertex with a node number which is not present in graph
best_vertex = -1

#Running modified BFS for each node of graph to find the best node
for v in vertexArray:
		val = BFS(vertexArray, adjList, v)
		if max < val:
			max = val
			best_vertex = v
#Final result
print ("Best node to poison the graph is: " + str(best_vertex))
