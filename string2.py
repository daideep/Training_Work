
#Write the function startEndVowels(word) that prints True if the word starts and ends with vowels.

def startEndVowels(word):
    if word[0] and word[-1] in ['a', 'e', 'i', 'o', 'u']:
        print('true')
    else:
        print('false')

startEndVowels('apple')
startEndVowels('elephant')

print('-------------------')

if 'daideep' in 'hello daideep':
    print('333333')

vowel = ['a', 'e', 'i', 'o', 'u']
if 'i' in vowel:
    print('22222222')

print('-------------------')

def removeVowels(word):
    vowel = ['a', 'e', 'i', 'o', 'u']
    for char in word:
        if char in vowel:
            word = word.replace(char, '')

    print(word)

removeVowels('Daideep')

print('-------------------')


def startWithVowel(word):
    #vowel = ['a', 'e', 'i', 'o', 'u']

    if word[0] in 'aeiou':
        return word
    else:
        for i in range(1, len(word)):
            if word[i] in 'aeiou':
                 return word[i:]
        return "No vowel"

print(startWithVowel('DDeep'))
print(startWithVowel('apple'))

print('-------------------')

def getCommonLetters(word1,word2):

    for letter in word1:
        if letter in word2:
            #return letter
            return ''.join(sorted(letter))
    return ''

print(getCommonLetters('aipple','dieepa'))

print('-------------------')

def mirrorText(w1,w2):

    one = w1 + w2
    two = w2 + w1

    return one + two

print(mirrorText('hello','world'))

print('-------------------')

def isPalindrome(word):
    if word == word[::-1]:
       return True
    else:
       return False

print(isPalindrome('kanak'))
print(isPalindrome('1211'))

print('-------------------')

def isInAlphabeticalOrder(word):

    if word == ''.join(sorted(word)):
        return True
    else:
        return False

print(isInAlphabeticalOrder('daideep'))
print(isInAlphabeticalOrder('abc'))


print(list(range(0,4,3)))


def isAnagram(w1, w2):
   w1 = w1.lower()
   w2 = w2.lower()
   if sorted(w1) == sorted(w2):
        return True
   else:
        return False

print(isAnagram('Deepa', 'peeda'))
print(isAnagram('Deepp', 'peeda'))