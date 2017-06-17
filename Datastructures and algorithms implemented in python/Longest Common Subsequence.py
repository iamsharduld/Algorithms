n,m = map(int,raw_input().split())
arr1 = map(int,raw_input().split())
arr2 = map(int,raw_input().split())
dp = [[0 for i in range(m+1)] for j in range(n+1)]	#Initialize the table with zeroes



for i in xrange(1,n+1):			#Populating the array from top to bottom	
	for j in xrange(1,m+1):
		if(arr1[i-1]==arr2[j-1]):
			dp[i][j] = dp[i-1][j-1]+1
		else:
			dp[i][j] = max(dp[i][j-1],dp[i-1][j])


ans = []
i = len(arr1)
j = len(arr2)
while i>0 and dp[i][j]!=0:			#traverse the dp array in reverse to find out the actual LCS
	while j>0 and dp[i][j]!=0:
		if(arr1[i-1]==arr2[j-1]):
			ans.append(arr1[i-1])	#Saving the diagonal traversals in array
			i-=1
			j-=1
		else:
			if(dp[i][j]==dp[i-1][j]):
				i-=1
			else:
				j-=1



for i in ans[::-1]:
	print i,