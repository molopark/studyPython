from flask import Flask
from flask import render_template
from jsonProcess import getMovie

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/movielist/<page>")
def movielist(page):
    list = getMovie(page)
    return render_template('htmlpage/movielist.html', list=list)



@app.route("/mogle")
def mogle():
    return render_template('htmlpage/mogle.html')




@app.route("/test")
def test():
    page = '''
    Welcome <a href='index_test'>index</a> page!!!<br>
    go <a href='movie/1'>movie</a> page
    '''
    return page
    
@app.route('/index_test')
def index_test():
    return render_template('index_test.html')

@app.route("/movie/<page>")
def movie(page):
    print(page)
    list = getMovie(page)
    return render_template('ktm/movie.html', list=list)

@app.route('/ktm/<sub1>')
def submain(sub1):
    print("### "+sub1)
    return render_template('ktm/'+sub1)

@app.route('/ktm/<sub1>/<sub2>')
def submain1(sub1,sub2):
    print("### "+sub1+" ## "+sub2)
    return render_template('ktm/'+sub1+'/'+sub2)

@app.route('/ktm/<sub1>/<sub2>/<sub3>')
def submain2(sub1,sub2,sub3):
    return render_template('ktm/'+sub1+'/'+sub2+'/'+sub3)

@app.get("/jsonHello")
def jsonHello():
    return {"message": "Hello World"}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9000, debug=True)
