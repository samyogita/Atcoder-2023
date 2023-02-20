n, m = list(map(int, input().split()))
A = list(map(int, input().split()))
b = list(map(int, input().split()))
sum = 0
for i in b:
    
    sum += int(A[i-1])

print(sum)
