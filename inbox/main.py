from os import getenv

import pymysql
from pymysql.err import OperationalError

# TODO: Bangun koneksi
CONNECTION_NAME = getenv(
    'INSTANCE_CONNECTION_NAME',
    'proud-woods-237806:asia-southeast1:dirga1')
DB_USER = getenv('MYSQL_USER', 'root')
DB_PASSWORD = getenv('MYSQL_PASSWORD', 'root13')
DB_NAME = getenv('MYSQL_DATABASE', 'mca')

mysql_config = {
    'user': DB_USER,
    'password': DB_PASSWORD,
    'db': DB_NAME,
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor,
    'autocommit': True
}

mysql_conn = None


def __get_cursor():
    """
    Helper function to get a cursor
      PyMySQL does NOT automatically reconnect,
      so we must reconnect explicitly using ping()
    """
    try:
        return mysql_conn.cursor()
    except OperationalError:
        mysql_conn.ping(reconnect=True)
        return mysql_conn.cursor()


def inbox(request):
    global mysql_conn

    # Initialize connections lazily, in case SQL access isn't needed for this
    # GCF instance. Doing so minimizes the number of active SQL connections,
    # which helps keep your GCF instances under SQL connection limits.
    if not mysql_conn:
        try:
            mysql_conn = pymysql.connect(**mysql_config)
        except OperationalError:
            # If production settings fail, use local development ones
            mysql_config['unix_socket'] = f'/cloudsql/{CONNECTION_NAME}'
            mysql_conn = pymysql.connect(**mysql_config)

    # Remember to close SQL resources declared while running this function.
    # Keep any declared in global scope (e.g. mysql_conn) for later reuse.
    # TODO: Handle POST request yang datang
    data = request.get_json(force=True)
    if request.method == 'POST':
        chat_id = data['chat_id']
        in_msg = data['in_msg']
        flag = data['flag']
        sql = "INSERT INTO tb_inbox (chat_id, in_msg, flag) VALUES (%s, %s, %s)"

        # TODO: Save request ke database
        with __get_cursor() as cursor:
            cursor.execute(sql, (chat_id, in_msg, flag))
            return ("Data inserted", 201)
