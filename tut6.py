from flask import Flask,redirect,url_for,render_template,request,session,flash
from datetime import timedelta

app=Flask(__name__)
app.secret_key="hello" #what is this used for?
app.permanent_session_lifetime = timedelta(days=1)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        name=request.form['name']
        session["user"]= name
        session.permanent=True
        return redirect(url_for('user',user=name))
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
        return redirect(url_for('login'))

@app.route('/user')
def user():
    if "user" in session:
        user = session["user"]
        flash("logged in successfully ","info")
        return render_template('user.html',user=user)
    else:
        flash("You are not logged in ","info")
        return redirect(url_for("login"))

if __name__=="__main__":
    app.run(debug=True)