
# for i in ['a','b','c']:
#     print(i**2)

try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print('unsupported operand Type')

print('---------------')

x = 5
y = 10
print(x+y)

print('---------------')

try:
    x = 5
    y = 0

    z = x/y

except ZeroDivisionError as msg:
    print( msg, ":: Can not divide by zero")

finally:
    print("All done")


print('---------------')

# import math
#
# def ask():
#     while True:
#         try:
#             num = int(input('Input Integer: '))
#         except:
#             print('Error Occur!')
#             continue
#         else:
#             print('Thank You! Your number is : {}'.format(math.sqrt(num)))
#             break
#
# ask()

print('---------------')


from math import pow

def square():
    while True:
        try:
            n = int(input('Input Integer: '))

        except ValueError as txt:
            print('Error is -' , txt)
            print('Try Again')

        else:
            sqr = pow(n,2)
            print(sqr)
            break

        # finally:
        #     print('Try Again')
        #     break

square()





