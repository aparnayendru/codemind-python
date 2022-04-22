n=int(input())
sum=0
a=n*n
r=0
while(a>0):
    r=a%10
    sum=sum+r
    a=a//10
if(n==sum):
    print("Neon Number")
else:
    print("Not Neon Number")