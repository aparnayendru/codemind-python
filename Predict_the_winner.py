n=int(input())
arr=list(map(int,input().split()))
diff=0
even=0
odd=0
for i in range(len(arr)):
    if i%2==0:
        even=even+arr[i]
    elif i%2!=0:
        odd=odd+arr[i]
diff=even-odd
if diff%4==0:
    print("X")
else:
    print("Y")