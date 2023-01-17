a, b = list(map(int, input().split()))
a, b = max(a,b), min(a,b)
if a//2 == b:
    print('Yes')
else:
    print('No')