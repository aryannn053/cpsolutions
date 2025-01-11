# AC

import bisect

n = int(input())
a = list(map(int, input().split()))

count = 0
for j in range(n):
    x = bisect.bisect_right(a, a[j] // 2) - 1
    count += max(0, x + 1)

print(count)