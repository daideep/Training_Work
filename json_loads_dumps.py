
# import json
#
# # result = json.loads('{"name":["Daideep", "deep"], "age":["10","20"]}')
# # print(result)
#
# final = json.loads('C:\Python\Training_Work\1.json')
# print(final)

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])