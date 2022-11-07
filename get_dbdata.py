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

@app.route('/showlist')
def showList():
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


@app.route('/addWord')
def addWord():
    #test code for register new words, this function might became a part of method for admin
    sql = "INSERT INTO cards (word,meaning,category) VALUES ('test','trial something', 1);"

    # try:
    conn = dbConnection()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

    cursor.close()
    conn.close()

    return sql

    # except Exception as e:
    #     print('DB ERROR')
    #     print(e)

## おまじない
if __name__ == "__main__":
    app.run(debug=True)
