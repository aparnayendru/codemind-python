t=int(input())
temp=0
count=0
r=0
while t>0:
    count=0
    a,b=map(int,input().split())
    for i in range(a,b+1):
        r=0
        temp=i
        r=temp%10
        if r==2 or r==3 or r==9:
            count=count+1
    print(count)
    t=t-1