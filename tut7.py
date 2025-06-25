from flask import Flask,redirect,url_for,render_template,request,session,flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.secret_key="hello" #what is this used for?
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
# app.permanent_session_lifetime = timedelta(minutes=5)

db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id",db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self,name,email):
        self.name = name
        self.email= email

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        #name=request.form['name']
        name =request.form['name']
        session["user"]= name
        # session.permanent=True
        found_user = users.query.filter_by(name = name).first()
        if found_user:
            session["email"] = found_user.email
        
        else:
            usr=users(name,"")
            db.session.add(usr)
            db.session.commit()

        return redirect(url_for('user'))
    else:
        if "user" in session:
            flash("Already logged in ","info")
            return redirect(url_for("user"))
        else:
            return render_template('login.html')
        

@app.route("/logout")
def logout():
        if "user" in session:
            user = session["user"]
            flash(f"you have been logged out {user}!","info")
            #session.pop("user",None)
        del(session["user"])
        del(session["email"])
        return redirect(url_for('login'))

@app.route('/user', methods=["POST","GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]
        flash("logged in successfully ","info")

        if request.method=="POST":
            email=request.form['email']
            session["email"]=email
            found_user = users.query.filter_by(name = user).first()
            found_user.email =email
            db.session.commit()
            flash("Email was saved ","info")
        else:
            if "email" in session:
                email = session["email"]
        
        return render_template('user.html',user=user,email=email)
    else:
        flash("You are not logged in ","info")
        return redirect(url_for("login"))

if __name__=="__main__":
    with app.app_context():
        db.create_all()
    
    app.run(debug=True)