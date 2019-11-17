# import mysql.connector
# import datetime

# mysqlConn = mysql.connector.connect(
#     host="localhost", # 192.168.1.155
#     user="root",
#     database="db_class",
#     passwd=""
# )
# cust_id=int(input("хэрэглэгчийн дугаар оруулах: "))

# query='''SELECT concat(cu2.customer_name, " бол ",cu1.customer_name," -н " ,type," юмаа.")
# FROM relative
# left join customer cu1 ON
# relative.customer_id1=cu1.customer_id
# left join customer cu2 ON
# relative.customer_id2=cu2.customer_id
# where relative.customer_id2=%d'''%(cust_id)

# query1='''SELECT concat("Бас ",customer_name, " бол ",occupation," юмаа.")
# FROM customer 
# inner join education on
# customer.customer_id=education.customer_id
# where customer.customer_id=%d'''%(cust_id)

# mysqlCursor = mysqlConn.cursor()

# mysqlCursor.execute(query)
# data = mysqlCursor.fetchall()

# mysqlCursor.execute(query1)
# data1 = mysqlCursor.fetchall()

# print(data[0][0])
# print(data1[0][0])
# # print(data[1][0])



# import mysql.connector
# import random



# aimags = ["Arkhangai", "Bulgan", "Zavkhan", "Gobi-Altai"]
# specs = ["Shonkhoruud", "Burgeduud", "Avarguud"]

# teams=[]
# counter=1
# # aimag_x=random.randint(0,3)
# for a in range(0,4):
#     for s in range(0,3):
#         teams.append({
#             "ID": counter,            
#             "NAME":aimags[a]+ " "+specs[s]
#         })
#         counter=counter+1

# print(teams)

# team1_id=random.randint(1,len(teams))
# team2_id=random.randint(1,len(teams))
# while(team1_id==team2_id):
#     team2_id=random.randrange(len(teams))

# print(teams[team1_id])
# print(teams[team2_id])
# Даалгавар: 
# Дээрх aimags, specs-ийн утгуудыг ашиглаад
# Arkhangai burgeduud, Bulgan Avarguud гэх мэт
# нэрсийг үүсгэнэ үү. Бүх боломжоор.


import mysql.connector
import random

mysqlConn = mysql.connector.connect(
    host="localhost", # 192.168.1.155
    user="root",
    database="db_class",
    passwd=""
)

# teams = []
# counter = 1

# def getGame():
#     team1_id = random.randrange(1, len(teams)+1)
#     team2_id = random.randrange(1, len(teams)+1)
#     while(team1_id == team2_id):
#         team2_id = random.randrange(1, len(teams)+1)

#     team1_poins = random.randrange(30, 120)
#     team2_poins = random.randrange(30, 120)

#     y = 2019
#     m = random.randrange(1, 13)
#     d = random.randrange(1, 32)
#     gamedate = "%d-%d-%d"%(y,m,d)

#     return (team1_id, team2_id, team1_poins, team2_poins, gamedate)

# aimags = ["Arkhangai", "Bulgan", "Zavkhan", "Gobi-Altai"]
# specs = ["Shonkhoruud", "Burgeduud", "Avarguud"]

# # Даалгавар: 
# # Дээрх aimags, specs-ийн утгуудыг ашиглаад
# # Arkhangai burgeduud, Bulgan Avarguud гэх мэт
# # нэрсийг үүсгэнэ үү. Бүх боломжоор.

# for aimag_ner in aimags:
#     for spec_ner in specs:
#         teams.append({
#             "id" : counter,
#             "name" : aimag_ner+" " + spec_ner
#         })
#         counter = counter + 1

# print(teams)
# # TODO: save teams to DB


# for i in range(30):
#     c0=i
#     c1=getGame()[0]
#     c2=getGame()[1]
#     c3=getGame()[2]
#     c4=getGame()[3]
#     c5=getGame()[4]
#     query="insert into games values(%s, %s, %s, %s,%s, '%s')"%(c0,c1,c2,c3,c4,c5)
#     # print(query)
#     mysqlCursor = mysqlConn.cursor()
#     mysqlCursor.execute(query)
    
query="Select min(game_date) date from games"
mysqlCursor = mysqlConn.cursor()
mysqlCursor.execute(query)
data= mysqlCursor.fetchall()
print(data[0][0])
