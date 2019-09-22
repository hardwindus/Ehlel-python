# 14 Шатрын хөлөг дээр байрлах 2 тэргийн коардинат x1, y1, x2, y2 хэлбэртэй өгөгдсөн бол биесээ идэх бол true үгүй бол false гэж хэвлэ.
# t1x=input("тэрэг 1 ийн X координат: ")
# t1y=input("тэрэг 1 ийн Y координат: ")
# t2x=input("тэрэг 2 ийн X координат: ")
# t2y=input("тэрэг 2 ийн Y координат: ")
# if t1x==t2x or t1y==t2y:
#     if t1x==t2x and t1y==t2y:
#         print(False)
#     else:
#         print(True)
# else:
#     print(False)
# 15 Шатрын хөлөг дээр байрлах 2 тэмээний коардинат x1, y1, x2, y2 хэлбэртэй өгөгдсөн бол биесээ идэх бол true үгүй бол false гэж хэвлэ.
t1x=input("тэмээ 1 ийн X координат: ")
t1y=input("тэмээ 1 ийн Y координат: ")
t2x=input("тэмээ 2 ийн X координат: ")
t2y=input("тэмээ 2 ийн Y координат: ")
if int(t1x)-int(t2x)==int(t1y)-int(t2y):
    if t1x==t2x and t1y==t2y:
        print("Буруу оруулаад байна")
    else:
        print("Идэх боломжтой")
else:
    print("Идэлцэхгүй")
# a=[3, 4, 5]
# for x in a:
#     print(x)
# a=input()
# b=input()
# c=input()
# list1=[int(a), int(b), int(c)]
# list1.sort(reverse=True)
# print(list1)

# a=input()
# b=input()
# c=input()
# if a<=b and b<=c:
#     print(a, b, c)    
# elif a<=b and b<=c:
#     print(a, c, b)  
# elif b<=a and a<=c:
#     print(b, a, c) 
# elif b<=c and c<=a:
#     print(b, c, a) 
# elif c<=a and a<=b:
#     print(c, a, b) 
# else:
#     print(c, b, a) 
# a=input()
# b=a.replace("a","b")
# print(b.replace("A","B"))
# print(a.replace("a" or "A", "B"))
