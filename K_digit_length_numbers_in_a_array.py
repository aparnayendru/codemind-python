def dig(n):
    count=0
    if n==0:
        count+=1
    else:
        while n>0:
            n=n//10
            count+=1
    return count
a,b=map(int,input().split())
arr=list(map(int,input().split()))
n=0
for i in range(len(arr)):
    m=arr[i]
    if m<0:
        m=-(m)
        #print(m)
        count=dig(m)
    elif m>=0:
        count=dig(m)
    if count==b:
        n+=1
print(n)
    