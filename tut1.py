from flask import Flask,redirect,url_for,render_template

app=Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

@app.route('/admin/<name>')
def admin(name):
    if name == "abhirup":
        return "Welcome to admin panel"
    else :
        return redirect(url_for('home'))


if __name__=="__main__":
    app.run(debug=True)