# import base64
# import json

# with open("/Users/ghkd1/Desktop/woals99_naver.png", "rb") as image_file:
#     encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

# data = {
#     "image_base64": encoded_string
# }

# json_data = json.dumps(data)

# print(json_data)


import pymysql
sele=[]
sql = "SELECT * FROM Favorite where ID = %s and number = %s"


# (1) MYSQL 연결 
conn = pymysql.connect(host='localhost',
                user='root',
                password='1234',
                db='bookmark',
                charset='utf8')
with conn:
    with conn.cursor() as cur:
        cur.execute(sql, ('woals99','1'))
        result = cur.fetchall()
        for data in result:
            sele.append(data)
            

print(sele)
json_data = {}
if len(sele) == 0 :
    json_data['result'] = 'false'

elif len(sele) != 0 :
    json_data['result'] = 'success'
    json_data['number'] = sele[0][0]
    json_data['ID'] = sele[0][1]
    json_data['link'] = sele[0][2]
    json_data['favName'] = sele[0][3]
    json_data['favImage'] = sele[0][4]
    
print(json_data)