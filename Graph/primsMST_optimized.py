# Prim's Algorithm Implementation using Adjacency List
from heapq import heappush,heappop
from collections import defaultdict


class Graph:
	def __init__(self, vertices):
		self.V=vertices
		self.graph=defaultdict(list)
		self.cost={}

	def weightMST(self,parent,s):
		weight=0
		for i in range(0,self.V):
			if parent[i]==-1 :
				continue
			weight+=self.cost[(parent[i],i)]
		return weight

	def primsMST(self,s):
		parent=[None]*self.V
		mstSet=[False]*self.V
		dist=[9999999999]*self.V
		#set the start key
		dist[s]=0
		parent[s]=-1
		heap=[]
		item=[dist[s],s]
		heappush(heap,item)
		while heap:
			d,u=heappop(heap)
			if mstSet[u]:
				continue
			mstSet[u]=True

			for v in self.graph[u]:
				if mstSet[v]==False and dist[v]>self.cost[(u,v)]:
					dist[v]=self.cost[(u,v)]
					parent[v]=u
					item=[dist[v],v]
					heappush(heap,item)

		print(self.weightMST(parent,s))

n,e=input().split(' ')
n,e=[int(n),int(e)]
# print(n,e)
g=Graph(n)
for i in range(e):
	j,k,l=input().split(' ')
	src,dst,wt=[int(j)-1,int(k)-1,int(l)]
	g.graph[src].append(dst)
	g.graph[dst].append(src)#for undirected graph
	g.cost[(src,dst)]=wt
	g.cost[(dst,src)]=wt

s=int(input())-1
g.primsMST(s)