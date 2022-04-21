s=input()
sum=0
for character in s:
    if character.isdigit():
        sum=sum+int(character)
print(sum)