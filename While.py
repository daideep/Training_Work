
def addNumbers(num):
	total = 0
	i = 1
	while i <= num:

		total = total + i
		i = i + 1
	return total

print(addNumbers(3))

print('-------------------')

# cnt = 0
# while True:
#     while cnt<10:
#         cnt+=1
#         #print(cnt)
#         if cnt>10:
#             break
#         print(cnt)

print('-------------')
# Factorial
num = 3
total = 1
for x in range(1,num+1):
    total = total * x

print(total)

