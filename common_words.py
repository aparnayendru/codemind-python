s=input().lower().split()
#print(s)
t=input().lower().split()
#print(t)
if len(s)>len(t):
    for words in s:
        if words in t:
            print(words,end=" ")
else:
    for words in t:
        if words in s:
            print(words,end=" ")