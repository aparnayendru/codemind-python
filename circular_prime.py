def prime(n):
    count=0
    for i in range(2,n):
        if n%i==0:
            count=1
            return False
    if count==0:
        return True
a=int(input())
sum=0
if prime(a):
    temp=a
    while(temp!=0):
        r=temp%10
        sum=sum*10+r
        temp=temp//10
    if prime(sum):
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")