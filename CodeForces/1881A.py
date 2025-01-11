# aryan053
# stand proud, you're strong
 
import sys
import math
import bisect
from sys import stdin,stdout
from math import gcd,floor,sqrt,log
from collections import defaultdict as dd
from collections import Counter
from bisect import bisect_left as bl,bisect_right as br
 
inp    = lambda: int(input())
strng  = lambda: input().strip()
jn     = lambda x,l: x.join(map(str,l))
strl   = lambda: list(input().strip())
mul    = lambda: map(int,input().strip().split())
mulf   = lambda: map(float,input().strip().split())
seq    = lambda: list(map(int,input().strip().split()))
 
ceil   = lambda x: int(x) if(x==int(x)) else int(x)+1
ceildiv = lambda x,d: x//d if(x%d==0) else x//d+1
 
flush  = lambda: stdout.flush()
stdstr = lambda: stdin.readline()
stdint = lambda: int(stdin.readline())
stdpr  = lambda x: stdout.write(str(x))
 
mod = 1000000007

t = inp()

for i in range(t):
    n, m = mul()
    
    x = strng()
    s = strng()
    
    flag = True
    
    for j in range(6):
        if s in x:
            print(j)
            flag = False
            break
        x += x
    
    if flag:
        print(-1)