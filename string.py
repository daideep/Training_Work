str = "Hello everyone"
print(str.find('e'))

print('-----------------------')

# palindrom or not
str = 'nayan'

if str == str[::-1]:
   print('palindrom')
else:
   print('Not palindrom')

print('-----------------------')

str = 'hello world i am here'

word = str.split()

print(word)
# print(type(word))

#word.sort()

for i in sorted(word):
     print(i," ")

print('------------------------------------')

#Write the function countA(word) that takes in a word as argument and returns the number of 'a' in that word.

def countA(word):
    count = 0
    for i in word:
        if i == 'a':
           count = count + 1
    print(count)

countA('bananA')

print('--------------------')

# Write a function removeLetter(word, letter) that takes in a word and a letter as arguments and remove all the occurrence of that particular letter from the word.
# The function will returns the remaining leters in the word.

# removeLetter("apple", "p")
# 'ale'

def removeLetter(word, letter):
    print(word.replace(letter, ''))

removeLetter('Hello', 'l')

print('----------------')

# def getChar(word,pos):
#     print(word.find(pos))
#
# getChar('apple',3)

print('----------------')

# def getChar(word,pos):
#     if pos > len(word):
#         print('Invalid Range')
#     else:
#         print(word[pos])

#getChar('apple', 3)

print('-----------------')

#for i in 'daideep':
i = 'aeiou'
if i in 'daideep':
    print(i.upper())

    # if i in ['a', 'i', 'o', 'u']:
    #     print(i.upper())

def capitalizeVowels(word):
    i = 'aeiou'
    if i in word:
        print(i.upper())


capitalizeVowels('apple')
