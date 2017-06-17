from collections import defaultdict
 
class Graph:
 
	def __init__ (self):
		self.graph = defaultdict(list)
 
 
	def add_edge(self,u,v,d):
		self.graph[u].append({v:d})
 
 
	def printf(self):
		print self.graph
 
	def makegr(self):
		return self.graph