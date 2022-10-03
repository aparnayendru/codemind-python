a,b=map(int,input().split())
m=list(map(int,input().split()))
n=list(map(int,input().split()))
x=[]
for i in m:
    if i in n and i not in x:
        x.append(i)
print(*x)