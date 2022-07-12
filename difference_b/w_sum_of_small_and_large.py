s=input()
s=s.split()
a=0
b=0
diff=0
for words in s:
    c=min(words)
    d=max(words)
    a=a+ord(c)
    b=b+ord(d)
diff=abs(a-b)
print(diff)