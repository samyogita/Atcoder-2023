n = int(input())
s = input()
t = input()
similar = True
for r in range(n):
    if s[r] == t[r]: 
        continue
    if (s[r] == 'o' and t[r] == '0') or (s[r] == '0' and t[r] == 'o'):
        continue
    elif (s[r] == 'l' and t[r] == '1') or (s[r] == '1' and t[r] == 'l'):
        continue
    elif s[r] != t[r]:
        similar = False
        break
    
print('Yes' if similar else 'No')

    