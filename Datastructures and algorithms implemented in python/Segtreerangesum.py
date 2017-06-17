#Working Range "maximum" Query on segment tree



def create(node,start,end):

	if(start==end):
		#print segtree,start,node
		segtree[node] = arr[start]
	else:
		mid = start+end
		mid /= 2
		create(2*node+1,start,mid)
		create(2*node+2,mid+1,end)
		#print node
		segtree[node] = (segtree[2*node+1]+segtree[2*node+2])


def query(node,st,en,left,right):

	if(left<=st and right>=en): 	# Total overlap
		#print node
		return segtree[node]
	elif(left>en or right<st):
		return 0
	else:
		mid = st+en
		mid /= 2
		q1 = query(2*node+1,st,mid,left,right)
		q2 = query(2*node+2,mid+1,en,left,right)
		return q1+q2


def update1(node,st,en,i,val):		#TO find the node which is to be updated

	if(st==en==i):
		segtree[node]=val
		return node
	elif(st>i or en<i):
		return 
	else:
		mid = st+en
		mid /= 2
		#print st,en
		val1 = update1(2*node+1,st,mid,i,val)
		val2 = update1(2*node+2,mid+1,en,i,val)
		if(val1 is not None):
			return val1
		if(val2 is not None):
			return val2




def update2(node):				# Updating all the nodes using bottom up approach
	while(node!=0):
		if(node%2==0):		#if it's right child
			par = (node-1)/2
			segtree[par] = (segtree[node]+segtree[node-1])
		else:				#left child
			par = (node-1)/2
			segtree[par] = (segtree[node]+segtree[node+1])
		node = (node-1)/2
		


n = int(raw_input())	
arr = map(int,raw_input().split())

segtree = [0 for i in range(4*n)]

create(0,0,n-1)

print segtree
#def query(node,st,en,left,right):

print query(0,0,n-1,3,4)

x = update1(0,0,n-1,3,10)
print x
update2(x)
print segtree






