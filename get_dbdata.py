from flask import Flask,request
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


@app.route('/addCard')
def addCard():
    #test code for register new words, this function might became a part of method for admin
    sql = "INSERT INTO cards (word,meaning,category) VALUES ('test','trial something', 1);"

    try:
        conn = dbConnection()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

        cursor.close()
        conn.close()

        return sql

    except Exception as e:
        print('DB ERROR')
        print(e)

@app.route('/editCard',methods=['GET'])
def editCard():

    # get url parameters
    req = request.args

    id = req.get('id')
    word = req.get('word')
    meaning = req.get('meaning')
    category = req.get('category')

    param = (word,meaning,category,id)

    sql = ("""
        UPDATE cards
            SET word = %s,
            meaning = %s,
            category = %s
            WHERE id = %s;
        """)

    # DB dbConnection
    try:
        conn = dbConnection()
        cursor = conn.cursor()
        cursor.execute(sql,param)
        conn.commit()

        cursor.close()
        conn.close()

        return sql

    except Exception as e:
        print('DB ERROR')
        print(e)


##
if __name__ == "__main__":
    app.run(debug=True)
