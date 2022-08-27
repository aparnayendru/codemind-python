def gcd(a,b):
    i=1
    gcdd=0
    while i<=a and i<=b:
        if a%i==0 and b%i==0:
            gcdd=i
        i+=1
    return gcdd
t=int(input())
for i in range(0,t):
    n,a,b,k=map(int,input().split())
    p=gcd(a,b)
    count=(n/a)+(n/b)-2*(n/((a*b)/(p)))
    if abs(count)>=k:
        print("Win")
    else:
        print("Lose")