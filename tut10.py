from flask import Flask,render_template
from second import second

app = Flask(__name__)
app.register_blueprint(second,url_prefix="/admin")

@app.route("/home")
def test():
    """this is docstring this will get commented out"""
    return "<h1>Test</h1>"

if __name__=='__main__':
    app.run(debug=True)
