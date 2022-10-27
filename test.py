from flask import Flask

app = Flask(__name__)

@app.route('/')
def fnc_a():
	return "root page"

@app.route('/sub')
def fnc_1():
	return "sub page"

if __name__ == '__main__':
	app.run()
