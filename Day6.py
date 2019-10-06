#niit huuhdiin toog avna
#n shirheg ner, dun
#A, B, C, D, E -g songoh

# table={}

# total=int(input("нийт оюутны тоо: "))
# print(total)
# count=0
# space=0
# symbol=""
# while total>count:
#     ner_dun=input("ner dun oruulah: ")
#     NerDunList=ner_dun.split(" ")
#     # space=ner_dun.find(" ")
#     # ner=ner_dun[:space]
#     # dun=ner_dun[space+1:]
#     # table[ner]=dun
#     name=NerDunList[0]
#     dun=float(NerDunList[1])
#     if dun<60:
#         symbol="F" 
#     elif dun<70:
#         symbol="D"
#     elif dun<80:
#         symbol="C"
#     elif dun<90:
#         symbol="B"
#     else:
#         symbol="A"
#     table[name]={"percent":dun,
#                  "symbol":symbol}
#     count=count+1

# for name in table:
#     print(name, table[name]["percent"], table[name]["symbol"])

# print(table.keys())


# import os
# value=os.path.exists("D:/python/bootsoo.py")
# value1=os.path.isfile("D:/python/bootsoo.py")
# value2=os.path.isdir("D:/python")
# print(value)
# print(value1)
# print(value2)

# fileobject=open("my-file.txt","r")
# fileobject.write("The text")
# fileobject.write("\n")
# fileobject.write("123")
# fileobject.close()

# while True:
#     line=fileobject.readline()
#     if line!="":
#         print(line)
#     else:
#         break

# fileobject.close()

# fileobject=open("my-file.txt","w")

# fileobject.write("long text %f is value."%10.0)

# # print(fileobject)
# import os
# import codecs

# # dictfile=open("dictionary.txt","w")

# dictionary={}
# # dictionary["hello"]="сайн уу"
# status="running"

# def addword(eng,mon):
#     dictfile=codecs.open("dictionary.txt","a","utf-8")
#     dictfile.write(u"%s--%s\r\n"% (eng,mon))
#     dictfile.close()

# def translate(eng):
#     dictfile=codecs.open("dictionary.txt","r","utf-8")
#     found=False
#     translation="Орчуулга олдсонгүй!"
#     while~False:
#         line=dictfile.readline()
#         if(line!=""):
#             EngMon=line.split("--")
#             if(EngMon[0]==eng):
#                 found=True
#                 translation=EngMon[1]
#             else:
#                 break
#     dictfile.close()
#     return translation

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

# dictfile.close()


import os
import codecs
# studentfile=open("studentfile.txt","w")
# table={}
def addstudent(name, dun,symbol):        
    studentfile=open("studentfile.txt","a","utf-8")
    studentfile.write(u"%s:%s:%s\r\n"% (name,str(dun),symbol))
    studentfile.close()

total=int(input("нийт оюутны тоо: "))
count=0
symbol=""
while total>count:
    ner_dun=input("ner dun oruulah: ")
    NerDunList=ner_dun.split(" ")
    name=NerDunList[0]
    dun=float(NerDunList[1])
    if dun<60:
        symbol="F" 
    elif dun<70:
        symbol="D"
    elif dun<80:
        symbol="C"
    elif dun<90:
        symbol="B"
    else:
        symbol="A"
    addstudent(name,str(dun),symbol)
    count=count+1
