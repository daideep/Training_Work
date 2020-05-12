
a={1:"A",2:"B",3:"C"}
for i,j in a.items():
    print(i,j,end="-")
    # print(i,j)
    # print(i)
    # print(j)

print('--------------------')

for i in 'dp':
    print(i)

print('------------------')

a={1:"A",2:"B",3:"C"}
print(a.get(1,4))
print(a.get(4))
print(a.get(3))
print(a.get(1,3))
print(a.get(5,4))

print('------------------')

a = {1:"A",2:"B",3:"C"}

print(a.setdefault(3))
print(a.setdefault(4,"D"))

print('------------------')

a={1:"A",2:"B",3:"C"}
b={4:"D",5:"E"}

a.update(b)
print(a)

print('------------------')

a = {1:"A",2:"B",3:"C"}
b = a.copy()

b[2] = "D"
print(a)

a = {1:"A",2:"B",3:"C"}
b = a

b[2] = "D"
print(a)

print('------------------')

a={1:"A",2:"B",3:"C"}
a.clear()
print(a)

print('------------------')

#A DNA strand consisting of the 4 nucleotide bases is usually represented with a string of letters: A,T, C, G.
#Write a function that computes the base composition of a given DNA sequence.

def baseComposition(dna_seq):

    if len(dna_seq) == 0:
        return {'A': 0, 'T': 0, 'C': 0, 'G': 0}

    return {i: dna_seq.count(i) for i in dna_seq}

print(baseComposition('AGTTCFM'))

print('------------------')

# A sparse vector is a vector whose entries are almost all zero, like [1, 0, 0, 0, 0, 0, 0, 2, 0]. Storing all those zeros wastes memory and dictionaries are commonly used to keep track of just the nonzero entries.
# For example, the vector shown earlier can be represented as {0:1, 7:2}, since the vector it is meant to represent has the value 1 at index 0 and the value 2 at index 7. Write a function that converts a dictionary back to its sparese vector representation.


def convertDictionary(dictionary):

    if len(dictionary) == 0:

        return []

    return [dictionary.get(i) if i in dictionary.keys() else 0 for i in range(max(list(dictionary.keys()))+1)]

    # for i in range(max(list(dictionary.keys()))+1):
    #     if i in dictionary.keys():
    #         return dictionary.get(i)
    #     else:
    #         return 0

print(convertDictionary({0: 1, 3: 6, 7: 3, 12: 3}))
#print(convertDictionary({}))