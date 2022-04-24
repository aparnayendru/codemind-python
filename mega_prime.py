n=int(input())
count=0
m=0
r=0
sum=0
for i in range(2,n):
    if(n%i==0):
        count=count+1
if(count==0):
    while n>0:
        sum=0
        r=n%10
        for j in range(2,r):
            if r%j==0:
                sum=sum+1
        if r==1:
            m=m+1
        n=n//10
if count==0 and sum==0 and m!=1:
    print("Mega Prime")
else:
    print("Not Mega Prime")