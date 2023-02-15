import pymysql
from flask import Flask,Response
from flask_cors import CORS
import base64

app = Flask(__name__)
CORS(app)


def connection() :
    conn = pymysql.connect(host='localhost',
                    user='root',
                    password='1234',
                    db='bookmark',
                    charset='utf8')


@app.route('/')
def hello():
    return "Hello World!"

# 회원가입
@app.route('/signup/<string:userid>/<string:userpw>')
def signup(userid,userpw) :
    # 아이디랑 비밀번호를 받아서 아이디만 중복확인을 한 후 db에 집어 넣는다.
    # 또 Favorite 테이블에 기본적인 구조를 넣어준다 (insert into Favorite(number,ID) values(1~9,userid))
    return "success" + userid

@app.route('/login/<string:userid>/<string:userpw>')
def login(userid,userpw):
    # 아이디랑 비밀번호 확인한다.
    # 로그인 성공이면 해당하는 아이디에 맞는 bookmark를 json 형식으로 넘겨준다.
    sele=[]
    sql = "SELECT * FROM user where ID = %s and pw = %s"
    
    
    # (1) MYSQL 연결 
    conn = pymysql.connect(host='localhost',
                    user='root',
                    password='1234',
                    db='bookmark',
                    charset='utf8')
    with conn:
        with conn.cursor() as cur:
            cur.execute(sql, (userid,userpw))
            result = cur.fetchall()
            for data in result:
                sele.append(data)
                

    json_data = {}
    if len(sele) == 0 :
        json_data['result'] = 'false'
        return json_data
    
    elif len(sele) != 0 :
        json_data['result'] = 'success'
        json_data['ID'] = sele[0][0]
        json_data['pw'] = sele[0][1]
        json_data['name'] = sele[0][2]
        # 해당하는 아이디에 맞는 bookmark를 json형식으로 넘겨준다
        return json_data
    
    
@app.route('/bookmark/<string:userid>')
def bookmark(userid):
    # 이제 userid에 대한 bookmark를 json 형식으로 넘겨준다.
    
    sele=[]
    sql = "SELECT * FROM Favorite where ID = %s order by number"
    
    
    # (1) MYSQL 연결 
    conn = pymysql.connect(host='localhost',
                    user='root',
                    password='1234',
                    db='bookmark',
                    charset='utf8')
    with conn:
        with conn.cursor() as cur:
            cur.execute(sql, (userid))
            result = cur.fetchall()
            for data in result:
                sele.append(data)
                

    json_data = {}
    li = []
    
    if len(sele) == 0 :
        json_data['result'] = 'false'
    
    

    elif len(sele) != 0 :
        json_data['result'] = "success"
        for i in range(len(sele)) :
            img_file='null'
            img_file = sele[i][4]
            if(img_file == None) :
                encoded_str = 'null'
            else :
                with open("/Users/ghkd1/Desktop/woals99_naver.png", "rb") as img_file:
                    # encoded_str = base64.b64encode(img_file.read()).decode('utf-8')
                    encoded_str = 'null'
            li.append({'num':sele[i][0],'ID':sele[i][1],'link':sele[i][2],'favName':sele[i][3],'favImage':encoded_str})
        
    json_data['list'] = li
        
        # 해당하는 아이디에 맞는 bookmark를 json형식으로 넘겨준다
    # return Response(json_data, content_type='application/json')
    return json_data

    

# 해당하는 bookamrk를 클릭했을 때
@app.route('/choosebook/<string:userid>/<string:bookno>')
def choose(userid,bookno) :
    # 해당하는 bookmark를 json 형식으로 넘겨준다.
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
            cur.execute(sql, (userid,bookno))
            result = cur.fetchall()
            for data in result:
                sele.append(data)
                

    json_data = {}
    li = []
    if len(sele) == 0 :
        json_data['result1'] = 'false'
        return json_data

    elif len(sele) != 0 :
        json_data['result1'] = 'success'
        # json_data['num'] = sele[0][0]
        # json_data['ID'] = sele[0][1]
        # json_data['link'] = sele[0][2]
        # json_data['favName'] = sele[0][3]
        # json_data['favImage'] = sele[0][4]
        li.append({'num':sele[0][0],'ID':sele[0][1],'link':sele[0][2],'favName':sele[0][3],'favImage':sele[0][4]})
        
        # 해당하는 아이디에 맞는 bookmark를 json형식으로 넘겨준다
        json_data['list1'] = li
    return json_data
    

# 수정된 bookmark를 저장해야한다.
@app.route('/modibook/<string:userid>/<string:bookno>/<string:name>/<string:link>')
def modi(userid,bookno,name,link):
    # 링크로 들어온 값들을 조건에 맞는 곳에 수정하기
    sql = "update  Favorite set link = %s , favName = %s where ID = %s and number = %s"
    sql1 = "select * from Favorite where ID = %s and favName = %s and link=%s and number = %s order by number"
    
    json_data = {}
    # (1) MYSQL 연결 
    conn = pymysql.connect(host='localhost',
                    user='root',
                    password='1234',
                    db='bookmark',
                    charset='utf8')
    with conn:
        with conn.cursor() as cur:
            cur.execute(sql, (link,name,userid,bookno))
            conn.commit()
 
    # update가 제대로 이루어졌는지 select로 확인을 해준다
    sele = []
    conn1 = pymysql.connect(host='localhost',
                user='root',
                password='1234',
                db='bookmark',)
    with conn1:
        with conn1.cursor() as cur:
            cur.execute(sql1, (userid,name,link,bookno))
            result = cur.fetchall()
            for data in result:
                sele.append(data)
            if len(sele) == 0 :
                json_data['result'] = "fail"
                return json_data
            else :
                json_data['result'] = "success"
                return json_data
                
                

# 삭제된 bookmark를 저장해야한다.
@app.route('/delebook/<string:userid>/<string:bookno>')
def dele(userid,bookno) :
    sql = "update  Favorite set link = NULL , favName = NULL, favImage = NULL  where ID = %s and number = %s"
    sql1 = "select * from Favorite where ID = %s and number = %s and favName is NULL"
    
    json_data = {}
    # (1) MYSQL 연결 
    conn = pymysql.connect(host='localhost',
                    user='root',
                    password='1234',
                    db='bookmark',
                    charset='utf8')
    with conn:
        with conn.cursor() as cur:
            cur.execute(sql, (userid,bookno))
            conn.commit()
            

    sele = []
    conn1 = pymysql.connect(host='localhost',
                user='root',
                password='1234',
                db='bookmark',)
    with conn1:
        with conn1.cursor() as cur:
            cur.execute(sql1, (userid,bookno))
            result = cur.fetchall()
            for data in result:
                sele.append(data)
            if len(sele) == 0 :
                json_data['result'] = "fail"
                return json_data
            else :
                json_data['result'] = "success"
                return json_data
                

if __name__ == '__main__':
    app.run(host='0.0.0.0')