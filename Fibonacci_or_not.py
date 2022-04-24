n=int(input())
n1=0
n2=1
n3=0
count=0
for i in range(2,n):
    n3=n1+n2
    if n3==n:
        count+=1
    n1=n2
    n2=n3
if count>0:
    print("True")
else:
    print("False")