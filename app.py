from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home_page():
	return "<a href='/post'>create</a>"

@app.route('/post', methods=['GET', 'POST'])
def Create_post():
	if request.method == 'GET':
		return render_template("Createpost.html",name="YUVAL") 
	else:
		event = request.form['eventname']
		des = request.form['description']
		loc = request.form['location']
		time = request.form['time']
		maxi = request.form['max']

		image = request.form['event']
		add_event("Yuval", image, des, time, loc, maxi)
		return render_template("Createpost.html", name = name, event = event)
       
    
      

if __name__ == '__main__':
   app.run(debug = True)