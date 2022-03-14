from flask import Flask, redirect, render_template, request, url_for
from modules import mod_sql

app = Flask(__name__)

#localhost로 접속했을때
@app.route("/")
def index():
    return render_template("index.html")

#localhost/signup로 접속했을때
@app.route("/signup/", methods=["GET"]) ### get은 데이터를 url에 실어서 보낸다
def signup():
    return render_template("signup.html")

@app.route("/signup", methods=["POST"])
def signup_2():
    


    _id = request.form["_id"]
    _password = request.form["_password"]
    _name = request.form["_name"]
    _phone = request.form["_phone"]
    _gender = request.form["_gender"]
    _age = request.form["_age"]
    _ads = request.form["_ads"]
    _regitdate = request.form["_regitdate"]
    sql = """
            INSERT INTO user_info VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    _values = [_id, _password, _name, _phone, _ads, _gender, _age, _regitdate]
    _db = mod_sql.Database()
    _db._execute(sql, _values)
    _db._commit()

    return redirect(url_for('index'))

@app.route("/login/", methods=["POST"])
def login():

    _id = request.form["_id"]
    _password = request.form["_password"]

    sql = """
            SELECT * FROM user_info WHERE ID = %s AND password = %s
          """
    _values = [_id, _password]
    _db = mod_sql.Database()
    result = _db._executeAll(sql, _values)

    if result:
        return render_template("welcome.html", name = result[0]["name"], id = result[0]["ID"])
    else :
        return redirect(url_for('index'))

@app.route("/update", methods = ["GET"])
def update():
    id = request.args["_id"]
    sql = """
            SELECT * FROM user_info WHERE ID = %s
            """
    values = [id]
    _db = mod_sql.Database()
    result = _db._executeAll(sql, values)
    return render_template("update.html", info = result[0])

@app.route("/update", methods=["POST"])
def update_2():
    
    _id = request.form["_id"]
    _password = request.form["_password"]
    _name = request.form["_name"]
    _phone = request.form["_phone"]
    _gender = request.form["_gender"]
    _age = request.form["_age"]
    _ads = request.form["_ads"]
    
    sql = """
            UPDATE user_info SET 
            
            password = %s,
            name = %s,
            phone = %s,
            gender = %s,
            age = %s,
            ads = %s
            WHERE ID = %s
    """
    _values = [_password, _name, _phone, _gender, _age, _ads, _id]
    _db = mod_sql.Database()
    _db._execute(sql, _values)
    _db._commit()

    return redirect(url_for('index'))

@app.route("/delete", methods = ["GET"])
def delete():
    id = request.args["_id"]
    sql = """
            SELECT * FROM user_info WHERE ID = %s
            """
    values = [id]
    _db = mod_sql.Database()
    result = _db._executeAll(sql, values)
    return render_template("delete.html", info = result[0])

@app.route("/delete", methods=["POST"])
def delete_2():
    
    _id = request.form["_id"]
    _password = request.form["_password"]
    _name = request.form["_name"]
    _phone = request.form["_phone"]
    _gender = request.form["_gender"]
    _age = request.form["_age"]
    _ads = request.form["_ads"]
    
    sql = """
            DELETE FROM user_info
            WHERE 
            ID = %s AND password = %s
        """
    _values = [_id, _password]
    _db = mod_sql.Database()
    _db._execute(sql, _values)
    _db._commit()

    return redirect(url_for('index'))


app.run(port="80")

        # DB ->SELECT문을 사용 -> index page input ID, PASSWORD 받아와서
        # SELECT문으로 조회
        # 결과 값이 존재하면 return "login" 존재하지 않으면 return "Fail"
        # index.html 수정 main.py 수정
        # 1.index.html /login url에 post형식으로 접속. 
        # ID, PASSWORD print 출력 
        # 2. DB에서 SELECT문을 실행해서 user_info table 정보를 print() 출력
        # 3. SELECT문에 조건식을 추가하여 데이터의 유무 판별