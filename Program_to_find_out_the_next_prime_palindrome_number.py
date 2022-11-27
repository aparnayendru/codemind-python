def prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def pal(n):
    temp=n
    sum=0
    while n!=0:
        r=n%10
        sum=sum*10+r
        n=n//10
    if temp==sum:
        return True
    else:
        return False
n=int(input())
while n>0:
    n+=1
    if pal(n) and prime(n):
        print(n)
        break

