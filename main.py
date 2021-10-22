a = [*range(1, 299)]

print("The list is: ")
for i in a:
    print(i)

print("----------------")

print("The length is: ", len(a))

print("----------------")

print("The squared values are: ")
for j in a:
    print(j ** 2)

print("----------------")

if 57 in a:
    print("Yes it 57 exists in the list")