	dist = [INF for i in range(n)]
	prev = [-1 for i in range(n)]
	dist[s-1]=0
	g = g1.makegr()
	#print g
	for i in xrange(n):	#add edges to priority queue
		if(i==s-1):
			add_task(s-1,0)
		else:
			add_task(i,INF)
 
 
	cnt = 0
 
	while cnt<n:		#while queue is not empty
		
		u = pop_task()
		cnt+=1
		for v in g[u]:
 
			if(dist[v.items()[0][0]]>dist[u]+v[v.items()[0][0]]):
				dist[v.items()[0][0]]=dist[u]+v[v.items()[0][0]]
				prev[v.items()[0][0]]=u
				add_task(v.items()[0][0],dist[v.items()[0][0]])