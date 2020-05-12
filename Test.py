# 1. Write a program to print a list of numbers from 1to 50, replace every 3
# divisible number with “Fizz”, every 5 divisible number with “Buzz” and both 3
# and 5 divisible numbers with “FizzBuzz”.

num = range(1,51)

for i in num:
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

print('---------------------------')
#2. Write a program to print the given string along with underscores ‘_’ which is
#added to the same amount as the length of string.




print('---------------------------')
#3. Write a program to verify if two given strings are Anagram.

s1 = "listen"
s2 = "silent"

if sorted(s1) == sorted(s2):
    print('The strings are anagrams.')
else:
    print('Not Angram')


print('---------------------------')
#4.Write a program to delete first and last values from a list of any len

list = [0,1,2,3,5,6,"Deep"]

list = list[1:-1]

print(list)


print('---------------------------')
#5. Write a program to print a list of all indexes for a value in the list.

list = [1, 4, 5, 6, 7]

for i in range(len(list)):
    print(i,end='--')
    print(list[i])

print('---------------------------')
#6. Write a program to reverse key:value pair in a dictionary.

d = {1:'one', 2:'two', 3:'three'}

final = { v:k for k,v in d.items()}
#final = reversed(d)

print(final)


print('---------------------------')
#7. Write a program to print the Fibonacci series upto first ‘n’ given numbers.

def Fibonacci(n):
    f1 = 0
    f2 = 1
    if (n < 1):
        return 0
    for x in range(0, n):
        print(f2, end=" ")
        next = f1 + f2
        f1 = f2
        f2 = next

Fibonacci(4)


print('---------------------------')
#8. Write a program to replace every double vowel in the string with single vowel.

str = 'Daideep'
vowel = ['a','e','i','o','u']

for i in str.lower():
    if i in vowel:
        str = str.replace(i,'*')
print(str)


print('---------------------------')
#9. Write a program to find the union of two given lists.

l1 = [1,2]
l2 = [3,2]

union = l1 + l2

print(union)


print('---------------------------')
#10. Write a program to find the count of a given digit on book pages numbers of given size.




print('---------------------------')