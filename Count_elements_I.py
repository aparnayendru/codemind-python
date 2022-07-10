m,n=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=set(a)
d=set(b)
count=0
for ele in c:
    if ele in d:
        count+=1
print(count)