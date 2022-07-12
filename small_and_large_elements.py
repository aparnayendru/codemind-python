s=input()
s=s.split()
for words in s:
    print(min(words),end=" ")
    break
for i in range(len(s)-1,-1,-1):
    x=s[i]
    print(max(x),end=" ")
    break
    