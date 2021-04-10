def find_sum(**kwargs):
    return sum(kwargs.values())
    
print(find_sum(a=1,b=2,c=3))


myString = "Amigos Para sampre"
#Get certain no of chars in a string
print(myString[0:5])


def foo(character, filepath="bear.txt"):
    file = open(filepath)
    content = file.read()
    return content.count(character)

print(foo("f"))


with open("bear.txt") as file:
    content = file.read()

with open("first.txt", "w") as file:
    file.write(content[:90])
    
    
with open("bear1.txt") as file:
    content = file.read()

with open("bear2.txt", "a") as file:
    file.write(content)