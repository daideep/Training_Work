
#Write a function removeFirstAndLast(list) that takes in a list as an argument and remove the first and last elements from the list.
# The function will return a list with the remaining items.

def removeFirstAndLast(numbers):

    new = numbers

    new.pop(0)
    # if not new:
    #     return new
    new.pop(-1)
    return new

print(removeFirstAndLast([1, 4, 8]))

print('---------------')
# In Python, variables are linked to objects by references.

a = [4, 5, 6 ]
b = a
b[0] = 1

# print(b)

print(a)

a[2] = 3

print(a)
print(b)

print('---------------')

a = [4, 5, 6]
b = a[:]
b[0] = 1
a[2] = 3

print(a)
print(b)


print('---------------')

