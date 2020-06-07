# Mode = 'r' , 'w' , 'a'
#  r = read
#  w = write
#  a = append
#  w+ = write and read
#  a+ = append and read

# read()    - read all the data
# read(1)   - read 1 character
# readline  - read 1 line
# readlines - read all lines - Return [as list]

f = open('test.txt','a+')

f.write('This is 1st Line \n')
f.write('This is 2nd Line')

f.read()

f.close()

print('--------------')


def addEmail(filename, name, email):
    f = open('emails.txt', 'a')  # replace the mode

    # Append name and email, each record should end with '\n'.
    f.write('Name is :'name)
    
    # close file
    f.close()

    return f  # do not remove this line

print(addEmail('emails.txt', 'Mary', 'mary@gmail.com'))
