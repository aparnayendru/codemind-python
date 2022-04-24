n=int(input())
temp=0
r=0
sum=0
t=0
temp=n
while temp>0:
    temp=temp//10
    t=t+1
temp=n
while temp>0:
    r=temp%10
    sum=sum+pow(r,t)
    temp=temp//10
    t=t-1
if sum==n:
    print("True")
else:
    print("False")