import threading
import mysql.connector
import requests

# konek ke database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root13",
    database="bot"
)
mycursor = mydb.cursor()

url = "http://localhost:5000/send"

# Fungsi interval


def setInterval(func, time):
    e = threading.Event()
    while not e.wait(time):
        func()


# app = Flask(__name__)


# @app.route("/")
# def hello():
#     return "Outbox"


def outbox():
    mycursor.execute(
        "SELECT * FROM outbox where flag=0"
    )
    myresult = mycursor.fetchall()
    if(len(myresult) > 0):
        for result in myresult:
            # fetch data
            _id = result[0]
            chat_id = result[1]
            nama = result[2]
            # update row
            sql = f'UPDATE outbox SET flag=1 WHERE id={_id}'
            mycursor.execute(sql)
            mydb.commit()
            # request ke gate
            data = {"chat_id": chat_id, "nama": nama}
            requests.post(url, json=data)
    else:
        print("Nope")


setInterval(outbox, 5)
