n = int(input())
s = input()
for i in range(1, n):
    l = 0
    for r in range(i, n):
        if s[l] == s[r]:
            break
        l += 1
    
    print(l)
