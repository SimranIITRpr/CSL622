'''

shiva(2014csb1037)
rishab(2014csb1027)
rahul(2014csb1026)

implemented search algorithm based on score of strongness
'''
import networkx as nx
m=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,100,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34]
list1=[]
list2=[]
list3=[]
list4=[]
X=nx.read_adjlist("pagerank.txt",nodetype=int, create_using=nx.DiGraph())
def sortSecond(val):
    return val[1] 
def scoreofstrongness(sors,targ):
 z=0
 for i in range(3):
  paths = nx.all_simple_paths(X, source=sors, target=targ, cutoff=i+1)
  lpaths = nx.all_simple_paths(X, source=sors, target=targ, cutoff=i)
  z=z+((len(list(paths))-len(list(lpaths)))*(10-i))
 return z
def search(nod):
 for k in m:
  d=nx.all_simple_paths(X,nod,k, 3)
  f=list(d)
  if f:
   e=min(len(x) for x in f)
   if e==2:
    list1.append([k,scoreofstrongness(nod,k),1])
   elif e==3:
    list2.append([k,scoreofstrongness(nod,k),2])
   elif e==4:
    list3.append([k,scoreofstrongness(nod,k),3])
   else:
    list4.append([k,scoreofstrongness(nod,k),"more"])
 list1.sort(key=sortSecond,reverse=True)
 list2.sort(key=sortSecond,reverse=True)
 list3.sort(key=sortSecond,reverse=True)
 list4.sort(key=sortSecond,reverse=True)
 final_list=list1+list2+list3+list4
 return final_list
print(list(search(1)))