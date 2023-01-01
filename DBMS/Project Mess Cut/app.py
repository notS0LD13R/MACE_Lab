import flask as flk
from mysqldb import Database

app=flk.Flask(__name__)

@app.route('/')
def home():
    return flk.redirect('/login')

@app.route('/login')
def login():
    return flk.render_template('login.html')

@app.route('/auth',methods=['POST'])
def auth():



if __name__=="__main__":
    app.run(debug=True)