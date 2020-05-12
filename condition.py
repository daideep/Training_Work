#Write a function isIsosceles(x, y, z) that accepts the 3 sides of a triangle as inputs.
# The function should return True if it is an isosceles triangle.
def isIsosceles(x, y, z):
    x = abs(x)
    y = abs(y)
    z = abs(z)

    if x == y or y == z or z == x:
        return True
    else:
        return False

print(isIsosceles(-3, 1, 3))

print('----------------------')
def isScalene(x, y, z):
    x = abs(x)
    y = abs(y)
    z = abs(z)

    if x != y and y != z and z != x:
        return True
    else:
        return False

print(isScalene(2, 1, 3))


print('----------------------')

def isPrime(x):
    for i in range(2,x):
        if(x % i == 0):
            return False
    return True

print(isPrime(11))
print(isPrime(0))



print('----------------------')



print('----------------------')




print('----------------------')