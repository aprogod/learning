# sql 모듈 생성
# 1. Class 생성 Databas

import pymysql

class Database():
    
    def __init__(self):
        self._db = pymysql.connect(host = "darkpreist.iptime.org",
        user = "ubion",
        passwd = "1234",
        db = "ubion",
        port = 3306)

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