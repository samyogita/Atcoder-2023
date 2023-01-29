
import sys
sys.setrecursionlimit(200001)
from collections import defaultdict

n, m = list(map(int, input().split()))
vis = set()
g = defaultdict(list)
one = 0
ans = True
def dfs(node):
    vis.add(node)
    for child in g[node]:
        if child not in vis:
            dfs(child)

for i in range(m):
    u, v = list(map(int, input().split()))
    g[u].append(v)
    g[v].append(u)

dfs(1)

if len(vis) != n:
    ans = False

for key, value in g.items():
    if len(g[key]) == 1:
        one += 1
    elif len(g[key]) > 2:
        ans = False

if one != 2:
    ans = False

print('Yes' if ans else 'No')





    
