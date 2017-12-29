from flask import Flask,render_template
from energenie import switch_on, switch_off
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('home.html')

@app.route('/lightson/', methods=['POST'])
def lightson():
	switch_on(4)
	return render_template('home.html', message='Lights turned on!')

@app.route('/lightsoff/', methods=['POST'])
def lightsoff():
	switch_off(4)
	return render_template('home.html', message='Lights turned off!')

@app.route('/treeon/', methods=['POST'])
def treeon():
	switch_on(3)
	return render_template('home.html', message='Tree turned on!')

@app.route('/treeoff/', methods=['POST'])
def treeoff():
	switch_off(3)
	return render_template('home.html', message='Tree turned off!')

if __name__ == '__main__':
	app.run(debug=True, host='192.168.10.95')
