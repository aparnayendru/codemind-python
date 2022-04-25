n=input()
count=0
for character in n:
    if character.islower():
        count=count+1
print(count)