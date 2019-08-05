from UserDB import *
from flask import Flask, render_template, request
from flask import session as login_session

app = Flask(__name__)
app.config['SECRET_KEY'] = ' you-will-never-guess'

@app.route('/', methods=['GET', 'POST'])
def home_page():
	return render_template("HomePage.html")

@app.route('/post', methods=['GET', 'POST'])
def Create_post():
	if request.method == 'GET':
		return render_template("Createpost.html",name="YUVAL", user_id = 0, point = 10) 
	else:
		event = request.form['eventname']
		des = request.form['description']
		loc = request.form['location']
		time = request.form['time']
		maxi = request.form['max']

		image = request.form['event']
		add_event("Yuval", image, des, time, loc, maxi)
		add_points()
		return render_template("Createpost.html", name = name, event = event)
       
 
## LOGIN ROUTES###
@app.route('/login', methods=['POST', 'GET'])
def login():
	if request.method == 'GET':
		return render_template('login.html')
	user = check_username(request.form['username'])
	if user != None and user.verify_password(request.form["password"]):
		login_session['name'] = user.username
		login_session['logged_in'] = True
		return render_template("Createpost.html")
	else:
		pass


@app.route('/signin',methods=['POST','GET'])
def signin():
	if request.method=='GET':
		return render_template('signin.html')

	else:
		pass
if __name__ == '__main__':
	app.run(debug = True)