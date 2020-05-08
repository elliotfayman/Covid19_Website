from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<name>')
def index(name):
	return render_template('name.html')


@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/Activities')
def Activities():
	return render_template('Activities.html')

@app.route('/FAQ')
def FAQ():
	return render_template('FAQ.html')

@app.route('/Contact')
def Contact():
	return render_template('Contact.html')
