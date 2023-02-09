import sys
sys.setrecursionlimit(200001)
from collections import defaultdict
cnt = 0
def dfs(node):
    vis[node] = 1
    for child in g[node]:
        if vis[child] == 0:
            dfs(child) 

n, m = list(map(int, input().split()))
g = defaultdict(list)
vis = [0] * int(n+1)
for _ in range(m):
    u, v = list(map(int, input().split()))
    g[u].append(v)
    g[v].append(u)

for k in range(1, n+1):
    if vis[k] == 0:
        cnt += 1
        dfs(k)

print(m-n+cnt)
