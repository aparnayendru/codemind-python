s1=input().lower().split()
s2=input().lower().split()
c=0
l=[]
for i in set(s1):
    if i in set(s2):
        l.append(i)
print(len(l))
