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

dictionary={}
dictionary["hello"]="сайн уу"
status="running"

while(status=="running"):

    print("A - үг нэмэх")
    print("S - үг хайх")
    print("E - гарах")

    choice=input("та үйлдлээ сонгоно уу: ")
    if(choice=="A"):
        print("Үг нэмэх үйлдэл хийнэ.")
        eng=input("ENG:")
        mon=input("MON:")
        dictionary[eng]=mon
    elif(choice=="S"):
        word=input("Үгээ оруулна уу:")
        print(dictionary[word])
    elif(choice=="E"):
        status="exit"
    else:
        print("Буруу комманд!")
