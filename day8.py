# import re
# longstring="RD11112315"
# key="^[A-Z][A-Z][0-9]{8}$"
# matches=re.search(key,longstring)
# print(matches)

# class Time:
#     hour=0
#     minute=0
#     second=0

#     def __init__(self, h=0, m=0, s=0):
#         self.hour=h
#         self.minute=m
#         self.second=s

#     def printTime(self):
#         print("%d:%d:%d" % (self.hour,self.minute,self.second))
    
#     def addseconds(self,secondToAdd):
#         self.second=self.second+secondToAdd
#         mi=self.second//60
#         self.second=self.second%60
#         self.minute=self.minute+mi
#         hh=self.minute//60
#         self.minute=self.minute%60
#         self.hour=self.hour+hh
#         self.hour=self.hour%24
        
#     def isAfter(self,time2):
#         if (self.hour*3600+self.minute*60+self.second)<(time2.hour*3600+time2.minute*60+time2.second):
#             return True
#         else:
#             False

    



# timeObject_1=Time(17,30 ,15)
# timeObject_1.addseconds(50)
# timeObject_1.printTime()

# timeObject_2=Time()
# timeObject_2.printTime()

# print(timeObject_1)
# print(timeObject_2)


# class Point:
#     x=0
#     y=0
#     def __init__(self, xx=0, yy=0):
#         self.x=xx
#         self.y=yy


#     def __add__(self, Point2):
#         _x=self.x+Point2.x
#         _y=self.y+Point2.y
#         return Point(_x, _y)

#     def __str__(self):
#         return "%d X %d"%(self.x, self.y)

# tseg_1=Point(3, 5)
# tseg_2=Point(10, 20)

# tseg_3=tseg_1+tseg_2

# print(tseg_1.x, tseg_1.y)
# print(tseg_2.x, tseg_2.y)
# print(tseg_3.x, tseg_3.y)


# class rectangle:
#     topleft=Point()
#     rightbottom=Point()

#     def setsize(self, urt=5, undur=7):
#         self.rightbottom.x=self.rightbottom.x+self.urt
#         self.rightbottom.y=self.rightbottom.y+self.undur


# rect_1=rectangle()
# print(rect_1.topleft)
# print(rect_1.rightbottom)

# Hunii passportiin medeelel:

# import json

# text="{ \
# \"ner\":\"Lhagva\", \
# \"ovog\":\"Davaasuren\",\
# \"RD\":\"ME50015522\",\
# \"Bdate\":\"1950-01-15\",\
# \"hayag\":\
#     {\
#         \"hot\":\"UB\",\
#         \"duureg\":\"BZD\",\
#         \"horoo\":\"25\",\
#         \"Delgerengui\":\"BZD iin 25-r horoo bla bla bla\"\
#     }\
# }"


# y = json.loads(text)

# print(y)
# print(y["ovog"], y["ner"], y["RD"])
# print(y["hayag"]["hot"])


import json

text='{ \
"ner":"Lhagva", \
"ovog":"Davaasuren",\
"RD":"ME50015522",\
"Bdate":"1950-01-15",\
"hayag":\
    {\
        "hot":"UB",\
        "duureg":"BZD",\
        "horoo":"25",\
        "Delgerengui":"BZD iin 25-r horoo bla bla bla"\
    }\
}'


y = json.loads(text)

print(y)
print(y["ovog"], y["ner"], y["RD"])
print(y["hayag"]["hot"])

Myvalue={
    "key":"value",
    "number":889977,
    "array":(0,2,4)
}

strval=json.dumps(Myvalue)
writingFile=open("json_outtest.txt","w")
writingFile.write(strval)
writingFile.close()
