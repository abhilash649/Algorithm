from collections import defaultdict

class Graph:

	def __init__(self,vertices):
		self.V= vertices
		self.graph_= defaultdict(list)


	def addEdge(self,v,w):
		self.graph_[v].append(w) 
		self.graph_[w].append(v) 

	def isCyclic_helper(self,v,visited,parent):
		visited[v]= True
		for i in self.graph_[v]:
			if visited[i]==False : 
				if(self.isCyclic_helper(i,visited,v)):
					return True
			elif parent!=i:
				return True
		
		return False
		
	def isCyclic(self):
		visited =[False]*(self.V)
		for i in range(self.V):
			if visited[i] ==False: 
				if(self.isCyclic_helper(i,visited,-1))== True:
					return True
		
		return False

v=int(input('Number of Vertices:'))
g=Graph(v)
k=int(input('Number of Edges:'))
print('Enter edges in pairs of two separated by space')
for i in range(0,k):
	l,m=raw_input().split(' ')
	l,m=[int(l),int(m)]
	g.addEdge(l,m)


if g.isCyclic():
	print "Graph contains cycle"
else :
	print "Graph does not contain cycle "
