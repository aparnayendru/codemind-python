n=int(input())
arr=list(map(int,input().split()))
sum=0
count=0
countt=0
for i in range(len(arr)-1,-1,-1):
    sum=sum+arr[i]
    count+=1
avrg=sum/count
for i in range(len(arr)):
    if arr[i]>=int(avrg):
        countt+=1
print(countt)