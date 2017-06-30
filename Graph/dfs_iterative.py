from collections import defaultdict 

class Graph:
	def __init__ (self,vertices):
		self.V=vertices
		self.graph=defaultdict(list)
		# print(type(graph))

	def addEdge(self,v,w):
		self.graph[v].append(w)

	def DFS(self,v):
		visited=[False]*self.V
		stack=[]
		stack.append(v)
		while len(stack)!=0:
			v=stack.pop()
			if(visited[v]==False):
				visited[v]=True
				print(v)
			for i in self.graph[v]:
				if(not visited[i]):
					stack.append(i)

v,k=input().split(' ')
v,k=[int(v),int(k)]
g=Graph(v)
for i in range(0,k):
	l,m=input().split(' ')
	l,m=[int(l),int(m)]
	g.addEdge(l,m)
g.DFS(0)