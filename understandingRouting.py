from flask import Flask  
app = Flask(__name__)  

#1
@app.route('/')          
def hello_world():
    return 'Hello World!'  

#2
@app.route('/dojo')         
def dojo():
    return 'Dojo!' 

#3
@app.route('/say/<name>')         
def sayName(name):
    return 'Hi '+ name+'!' 

#4
@app.route('/repeat/<number>/<name>')         
def repeat(number,name):
    x =(name+" ")*int(number)
    return x
if __name__=="__main__":    
  app.run(debug=True)   