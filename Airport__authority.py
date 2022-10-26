n=int(input())
l=[]
for i in range(n):
    k=int(input())
    l.append(k)
t=int(input())
c=0
for i in range(len(l)):
    if l[i]<=t:
        c+=1
    elif l[i]>t:
        c+=2
print(c)