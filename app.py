from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/lorde/Desktop/firstFullStackProject/test.db'
db = SQLAlchemy(app)

class userInfo(db.Model):
        userName = db.Column(db.String(), primary_key = True)
        password = db.Column(db.String(), nullable = False)
        dateCreated = db.Column(db.DateTime ,default=datetime.utcnow)

        #returns task and userName as a string 
        def __repr__(self):
            return "<Task %r>" % self.userName
@app.route("/")
def home():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)

#todo: Get my test.db file working 
import os
print('test.db exists:', os.path.exists('test.db'))