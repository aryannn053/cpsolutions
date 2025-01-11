# AC

n = int(input())
a = list(map(int, input().split()))

res = set()

for i in range(n):
    for j in range(i+1, n):
        if a[i] < (a[j]//2):
            res.add([a[i], a[j]])

print(len(res))