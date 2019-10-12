# x = lambda a : a + 10
# print(x(8))

# x =lambda a, b, c:a*b*c
# print(x(5,7,8))


# def myfunc(n):
#   return lambda a : a * n

# mytripler = myfunc(3)

# print(mytripler(11))

# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)

# print(mydoubler(11))


# def myfunc1(n):
#     return lambda a:a**n

# SQRT3=myfunc1(3)
# print(SQRT3(4))
# import re

# stringline="Search the string to see if it starts w"
# newstr=stringline.replace(stringline[0],"P")
# print(newstr)
# key="it starts w"
# te=re.search(key,stringline)
# # print(te.pos)
# print(te.start())
# print(te.end())
# substring=stringline[:te.start()]+stringline[te.end():]
# print(substring)


# import re

# str = "The rain in Spain"
# x = re.sub("\s", "9",str)
# print(x)

import re

def mysearchfunc(key,strline):
key="the"
strline="Search the string to see if it starts "
if key in strline:
    print(strline.index(key))
else:
    print("none")

