n=int(input())
left=2
right=2
while left*2<=n:
    left=left*2
right=left*2
if n-left<right-n:
    print(n-left)
elif n-left==right-n:
    print(left,right,end=" ")
else:
    print(right-n)