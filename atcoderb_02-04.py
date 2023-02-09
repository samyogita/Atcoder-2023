n, k = list(map(int, input().split()))
arr = []
for _ in range(n):
    s = input()
    arr.append(s)
ans = arr[:k]
print(*sorted(ans), sep = '\n')
