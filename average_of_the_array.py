n=int(input())
arr=list(map(int,input().split()))
sum=0
count=0
for i in range(len(arr)):
    sum=sum+arr[i]
    count+=1
avrg=sum/count
print('%.2f' %avrg)