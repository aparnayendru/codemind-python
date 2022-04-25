n=input()
x=n.split()
count=0
max=0
for word in x:
    count=0
    for character in word:
        count=count+1
    if count>max:
        max=count
print(max)