from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
	return "hello world"

@app.route('/sub')
def sub():
	return "sub page"

if __name__ == '__main__':
	app.run()
