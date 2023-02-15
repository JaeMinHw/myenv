import pymysql

    # # (1) MYSQL 연결 
    # connection = mysql.connector.connect(
    #     host = '127.0.0.1',
    #     database = 'bookmark',  
    #     user = 'root',
    #     password = '1234'   
    # )

    # if connection.is_connected():
    #     db_info = connection.get_server_info()
    #     print('mysql Version : ', db_info)  

    #     # (2) 커서 만들기 
    #     cursor = connection.cursor()

    #     # (3) 원하는 쿼리문 등 실행 
    #     sql = 'select * from user where ID = %s;'
        
    #     with conn:
    #         with conn.cursor() as cur:
    #         cur.execute(sql, ('Jaehee'))
    #         result = cur.fetchall()
    #         for data in result:
    #             print(data)
            
    #     cursor.execute(sql, 'woals99')
    #     result = cursor.fetchall()
    #     for data in result:
    #         print(data)
    
    
    
    
# conn = pymysql.connect(host='localhost',
#                     user='root',
#                     password='1234',
#                     db='bookmark',
#                     charset='utf8')

# sql = "SELECT * FROM user where ID = %s and pw= %s"


# # with conn:
# #     with conn.cursor() as cur:
# #         cur.execute(sql, ('woals99','woals99'))
# #         result = cur.fetchall()
# #         for data in result:
# #             print(data[0])
# #             print(data[1])


# sele = []
# with conn:
#         with conn.cursor() as cur:
#             cur.execute(sql, ('woals99','woals99'))
#             result = cur.fetchall()
#             for data in result:
#                 sele.append(data)
                
# print(sele[0])
# print(sele[0][2])

sele=[]
sql = "SELECT * FROM Favorite where ID = %s "


# (1) MYSQL 연결 
conn = pymysql.connect(host='localhost',
                user='root',
                password='1234',
                db='bookmark',
                charset='utf8')
with conn:
    with conn.cursor() as cur:
        cur.execute(sql, ('woals99'))
        result = cur.fetchall()
        for data in result:
            sele.append(data)
            

json_data = {}
li = []
if len(sele) == 0 :
    json_data['result'] = 'false'



# elif len(sele) != 0 :
#     json_data['result'] = "success"
#     for i in range(len(sele)) :
#         json_data['num'] = sele[i][0]
#         json_data['ID'] = sele[i][1]
#         json_data['link'] = sele[i][2]
#         json_data['favName'] = sele[i][3]
#         json_data['favImage'] = sele[i][4]

# elif len(sele) != 0 :
#     json_data['result'] = "success"
#     for i in range(len(sele)) :
#         print(json_data)
#         json_data['list'] = [{'num':sele[i][0],'ID':sele[i][1],'link':sele[i][2],'favName':sele[i][3],'favImage':sele[i][4]},]
elif len(sele) != 0 :
    json_data['result'] = "success"
    for i in range(len(sele)) :
        img_file = sele[i][4]
        if(img_file == None) :
            print("wrong")
        elif(img_file != 'NULL') :
            print("pass")
        # print(sele[i][4])
        # li.append({'num':sele[i][0],'ID':sele[i][1],'link':sele[i][2],'favName':sele[i][3],'favImage':sele[i][4]})
        
    # json_data['list'] = li
    # print(json_data)


