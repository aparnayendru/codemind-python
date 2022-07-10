m,n=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=set(a)
d=set(b)
count=0
for ele in c:
    if ele not in d:
        count+=1
for ele in d:
    if ele not in c:
        count+=1
print(count)