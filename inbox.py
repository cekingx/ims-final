from flask import Flask, request
import mysql.connector

# konek ke database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root13",
    database="bot"
)
mycursor = mydb.cursor()

app = Flask(__name__)


@app.route("/")
def hello():
    return "Inbox"


@app.route('/inbox', methods=['POST'])
def inbox():
    # Mendapatkan data dari gate
    data = request.get_json()
    chat_id = data['chat_id']
    nama = data['nama']
    # Menambahkan data ke database
    sql = "INSERT INTO inbox (chat_id, nama) VALUES (%s, %s)"
    value = (chat_id, nama)
    mycursor.execute(sql, value)
    mydb.commit()
    # response 201
    print(mycursor.rowcount, " row inserted")
    return "Data Inserted", 201
