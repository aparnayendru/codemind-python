n=int(input())
arr=list(map(int,input().split()))
sum=0
base=1
d=0
for i in range(len(arr)):
    sum=sum*10+arr[i]
while sum!=0:
    r=sum%10
    d=d+r*base
    sum=sum//10
    base*=2
print(d)
