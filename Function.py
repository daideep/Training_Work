
num = '123'
print(num[-1:])

print('----------------------')
#Write a function getSumOfLastDigits() that takes in a list of positive numbers and returns the sum of all the last digits in the list.

def getSumOfLastDigits(numList):
    total = 0
    for item in numList:
        newItem = str(item)
        last = newItem[len(newItem) - 1]
        total += int(last)
    return total

print(getSumOfLastDigits([22, 4, 234]))

print('--------------')

x = [3,2,11]
y = [10,2,1]
print(x+y)

x = [3,2,11]
sum = x[0] + x[-1]
print(sum)

#Define a function calls addFirstAndLast(x) that takes in a list of numbers and returns the sum of the first and last numbers.

def addFirstAndLast(x):

    if len(x) == 0:
        return 0
    elif len(x) == 1:
        return x[0]
    else:
        return x[0] + x[-1]

print(addFirstAndLast([10, 3, 52]))
print(addFirstAndLast([]))
print(addFirstAndLast([2]))

print('--------------')

# lambda Function to check even . Return True if its even or False

even = lambda x : x%2 == 0

print(even(11))
print(even(0))

print('--------------')
# In Python, it is possible to pass a function as a argument to another function. Write a function useFunction(func, num) that takes in a
# function and a number as arguments. The useFunction should produce the output shown in the examples given below.

def addOne(x):
    return x+1

def useFunction(func, x):
    return addOne(x)**2

print(useFunction(addOne, 4))

print('--------------')