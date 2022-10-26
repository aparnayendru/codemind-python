n=int(input())
c=0
a=1
for i in range(a*a,n+1):
    if i*i==n:
        c=1
        print("True")
        break
if c==0:
    print("False")