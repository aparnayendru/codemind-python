n=int(input())
sum=0
prod=1
r=0
sub=0
while n>0:
    r=n%10
    sum=sum+r
    prod=prod*r
    n=n//10
sub=prod-sum
print(sub)