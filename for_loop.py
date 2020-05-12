sum = 0
def addNumbers(num):
    global sum
    for i in range(1,num+1):
         sum = sum + i
    print(sum)

addNumbers(3)


print('------------------')

def sumOfDigit(num):
    sum = 0
    for i in str(num):
        #print(i)
        sum = sum + int(i)

    print(sum)

sumOfDigit(4101)

print('----------')

print(dict(str))
