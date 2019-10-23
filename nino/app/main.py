from flask import Flask, render_template
from banco import *


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/insert')
def upload():
	return render_template('manage.html')


@app.route('/search')
def search():

	return render_template('search.html', array = [ 1 , 2 , 3,'Carol'] ) 
'''
@app.route('/insertdata')
def upload_data(data):
	res = render_template('upload_data.html',data=data)
	banco.insert(data)
	return res
'''

	
if __name__ == '__main__':
    app.run(debug=True)
