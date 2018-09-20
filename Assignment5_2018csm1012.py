import networkx as nx


with open("subj.txt") as f:
	Data = [l.strip() for l in f.readlines()]
	info = {int(Datum.split()[0]):Datum.split()[1:] for Datum in Data}
	nodes = info.keys()


G = nx.Graph()

G.add_nodes_from(nodes)


for i in range(1, len(info)):
	for j in range(i+1, len(info)+1):
		for (p, q) in zip(info[i], info[j]):
			if p is '1' and q is '1':
					G.add_edge(i, j)
					break


def weight(info, i, j):
	count = 0
	for p, q in zip(info[i], info[j]):
		if p is '1' and q is '1':
			count+=1
	return count



def Path(Graph, points, src, dest):
    path = [src]
    while True:
        n = list(Graph.neighbors(src))
        if dest in n:
            path.append(dest)
            break
        for p in path:
            if p in n:
                n.remove(p)
        Weight= [weight(info, src, i) for i in n]
        best = Weight.index(max(Weight))
        path.append(n[best])
        src = n[best]
    return path
        



for i in G.nodes():
 for j in G.nodes():
    if(i!=j):
     print(str(i)+" "+str(j)+"    "+ str(Path(G, info, i, j)))  






