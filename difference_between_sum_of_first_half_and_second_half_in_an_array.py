n=int(input())
arr=list(map(int,input().split()))
m=n//2
sum=0
summ=0
for i in range(m):
    sum=sum+arr[i]
for i in range(m,len(arr)):
    summ=summ+arr[i]
print(abs(sum-summ))
