import copy

text = "Hello, everyone!"
myList = list(text)

print(id(myList))
print(myList)

copyList = copy.copy(myList)
copyList.append("+")

print(id(copyList))
print(copyList)