
from dataclasses import fields
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app=Flask(__name__)#instantiate the app
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///hello.db"
db=SQLAlchemy(app)
ma=Marshmallow(app)

class Schema(ma.Schema):
    class meta:
        fields=("id","name","age")

user=Schema()
users=Schema(many=True)


class Users(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String)
    age=db.Column(db.Integer)

    def __init__(self,name,age):
        self.name=name
        self.age=age
        

@app.route("/")
def index():
    return "hello world"

@app.route("/add/<name>/<age>")
def addusers(name,age):
    user=Users(name,age)
    db.session.add(user)
    db.session.commit()

    return {"message":"added user successfully"}

@app.route("/users")
def allusers():
    data=Users.query.all()
    data=users.dump(data)

    return users.jsonify(data)

@app.route("/about/<name>")
def about(name):

    return "Hello "+name


#ORM-Object Relational Mapper

if __name__=="__main__":
    db.create_all()
    app.run(debug=True)
    