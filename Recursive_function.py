
#Write a recursive function addDashes() that takes in a string and returns a new string with all the characters separated by a "-".

def addDashes(s):
    if len(s) < 1:
        return None
    elif len(s) == 1:
        return s
    else:
        return s.split("-")

print(addDashes('deep'))

