n=int(input())
arr=list(map(int,input().split()))
sum=0
count=0
y=0
for i in range(len(arr)):
    sum=sum+arr[i]
    count+=1
avrg=sum/count
for i in range(len(arr)):
    if int(avrg)==arr[i]:
        y=1
        break
if y==0:
    print("False")
else:
    print("True")