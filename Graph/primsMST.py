#Prim's Algorithm Implementation using Adjacency Matrix
class Graph:
	def __init__(self,vertices):
		self.V=vertices
		self.graph=[[-1 for columns in range(vertices)] for row in range(vertices)]

	def minKey(self,key,mstSet):
		min=9999999999
		min_index=-1
		for i in range(self.V):
			if mstSet[i]==False and key[i]<min:
				min=key[i]
				min_index=i
		return min_index

	def weightMST(self,parent,s):
		weight=0
		#start from 1 because 0th node is the root node
		for i in range(0,self.V):
			if parent[i]==-1:
				continue
			# print(parent[i],"----",self.graph[parent[i]][i],"------",i)
			weight+=self.graph[parent[i]][i]
		return weight

	def primsMST(self,s):
		parent=[None]*self.V
		mstSet=[False]*self.V
		key=[9999999999]*self.V
		#set the start key
		key[s]=0
		parent[s]=-1
		#loop over the vertices 
		for j in range(self.V):
			#set the value of u 
			u=self.minKey(key,mstSet)
			# print(key)
			# print(u)
			if u==-1:
				print("Some Error Index returned -1")
				return
			#put u in mst set
			mstSet[u]=True
			# print(mstSet)

			for v in range(self.V):
				if self.graph[u][v]>=0 and mstSet[v]==False and key[v]>self.graph[u][v]:
					key[v]=self.graph[u][v]
					parent[v]=u

		print(self.weightMST(parent,s))

n,e=input().split(' ')
n,e=[int(n),int(e)]
# print(n,e)
g=Graph(n)
for i in range(e):
	j,k,l=input().split(' ')
	j,k,l=[int(j)-1,int(k)-1,int(l)]
	g.graph[j][k]=l
	g.graph[k][j]=l
s=int(input())-1
g.primsMST(s)