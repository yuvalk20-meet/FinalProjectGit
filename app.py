
from databases import *
from flask import Flask, render_template, request, url_for
from flask import session as login_session
 
app = Flask(__name__)
app.config['SECRET_KEY'] = ' you-will-never-guess'

@app.route('/', methods=['GET', 'POST'])
def home_page():
	posts = query_all()
	posts = posts[::-1]
	return render_template("HomePage.html", posts = posts )

@app.route('/post', methods=['GET', 'POST'])
def Create_post():
	
	username =login_session['name']
	
	if request.method=='GET':
		return render_template("Createpost.html",username=username) 
	else:
		

		event = request.form['eventname']
		des = request.form['description']
		loc = request.form['location']
		time = request.form['time']
		maxi = request.form['max']

		image = request.form['event']
		add_event(event, image, des, time, loc, maxi, username)
		user_ob = session.query(User).filter_by(name=username).first()
		add_points(user_ob.user_id)
		posts = query_all()
		posts = posts[::-1]
		return render_template("HomePage.html", name=username, event = event, posts = posts, user_id = user_ob.user_id)
       
 
## LOGIN ROUTES###
@app.route('/login', methods=['POST', 'GET'])
def login():
	if request.method == 'GET':
		return render_template('login.html')
	user = check_username(request.form['name'])
	if user != None and user.verify_password(request.form["password"]):
		login_session['name'] = user.name
		print(user.name)
		login_session['logged_in'] = True
		posts = query_all()
		posts = posts[::-1]
		return render_template("HomePage.html", posts = posts)
	else:
		return render_template("")



@app.route('/signup',methods=['POST','GET'])
def signup():
	if request.method=='GET':
		return render_template('signup.html')

	else:
		name=request.form['userName']
		password=request.form['password']
		age=request.form['age']
		phoneNumber=request.form['phoneNumber']
		gender=request.form['gender']
		neiborhood=request.form['neiborhood']
		addUser(name,password,age,phoneNumber,gender,neiborhood)
		print("Added User")
		return render_template("login.html")

		
if __name__ == '__main__':
	app.run(debug = True)