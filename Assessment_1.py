'''Write a program to print a list of numbers from 1to 50, replace every 3
divisible number with “Fizz”, every 5 divisible number with “Buzz” and
both 3 and 5 divisible numbers with “FizzBuzz”.'''

#def fizzbuzz():
for i in range(1,51):
    if i % 3 == 0 and i % 5 == 0:
        print(i ,'is fizzbuzz')
    elif i % 3 == 0:
        print(i,'is fizz')
    elif i % 5 == 0:
        print(i , 'is buzz')
    else:
         print(i ,'is not fizzbuzz')

#fizzbuzz()

print('--------------------------------')
#Take 10 integers from keyboard using loop and print their average value on the screen.


#L = list(range(10,101,10))
#print(L)

num = 0

for i in range(1,11):
    #print(i)
    num = num + i
    avg = num / i

print(avg)

print('--------------------------------')
#Print the following patterns using loop

# def pattern():
#     print('*')
#     print('**')
#     print('***')
#     print('****')
#
# pattern()

star = ['*','**','***','****']

for i in star:
      print(i)

print('--------------------------------')
#Print the following patterns using loop

list = ['1010101',' 10101 ','  101  ','   1   ']

for i in list:
    print(i)

print('--------------------------------')
#Print multiplication table of 24, 50 and 29 using loop.

num = 50

for i in range(1,11):
    total = num * i
    print(num ,'*', i , '=', total)

print('--------------------------------')
#Write a program to calculate the factorial of a number.
#Factorial of any number n is represented by n! and is equal to
# 1*2*3*....*(n-1)*n. E.g.-
# 4! = 1*2*3*4 = 24
# 3! = 3*2*1 = 6
# 2! = 2*1 = 2

num = 1

def factorial(n):
    global num
    for i in range(1,n+1):
         num = num * i
    print(num)

factorial(5)

print('--------------------------------')
#What are the different data types in python

number = 10       #int
number = 10.34    #float
number = 10 + 5j  #complex
n1,n2,n3 = 5, 5.5, 5+2j
print(n1,n2,n3)

string1 = "Hello"
string2 = "10"
print(string1,string2)

list = [55, 'daideep', 3.5 , (15,20,25)]
print(list)

list[3] = 60
print(list)

tuple = ('deep',4,5,6.7)
print(tuple)

set = {1,3,7,6,6,4,3,2,1}
print(set)

dict = {'name' : 'daideep',
        'salary' : 5000,
        'email' : 'dpate218@nyit.edu'
       }
print(dict)

print('-------------------')
#Write an infinite loop
#An infinite loop never ends. Condition is always true.



















