from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', x = 8, y = 8)

@app.route('/4')
def callDown():
    return render_template('index.html', x = 8, y = 4)

@app.route('/<x>/<y>')
def acrossDown(x,y):
    return render_template('index.html', x = int(x), y = int(y) )

@app.route('/10/10')
def hellaColors():
    return render_template('index.html', x =10,y=10)

if __name__ == "__main__":
    app.run(debug=True)