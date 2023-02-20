n , k = list(map(int, input().split()))
s = input()
count = 0
ans = ''
for i in range(n):
    if s[i] == 'x' and count == k:
        ans += 'x'
    elif s[i] == 'o' and count !=k : 
        ans += 'o'
        count += 1
    else: 
        ans += 'x'   
print(ans)


