from collections import defaultdict 

class Graph:
	def __init__ (self,vertices):
		self.V=vertices
		self.graph=defaultdict(list)
		# print(type(graph))

	def addEdge(self,v,w):
		self.graph[v].append(w)
		# self.graph[w].append(v) # uncomment for undirected graph
	def helper(self,v,visited):
		visited[v]=True
		print(v)
		for i in self.graph[v]:
			if(visited[i]==False):
				self.helper(i,visited)
	def DFS(self,v):
		visited=[False]*self.V
		self.helper(v,visited)

v,k=input().split(' ')
v,k=[int(v),int(k)]
g=Graph(v)
for i in range(0,k):
	l,m=input().split(' ')
	l,m=[int(l),int(m)]
	g.addEdge(l,m)
g.DFS(0)