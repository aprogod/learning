# sql 모듈 생성
# 1. Class 생성 Database
# 2. Class가 생성이 될떄 pymysql.connect 변수 생성, cursor 생성(__init__)
# 3. init을 제외한 함수 3개 생성
# 4. execute() -> sql, value를 받아와서 sql문을 실행.
# 5. executeAll() -> sql, value 를 받아와서 sql문을 실행하고 결과값을 return
# 6. commit() -> commit을 하는 함수생성
import pymysql

class Database():
    
    def __init__(self):
        self._db = pymysql.connect(
        user = "root",
        passwd = "1234",
        host = "localhost",
        db = "ubion"
        )

        self.cursor = self._db.cursor(pymysql.cursors.DictCursor)

    def _execute(self, input_sql, input_value = {}):
        
        self.sql = input_sql
        self._values = input_value
        self.cursor.execute(self.sql, self._values)

    def _executeAll(self, input_sql, input_value = {}):
        
        self.sql = input_sql
        self._values = input_value
        self.cursor.execute(self.sql, self._values)
        self.result = self.cursor.fetchall()
        return self.result

    def _commit(self):
        self._db.commit()
