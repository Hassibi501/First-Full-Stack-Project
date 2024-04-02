from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
app.app_context().push()

class userInfo(db.Model):
        id = db.Column(db.Integer, primary_key = True)
        userName = db.Column(db.String(200))
        password = db.Column(db.String(100), nullable = False)
        dateCreated = db.Column(db.DateTime ,default=datetime.utcnow)

        #returns task and userName as a string 
        def __repr__(self):
            return "<Task %r>" % self.userName
        


@app.route("/", methods=["POST" ,"GET"])
def home():
    if request.method == "POST":
        pass
        return "hello world"
    else:
        return render_template("login.html")

         


if __name__ == "__main__":
    app.run(debug=True)
