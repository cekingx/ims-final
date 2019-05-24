import pymysql
from pymysql import cursors

DB_USER = "root"
DB_PASS = "root13"
DB_NAME = "bot"

mysql_config = {
    'user': DB_USER,
    'password': DB_PASS,
    'db': DB_NAME,
    'charset': 'utf8mb4',
    'cursorclass': cursors.DictCursor,
    'autocommit': True
}
