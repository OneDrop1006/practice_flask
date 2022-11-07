from flask import Flask
import pymysql

app = Flask(__name__)


#db connection object
# get all data
def dbConnection():
    return pymysql.connect(
        host = 'localhost',
        user = 'admin',
        password = 'admin',
        db = 'flashcard',
        charset = 'utf8',
        port = 3306,
        cursorclass=pymysql.cursors.DictCursor,
    )

@app.route('/getlist')
def getList():
    sql = "SELECT * FROM cards;"

    try:
        conn = dbConnection()
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        return rows[0]

    except Exception as e:
        print('DB ERROR')
        print(e)


## おまじない
if __name__ == "__main__":
    app.run(debug=True)
