t=int(input())
while t>0:
    n=int(input())
    a=list(map(int,input().split()))
    o=0
    for i in range(n):
        if a[i]%2!=0:
            o+=1
    print(o//2)
    t=t-1