# aryan053
# stand proud, you're strong
 
import sys
import math
import bisect
from sys import stdin,stdout
from math import gcd,floor,sqrt,log
from collections import defaultdict as dd
from collections import Counter
import string
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

s = input()
x = [0] * 26
for i in range(26):
    x[ord(s[i]) - ord("A")] = i
ans = 0
for i in range(25):
    ans += abs(x[i] - x[i + 1])
print(ans)