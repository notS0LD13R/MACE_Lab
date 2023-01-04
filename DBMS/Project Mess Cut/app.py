import flask as flk
from mysqldb import Database

app=flk.Flask(__name__)
app.secret_key="bruh"
db_user='root'
db_pass='root'

@app.route('/')
def home():
    return flk.redirect('/login')

@app.route('/login')
def login():
    return flk.render_template('login.html')

@app.route('/auth',methods=['POST'])
def auth():
    db=Database(db_user,db_pass,'mess_management')
    
    adm_no=flk.request.form.get('user')
    password=flk.request.form.get('pass')
    name=db.getname(adm_no)
    status=db.authenticate(adm_no,password)
    #need fixing authenticate auto closing the connection :(
    
    db.close()
    if status[0]:
        flk.session['user']=adm_no
        flk.session['name']=name
        
        if status[1]:
            return flk.redirect('/admin')
        else:
            return flk.redirect('/user')
    else:
        return flk.render_template('login.html',alert="Invalid Credentials")

@app.route('/user',methods=['POST','GET'])
def user():
    content={'adm_no':flk.session['user'],
            'name':flk.session['name'],
            'cut_calendar':list(range(31))
            }

    if flk.request.method=='POST':
        
        day=int((flk.request.form.get('calendar')[-2:]))
        iscut=flk.request.form.get('cut')=='cut'
        
        db=Database(db_user,db_pass,'mess_management')
        
        if day:
            db.alter_cut(flk.session['user'],day,iscut)
            content['cut_status']='Added mess cut'
        cuts=db.get_cuts(adm_no=flk.session['user'])
        
        db.close()
    
        content['cut_calendar']=['green' if x else 'red' for x in cuts]

    return flk.render_template('user.html',**content)

@app.route("/admin",methods=['POST','GET'])
def admin():
    content={'insert_status':flk.request.args.get('insert_status')}
    db=db=Database(db_user,db_pass,'mess_management')
    content['student_list']=db.get_students()
    sql='select * from mess_cost order by date desc limit 5'
    content['mess_cost']=db.execute(sql)
    db.close()
    
    return flk.render_template('admin.html',**content)

@app.route("/admin_func",methods=['POST','GET'])
def admin_func():
    cost=flk.request.form.get('cost')
    content={}
    print(flk.request.method)
    if flk.request.method=='POST':
        form=flk.request.form
        db=Database(db_user,db_pass,'mess_management')
        print(form)
        if 'messcost' in form:
            db.set_mess_cost(cost)
            db.calc_mess_bill()
            
        elif 'reset' in form:
            db.monthly_reset()
        
        elif 'student' in form:
            name=form.get('name')
            adm_no=form.get('adm_no')
            hostel_id=form.get('hostel_id')
            
            if ((1<=len(name)<=50) and (len(adm_no)==8)):
                db.insert_student(adm_no,name,int(hostel_id))
                content['insert_status']="Student inserted"
            else:
                content['insert_status']="Student detail invalid"
        db.close()
    return flk.redirect(flk.url_for("admin",**content))




if __name__=="__main__":
    app.run(debug=True)