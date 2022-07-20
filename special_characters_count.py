s=input()
s=s.lower()
y="@!~`#$%^&*():;><=?.,/|{}-_[]"
count=0
for ch in s:
    if ch in y:
        count+=1
print(count)