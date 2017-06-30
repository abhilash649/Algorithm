# Prim's Algorithm Implementation using Adjacency List
from heapq import heappush,heappop,heapify
from collections import defaultdict


class Graph:
	def __init__(self, vertices):
		self.V=vertices
		self.graph=defaultdict(list)
		self.cost={}

	def printMST(self,s,dist):
		for i in range(0,self.V):
			if i!=s:
				if dist[i]==9999999999:
					print("-1",end=" ")
				else:
					print(dist[i],end=" ")
		return 

	def dijkstra(self,s):
		parent=[None]*self.V
		mstSet=[False]*self.V
		dist=[9999999999]*self.V
		#set the start key
		dist[s]=0
		parent[s]=-1
		heap=[]
		item=[dist[s],s]
		heappush(heap,item)
		while heap :
			heapify(heap)
			d,u=heappop(heap)
			# print("dist till ",u,"= ",d)
			if mstSet[u]:
				continue
			for v in self.graph[u]:
				if mstSet[v]==False and dist[v]>self.cost[(u,v)] + dist[u] :
					dist[v]=self.cost[(u,v)] + dist[u]
					parent[v]=u
					item=[dist[v],v]
					# print("dist till ",v,"= ",dist[v])
					heappush(heap,item)

		self.printMST(s,dist)

t=int(input())
for k in range(t):
	n,e=map(int,input().split(' '))
	# print(n,e)
	g=Graph(n)
	for i in range(e):
		src,dst,wt=map(int,input().split(' '))
		src=src-1
		dst=dst-1
		if src==dst:
			continue
		if (src,dst) not in g.cost:
			g.graph[src].append(dst)
			g.graph[dst].append(src)#for undirected graph
			g.cost[(src,dst)]=wt
			g.cost[(dst,src)]=wt
		else:
			if g.cost[(src,dst)] > wt:
				g.cost[(src,dst)]=wt
				g.cost[(dst,src)]=wt
	s=int(input())-1
	g.dijkstra(s)
	print("")