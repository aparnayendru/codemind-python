n=int(input())
sum=0
prod=1
r=0
temp=n
while(temp>0):
    r=temp%10
    sum=sum+r
    prod=prod*r
    temp=temp//10
if(sum==prod):
    print("Spy Number")
else:
    print("Not Spy Number")
    
    