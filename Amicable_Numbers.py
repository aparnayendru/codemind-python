a=int(input())
b=int(input())
sum=0
prod=0
for i in range(1,a):
    if a%i==0:
        sum=sum+i
for j in range(1,b):
    if b%j==0:
        prod=prod+j
if sum==b and prod==a:
    print("Amicable")
else:
    print("Not Amicable")