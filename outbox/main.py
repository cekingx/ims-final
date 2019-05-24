from os import getenv
import requests
import json
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

# Create SQL connection globally to enable reuse
# PyMySQL does not include support for connection pooling
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


def outbox(request):
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

    # TODO: Buat fungsi untuk select data dari database serta handling flag 1 dan 2
    # Handling jika flag 1 :
    # - post request ke gate untuk mengirim pesan
    # - ubah flag data jadi 2
    # Handling jika flag 2:
    # - return "Tidak ada pesan untuk dikirim"
    if request.method == 'GET':
        with __get_cursor() as cursor:
            cursor.execute('SELECT * FROM tb_outbox WHERE flag="1"')
            update = 'UPDATE tb_outbox SET flag="2" WHERE id_outbox=%s'
            GATE_ENDPOINT = "https://us-central1-proud-woods-237806.cloudfunctions.net/gate"
            raw_data = {
                "update_id": 1,
                "from_outbox": True,
                "chat": {
                    "id": 000000000,
                    "tipe": "none"
                }
            }
            results = cursor.fetchall()
            if len(results) > 0:
                for result in results:
                    # Send POST request
                    raw_data['chat']['id'] = result['chat_id']
                    if result['type'] == None:
                        raw_data['chat']['tipe'] = "Tidak diketahui"
                    else:
                        raw_data['chat']['tipe'] = result['type']
                    data = json.dumps(raw_data)
                    requests.post(url=GATE_ENDPOINT, data=data)
                    # Ganti flag
                    cursor.execute(update, result['id_outbox'])
                return "Oke"
            else:
                return "Tidak ada pesan untuk dikirim"
