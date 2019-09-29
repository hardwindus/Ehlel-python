# fruits=["Banana","Apple","Cherry"]
# fruits.append("Orange")
# fruits.insert(2,"Kiwi")
# list2=fruits.copy()
# fruits.remove("Banana")
# fruits.pop()
# # del fruits
# # fruits.clear()
# print(fruits)
# print(list2)
# print(list2.count("Banana"))
# print(List2.index("Kiwi"))


# def Fibonacci(n): 
#     if n==1: 
#         return 0
#     elif n==2: 
#         return 1
#     else: 
#         return Fibonacci(n-1)+Fibonacci(n-2) 
  

# 10. Өгөгдсөн тооны хуваагчдыг ол
# def func10(n):
#     for x in range(1,n//2+1):
#         if n%x==0:
#             print(x,end=' ')


# # Функц дуудан ажиллуулах
# print(func10(int(input()))) 

# 11. Өгөгдсөн тооны хуваагчдын тоог ол
# def func11(n):
#     count=0
#     for x in range(1,n+1):
#         if n%x==0:
#             count+=1
#     return count

# n=int(input())
# print(func11(n))


#11. Өгөгдсөн тооны хуваагчдын тоог ол
#12. Өгөгдсөн үгэнд а үсэг хэдэн удаа орсон байна вэ
#13. Өгүүлбэрийн үгүүдээс b үсгийг хас
#14. Өгөгдсөн тооны цифрүүдийн нийлбэрийг ол
# def func14(n):
#     s=0
#     for x in range(len(n)):
#         s=s+int(n[x])
    
#     return s

# n=str(input())
# print(func14(n))

# def niilber(n):
#     s=0
#     k=0
#     while(n>0):
#         p=n%10
#         s+=p
#         k+=1
#         n=n//10
#     # return s
#     return k

# n=int(input())
# print(niilber(n))

#15. Өгөдсөн n тоо анхны тоо мөн үү

# import time

# def func15(n):
#     start_time = time.time()
#     c=True
#     for x in range(2,n//2+1):
#         if n%x==0:
#             c=False
#     end_time = time.time()
#     return c,end_time-start_time

# n=int(input())
# print(func15(n))

# def func15(n):
#     if func11(n)==2

# n=int(input())
# print(func15(n))



#16. 3 оронтой бүх палендром тоонуудыг ол
#17. Цифрүүдын нийлбэр нь k байх бүх 3 оронтой тоонуудын тоог ол
#18. Өгөгдсөн тоо анхны тоо мөн үү
#19. n ээс m тоо хүртэлх анхны тоонуудыг ол
#20. n ээс m тоо хүртэлх анхны тоонуудын тоог ол


# fruits=["Apple","Orange","Banana","Orange"]
# fruits.append("Strawberry")
# fruits.insert(0,"Kiwi")
# list2=fruits.copy()
# # print(fruits[1])
# # print(fruits)
# print(fruits)
# print(fruits.index("Orange"))
# print(len(fruits))
# fruits.sort()
# fruits.reverse()
# # print(fruits)

# car=["prius","200","570","RX"]
# for x in car:
#     print(x)

# fruits.extend(car)
# print(fruits)


#1. Тоон дарааллын элементүүдын нийлбэрийг ол.
# list1=[12,25,25,263,36,54,4,5,6,6,88]
# print(sum(list1))
# s=0
# print(list1)
# for x in list1:
#     s=s+x
# print(s)

#2. Тоон дарааллын элементүүдын хамгийн их элементийг ол.
# s=list1[0]
# for x in list1:
#     if x>s:
#         s=x
#     else:
#         s=s
# print(s)

# # Тоон дарааллын элементүүдын хамгийн бага элементийг ол.
# s=list1[0]
# for x in list1:
#     if x<s:
#         s=x
#     else:
#         s=s
# print(s)

# Нэрсийн дарааллаас хамгийн урт нэрийг ол.
# name_list=["Davaa","Amaraa","Ganaa","Sanaa","Od"]
# print(max(name_list,key=len))


