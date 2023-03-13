n = int(input())
A = list(map(int, input().split()))
ans = [0] * (n+1)
res = []
for i in range(n):
    if ans[i+1] == 0:
        ans[A[i]] = 1
for j in range(1, n+1):
    if not ans[j]:
        res.append(j)
print(len(res))
print(*res)

