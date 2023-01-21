n , p, q, r, s = list(map(int, input().split()))
A = list(map(int, input().split()))
for i in range(q-p+1):
    A[i+p-1], A[i+r-1] = A[i+r-1], A[i+p-1]
print(*A)