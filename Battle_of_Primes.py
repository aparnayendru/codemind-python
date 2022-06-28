def prime(n):
    count=0
    for i in range(2,n):
        if n%i==0:
            count=1
            return False
    if count==0:
        return True
a=int(input())
b=int(input())
for i in range(1,100):
    c=a+b+i
    if prime(c):
        print(i)
        break