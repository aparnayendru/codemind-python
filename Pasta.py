n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
x=0
count=0
for i in range(len(b)):
    for j in range(len(a)):
        if b[i]==a[i]:
            count+=1
    if count>0:
        x+=1
if x>0:
    print("Yes")
else:
    print("No")