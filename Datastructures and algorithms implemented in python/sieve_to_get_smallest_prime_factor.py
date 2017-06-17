import itertools
import collections

import math
MAX = 10**6+1
prim = [1]*(MAX)#[0 for i in range(MAX)]
barr = [0]*(MAX)#[] for i in range(MAX)]
 
numprim = [] 
 
for i in xrange(2,MAX,2):
    prim[i] = 2
 
for i in xrange(3,MAX,2):
    if(barr[i]==0):
        prim[i] = i
        j = i
        while(j*i<MAX):
            if(barr[j*i]==0):
                barr[j*i] = 1
                prim[i*j] = i
            j+=2
prim[0] = 1
prim[1] = 2
#prim contains the lowest prime factor of ith index
for i in xrange(1,10**6+1):
    if(prim[i]==i):
        numprim.append(i)
print numprim
#numprim contains list of primes from 0 to 10**6+1














