st = []

def topsor(ver,g,vis):
	print "hsad"
	vis[ver] = 1
	print st
	for i in g[ver]:
		if(not vis[i]):
			topsor(i,g,vis)

	st.append(ver)






n = int(raw_input()) # 10

e = int(raw_input()) #13


graph = [[] for i in range(n+1)]

for i in xrange(e):
	u,v = map(int,raw_input().split())
	graph[u].append(v)

print graph

vis = [0 for i in range(n+1)]
for i in xrange(1,n+1):
	if(not vis[i]):
		topsor(i,graph,vis)

print st
while(len(st)>0):
	print st.pop()
















