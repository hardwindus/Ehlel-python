# # tuple=('a','b','c')
# tuple1=('a','b','c')
# tuple2=('a1','b1','c1')

# # a=tuple1
# # tuple1=tuple2
# # tuple2=a
# tuple1,tuple2=tuple2,tuple1

# print(tuple1)
# print(tuple2)


# a={"hello" : "сайн уу",
#    "bye" : "баяртай",
#    "name" : "нэр"}
# print(a)

# print(a["hello"])
# print(a.get("hello"))

# if("hello" in a):
#     print("hello tulhuur bna")
# else:
#     print("hello tulhuur baihgui")

# үг нэмэх
# үг хайх

# dictionary={}
# dictionary["hello"]="сайн уу"
# status="running"

# def addword(eng,mon):
#     dictionary[eng]=mon
#     print(dictionary)

# def translate(eng):
#     if(eng in dictionary):
#         return dictionary[eng]
#     else:
#         return "орчуулга олдсонгүй"



# while(status=="running"):

#     print("A - үг нэмэх")
#     print("S - үг хайх")
#     print("E - гарах")

#     choice=input("та үйлдлээ сонгоно уу: ")
#     if(choice=="A" or choice=="a"):
#         print("Үг нэмэх үйлдэл хийнэ.")
#         eng=input("ENG:")
#         mon=input("MON:")
#         addword(eng,mon)
#     elif(choice=="S" or choice=="s"):
#         eng=input("Үгээ оруулна уу:")
#         translateword=translate(eng)
#         print(translateword)
#     elif(choice=="E" or choice=="e"):
#         status="exit"
#     else:
#         print("Буруу комманд!")
# a-z
# A-Z
# 0-9
# # _
# def add(a,b):
#     print(a+b)

# def main():
#     print("I am main function") 
#     add(7,8)


# def  selfCallingFunc(too):
#         selfCallingFunc(too-1)


# selfCallingFunc(5)

##RECURSIVE FUNCTION example
# def factorial(n):
#     if(n==1):
#         return 1
#     else:
#         return n*factorial(n-1)

# print(factorial(5))

# import math
# print(math.factorial(15))

#default value
# def printer(text = "Default text"):
#     print(text)

# printer("хэвлүүлэх текст")
# printer()


# #олон элемэнттэй аргумент

# def listhandler(thelist):
#     for x in thelist:
#         print(x)
# # listhandler([1,"neg","abc",("a1,").{"a":1}])

# def named(arg1, arg2="A"):
#     print("arg1 = "+arg1)
#     print("arg2 = "+arg2)

# named(arg1="neg")

# def manyargs(*args):
#     urt=len(args)
#     print("ta "+str(urt) + " shirheg ugugdul damjuulsan bna")
#     if(1 in args):
#         print("1 bna")
#     # print(args)

# manyargs(1,2,3,4,"dg")

#calculater
# - N nemeh
# - H hasah
# - U urjih
# - D huvaah
# - E exit

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multi(a,b):
    return a*b

def div(a,b):
    return a/b

def sqrt(a,b):
    return a**b

funcs ={"n": add,
        "N": add,
        "h" ,"H": sub,sub,
        "d": div,
        "u": multi,
        "s": sqrt
}
isrunning=True

while(isrunning):
    print("N nemeh , H hasah, U urjih, D huvaah,S zereg, E exit")
    choice=input("Үйлдэлээ сонгоно уу: ")
    if(choice=="e"):
        isrunning=False
    elif(choice in funcs):
        a=float(input("a = "))
        b=float(input("b = "))
        print(funcs[choice](a,b))
    else:
        print("Буруу утга оруулсан байна")

# status="running"
# s=0
# numb1=int(input("number1: "))
# numb2=int(input("number2: "))
# while(status=="running"):        

#     # print("N nemeh")
#     # print("H hasah")
#     # print("U urjih")
#     # print("D huvaah")
#     # print("E exit")
#     print("N nemeh , H hasah, U urjih, D huvaah,S zereg, E exit")

#     choice=input("Үйлдэлээ сонгоно уу: ")


#     if(choice=="N" or choice=="n"):
#         s=numb1+numb2
#     elif(choice=="H" or choice=="h"):
#         s=numb1-numb2
#     elif(choice=="U" or choice=="u"):
#         s=numb1*numb2
#     elif(choice=="D" or choice=="d"):
#         s=numb1/numb2
#     elif(choice=="S" or choice=="s"):
#         s=numb1**numb2
#     elif(choice=="E" or choice=="e"):
#         status="exit"
#     else:
#         print("Буруу утга оруулсан байна")

#     if(choice=="E" or choice=="e"):
#         print("exit")
#     else:
#         print(s)


