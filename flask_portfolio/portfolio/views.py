## FROM THE CURRENT DIRECTORY, IMPORT APP
from . import app
from flask import render_template, request

comments = [{'name' :'bae','message' : 'Love you'},
			{'name': 'Saroosh', 'message': 'bring me a beer, Please!'}]


@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/hobbies', methods = ['GET', 'POST'])
def hobbies():
	if request.method == 'POST':
		the_name = request.form['name']
		the_note = request.form['the_message']
		comments.append({'name' : the_name, 'message': the_note})

		print(comments)
		return render_template('/hobbies.html', messages = comments)
	else:
		print('get method')
		print(comments)
		return render_template('/hobbies.html', messages= comments)

@app.route('/surprise', methods = ['GET', 'POST'])
def surprise():
	if request.method == 'POST':
		return render_template('/surprise.html', messages = comments)
	else:
		print('get method')
		print(comments)
		return render_template('/surprise.html', messages= comments)

@app.route('/youwin', methods = ['GET', 'POST'])
def wins():
	   return render_template('/winning.html')
