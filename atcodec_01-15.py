s = input()
s = s[::-1]
ans = 0
for i in range(len(s)):
    ans +=  (ord(s[i]) - ord('A') + 1) * (26 ** i)
print(ans)

