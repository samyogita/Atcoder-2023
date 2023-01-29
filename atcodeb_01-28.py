n, m = list(map(int, input().split()))
l = []
t = set()
ans = 0
for i in range(n):
    val = input()
    l.append(val[-3:])
for j in range(m):
    T = input()
    t.add(T)
for items in l:
    if items in t:
        ans += 1
print(ans)

