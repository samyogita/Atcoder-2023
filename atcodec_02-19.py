n , k = list(map(int, input().split()))
A = list(map(int, input().split()))
a = set(A)
count = 0
arr = sorted(list(a))
prev = -1
for x in arr:
    if x != prev + 1 or count == k:
        break
    prev = x
    count += 1

print(prev+1)