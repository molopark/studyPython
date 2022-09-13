from flask import Flask
from flask import render_template
from jsonProcess import getMovie

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome index page!!!"
    
@app.route("/movie/<page>")
def movie(page):
    print(page)
    list = getMovie(page)
    return render_template('movie.html', list=list)

@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/index')
def main():
    return render_template('index.html')

@app.route('/html/<sub1>')
def submain(sub1):
    print("### "+sub1)
    return render_template('html/'+sub1)

@app.route('/html/<sub1>/<sub2>')
def submain1(sub1,sub2):
    print("### "+sub1+" ## "+sub2)
    return render_template('html/'+sub1+'/'+sub2)

@app.route('/html/<sub1>/<sub2>/<sub3>')
def submain2(sub1,sub2,sub3):
    return render_template('html/'+sub1+'/'+sub2+'/'+sub3)

@app.get("/jsonHello")
def jsonHello():
    return {"message": "Hello World"}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9000, debug=True)
    