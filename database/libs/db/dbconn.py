#데이터베이스 연결파일
import sqlite3

def getconn():
    conn = sqlite3.connect("e:/python/pyworks-jds/pydb/mydb.db")
    return conn
