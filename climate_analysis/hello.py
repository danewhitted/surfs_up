from flask import Flask

app = Flask(__name__)

@app.route('/')

@app.route('/')
def hello_world():
	return 'Hello world'

#if _name_ == "_main_":
	#app.run(debug=True)