# Нэрсийн дарааллаас хамгийн богино нэрийг ол.
# name_list=["Davaa","Amar","Ganaa","Sanaa"],"Od"]
# print(min(name_list,key=len))

# Нэрсийн дарааллаас хамгийн урт нэрийг олж бүх үсгийг том болго.
# k=name_list.index(max(name_list,key=len))
# name_list[k]=max(name_list,key=len).upper()
# print(name_list)

# Нэрсийн дарааллаас хамгийн богино нэрийг олж 'Сайн уу?' гэж соль.
# k=name_list.index(min(name_list,key=len))
# name_list[k]="Сайн уу?"
# print(name_list)

# Өгөгдсөн тоон дарааллыг буурахаар эрэмбэл.
# list1=[12,25,21,263,36,54,4,28,6,6,77]
# list1.sort()
# list1.reverse()
# print(list1)

#9. Тоон дарааллын хамгийн их болон багын байрыг соль.
# max_ind=list1.index(max(list1))
# max_val=max(list1)
# min_ind=list1.index(min(list1))
# min_val=min(list1)

# list1[max_ind]=min_val
# list1[min_ind]=max_val
# print(list1)

# def func_swap(n):
#     ih=n.index(max(n))
#     baga=n.index(min(n))
#     n[ih],n[baga]=min(n),max(n)
#     return n

# list1=[12,25,21,263,36,54,4,28,6,6,77]
# print(func_swap(list1))

#10. Тоон дарааллаас 7т хуваагддаг тоонуудыг ол.
# for x in list1:
#     if x%7==0:
#         print(x,end=' ')



#11. Тоон дарааллаас хамгийн бага элементийг устга.
# list1=[12,25,21,263,36,54,4,28,6,6,77]
# list1.remove(min(list1))
# print(list1)

#12. Тоон дарааллаас сөрөг тоонуудыг 0 болго.
# list1=[12,-25,21,-263,36,54,4,28,6,6,77]
# for x in list1:
#     if x<0:
#         list1.index(list1(x))

list2=[12,25,9,263,36,54,4,28,6,6,77]
for x in list2:
    if x%2==1:
        list2.remove(x)
print(list2)

# too=[]
# list2=[12,25,9,263,36,54,4,28,6,6,77]
# for x in list2:
#     if x%2==0:
#         too.append(x)
# print(too)

# def func_odd(list2):
#     alist=[]
#     for x in list2:
#         if x%2==0:
#             alist.append(x)
#     return alist

# list2=[12,25,9,263,36,54,4,28,6,6,77]
# print(func_odd(list2))

# Олимпиадын дүн бүхий оноонуудын жагсаалт өгөгдсөн бол хэд дэх хүн түрүүлсэн бэ.
# Байгууллагуудын нэрсийн жагсаалт өгөгдсөн бол хамгийн урт нэртэй хүнтэй байгууллагын байрлалыг ол.
# Нэрсийн дарааллаас хамгийн богино нэртэй хүмүүсийн тоог ол.
# Нэрсийн дарааллаас хамгийн урт нэртэй хүмүүсийг ол.
# Сурагчдын тоон үнэлгээний жагсаалт өгөгдсөн бол 89-өөс их бол А, 79-өөс их В, 69-өөс их бол С, 59-өөс их бол D бусад тохиолдолд F үсгэн дүнг хэвлэ.
# Болд шинэ ажилтан бүртгэж байв. Гэтэл бүртгүүлсэн хүмүүс дахиж бүртггүүлж түүнд асуудал үүсгэв. Давхардсан нэрсийг устгах программ бичиж түүнд туслацгаая.
# Нэрсийн бүртгэл өгөгдсөн боловч нэрийн эхний үсэг бүр том биш байв тэдгээрийг том үсэг болго.
# Нэрсийн бүртгэл өгөгдсөн бол нэрэнд нь б үсэг орсон хүмүүсийг олж хасаад өөр бүртгэлд бүртгэж ав.
# Нэрсийн бүртгэл өгөгдсөн бол нэрэнд нь 2-аас олон а үсэг орсон хүмүүсийг ол
