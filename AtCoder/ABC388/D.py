# TLE

n = int(input())
a = list(map(int, input().split()))

def change(arr):
    cnt = 0
    
    for i in range(len(arr)):
        if arr[i] >= 1:
            arr[i] -= 1
            cnt += 1
    
    return (arr, cnt)

for i in range(1, n):
    res = change(a[:i])
    a[:i] = res[0]
    a[i] += res[1]
    

print(a)