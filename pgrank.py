# authors : Gurkaranpreet Singh , Gurparteek Singh , Rachit Arora
#It is simple page ranking Algorithm which takes input as pagerank.txt and gives output in the form of directed graph with radius of nodes proportional to its pagerank



import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def column(matrix, i):
  return [row[i] for row in matrix]

def convertDirectedGraphToAjdecencyMatrix(graph):
  maxNode = max(max(column(graph, 0)), max(column(graph, 1)))
  a = []
  for i in range(0,maxNode):
    b = [];
    for j in range(0, maxNode):
      b.append(0)
    a.append(b)

  for edge in graph:
    a[edge[0] - 1][edge[1] - 1] = 1

  return a

def readFile():
  with open('pagerank.txt') as f:
    array = [[int(x) for x in line.split()] for line in f]
  return array

def outBoundj(graph, j):
  return sum(graph[j])

def outBound(graph):
  L = []
  N = len(graph)
  for i in range(0,N):
    L.append(outBoundj(graph, i))
  return L

def m(graph):
  N = len(graph)
  M = []
  L = outBound(graph)
  for i in range(0, N):
    mi = []
    for j in range(0, N):
      if (graph[j][i]):
        mi.append(1.0/L[j])
      else:
        mi.append(0)
    M.append(mi)
  return M

def iterate(graph, R, d):
  N = len(graph);
  One = np.ones(N, dtype = int)
  One.shape = (N, 1)
  D = ((1-d)/N)*One
  M = np.matrix(m(graph))
  return d * M * R + D;

def findPageRank(graph, array, d = 0.85, e = 0.000001):
  N = len(graph)
  R = []
  for i in range(0, N):
    R.append(1*1.0/N)
  R = np.matrix(R)
  R.shape = (N, 1)
  E = N * e
  currE = 1
  Rnext = iterate(graph, R, d)
  while currE > E:
    Rnext = iterate(graph, R, d)
    currE = sum(abs(Rnext - R))
    R = Rnext
  # V = validNodes(graph)
  R = np.squeeze(np.asarray(R.transpose()))
  return validRanks(validNodes(array), R)

def arrayToTupples(graph):
  tupples = []
  for a in range(0, len(graph)):
    tupples.append((graph[a][0], graph[a][1]))
  return tupples;

def arrayToValues(R):
  tupples = []
  for a in range(0, len(R)):
    tupples.append((a+1, R[1]))
  return tupples;

def validNodes(graph):
  maxNode = max(max(column(graph, 0)), max(column(graph, 1)))
  n = [0 for x in range(0, maxNode)]
  for x in range(0, len(graph)):
    n[graph[x][0]-1] = 1
    n[graph[x][1]-1] = 1
  valid = []
  for x in range(1, maxNode+1):
    if (n[x-1]):
      valid.append(x);
  return valid;

def radius(rank):
  R = []
  for x in range(0, len(rank)):
    R.append(rank[x][1] * 100000)
  return R

def validRanks(V, R):
  C = []
  for x in range(0, len(V)):
    C.append((V[x], R[V[x] - 1]))
  return C

def labels(V, R):
  C = []
  for x in range(0, len(R)):
    C.append(str(V[x]) + str(R[x]))
  return C

def plot(graph, rank):
  G = nx.DiGraph()
  V = validNodes(graph)
  R = radius(rank)
  G.add_nodes_from(V)
  G.add_edges_from(arrayToTupples(graph))
  nx.draw(G, with_labels = True, node_size = R)
  plt.draw()
  plt.show()

def __main__():
  array = readFile()
  matrix = convertDirectedGraphToAjdecencyMatrix(array)
  pageRank = findPageRank(matrix, array)
  print(pageRank)
  plot(array, pageRank)

__main__()
