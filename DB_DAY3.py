# import mysql.connector

# mysqlConn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     database="class_db",
#     passwd=""
# )

# mysqlcursor=mysqlConn.cursor()

# query1="Select start_year from worker where address='UB3'"

# mysqlcursor.execute(query1)

# data = mysqlcursor.fetchall()

# print(data)

# Мэдээний вэб:

# - Агуулга /content/
#     * id        integer,
#     * title     string
#     * body      string
#     * worker_id intenger
#     * created_date datetime
#     * viewed_count /үзсэн тоо/   integer
#     * like_count                integer
# - Ангилал /category/
#     * id    integer
#     * name   string
# - Сэтгэгдэл /comment/
#     * id      integer
#     * name    string
#     * body    string
#     * like_count    integer
#     * dislike_count   integer


# create table content
# (
#     ID integer not null,
#     TITLE varchar(200),
#     BODY text,
#     WORKER_ID integer,
#     CREATED_DATE datetime,
#     VIEWED_COUNT integer,
#     LIKE_COUNT integer
# );

# create table category
# (
#     ID integer not null,
#     name varchar(200)

# )

# create table comment
# (
#     ID integer not null,
#     NAME varchar(200),
#     BODY text,
#     LIKE_COUNT integer,
#     DISLIKE_COUNT integer
# )

# Агуулга бичдэг, уншдаг програм хийх!
#  - Унших [u]/Бичих [b]
#  - songolt oruulna
#  herev "u":
#     -- suuliin 5 medeenii garchgiig haruulna
#      [id] [title]
#      [1] [Medee neg]
#     ---- hereglegch medeenii id oruulna.
#         *** Medeenii uzsen toog 1-eer nemne.
#      ---- medeeg haruulna

#  herev "b":
#     -- hereglegch songoh!
#      [worker_id] [worker name]
#         [1] [Bat]
#         ...
#     --- hereglegch id oruulna.
#     - garchig oruulna
#     - aguulga bichne
#     - Хадгална
#         * үүсгэсэн огноо
#         * бичсэн хэрэглэгчийн ID-г цуг хадгалах


# import mysql.connector

# mysqlConn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     database="class_db",
#     passwd=""
# )

# mysqlcursor=mysqlConn.cursor()

# while(status=="running"):
#     print("Унших[u]")
#     print("Бичих[b]")

#     songolt_1=input("Унших[u], Бичих[b]")

#     if(songolt_1=="u"):
#         print("Унших")
#     elif(songolt_1=="b"):
#         print("бичих")
#     else:
#         print("буруу комманд")

import mysql.connector
import datetime

mysqlConn = mysql.connector.connect(
    host="192.168.1.155",
    user="root",
    database="class_db",
    passwd=""
)

def executeSql(query):
    mysqlCursor = mysqlConn.cursor()

    mysqlCursor.execute(query)

    if(mysqlCursor.with_rows):
        data = mysqlCursor.fetchall()
        return data
    
    return "OK"


songolt_1 = input("Унших[u], Бичих[b]: ")

# if(songolt_1 == "u"):
    
#     print("Унших мэдэгээ сонгоно уу")
#     last_five=executeSql("Select ID, TITLE, BODY from content order by created_date desc limit 5")
#     print(last_five)
#     info_id=int(input("МэдээниЙ ID:"))
#     query2="Select BODY from content where ID=%d"%(info_id)
#     data=executeSql(query2)
#     print(data)
#     pass

if(songolt_1 == "u"): 

    query = '''SELECT id, title FROM content
    ORDER BY created_date DESC
    LIMIT 5'''

    data = executeSql(query)
    for row in data:
        print("[%d] %s"%(row[0], row[1]))

    content_id = int(input("Мэдээний ID: "))

    query = '''SELECT * FROM content
    WHERE id = %d'''%(content_id)

    news = executeSql(query)
    old_viewed_count = news[0][5]
    query = '''UPDATE content
    SET viewed_count = %d
    WHERE id = %d'''%(old_viewed_count+1, content_id)
    executeSql(query)
    print(news[0][1])
    print("--------------")
    print(news[0][2])
    print("[L]ike  [C]omment")
    action=input(": ")
    if(action=="L"):
        update_query='''update content set LIKE_COUNT=LIKE_COUNT+1 where ID=%d'''%(content_id)
        executeSql(update_query)
    elif(action=="C"):
        guest_name=input("Таны нэр: ")
        comment=input("Комментоо оруулна уу: ")
    pass

    


elif(songolt_1 == "b"):
    print("Бичих хэрэглэгчээ сонго:")
    workers = executeSql("SELECT id, name FROM worker")
    for w in workers:
        print("[%d] %s"%(w[0], w[1]))
    
    w_id = int(input("Хэрэглэгчийн ID: "))
    
    print("Мэдээний ангилал сонго:")
    cats = executeSql("SELECT id, name FROM category")
    for row in cats:
        print("[%d] %s"%(row[0], row[1]))
    
    c_id = int(input("Хэрэглэгчийн ID: "))
    
    title = input("Мэдээний гарчиг: ")
    body = input("Мэдээ: ")

    max_id = executeSql("SELECT MAX(id) FROM content")
    new_id = max_id[0][0] + 1

    insertQuery = '''
        INSERT INTO content (id, title, body, worker_id, category_id, created_date) 
        VALUES
        (%d, "%s", "%s", %d, %d, "%s")
    '''%(new_id, title, body, w_id, c_id, datetime.date.today())
    
    value = executeSql(insertQuery)

    pass
else:
    print("Буруу сонголт байна. Програм дууслаа.")
