t=int(input())
sum=0
r=0
temp=0
while t>0:
    sum=0
    n=int(input())
    temp=n
    while(temp>0):
        r=temp%10;
        sum=sum*10+r
        temp=temp//10
    if sum==n:
        print("True")
    else:
        print("False")
     
    