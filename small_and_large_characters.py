s=input()
s=s.split()
for words in s:
    print(min(words),end=" ")
    print(max(words),end=" ")