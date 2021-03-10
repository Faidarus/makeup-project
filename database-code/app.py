from flask_sqlalchemy import SQLAlchemy 
from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root@35.189.66.154/my_make_up_bag"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=True
db = SQLAlchemy(app)


class Make_up_bag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    faces = db.relationship('Face', backref='make_up_bag')
    eyess = db.relationship('Eyes', backref='make_up_bag')
    lipss = db.relationship('Lips', backref='make_up_bag')
    

class Face(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    face_primer = db.Column(db.String(50), nullable=False)
    foundation = db.Column(db.String(50), nullable=False)
    bronzer = db.Column(db.String(50), nullable=False)
    blush = db.Column(db.String(50), nullable=False)
    make_up_bag_id = db.Column(db.Integer,db.ForeignKey('make_up_bag.id'),nullable=False)
   

class Eyes(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    eye_concealer = db.Column(db.String(50), nullable=False)
    eye_shadow = db.Column(db.String(50), nullable=False)
    eye_liner = db.Column(db.String(50), nullable=False)
    mascara = db.Column(db.String(50), nullable=False)
    eye_brow_pencil = db.Column(db.String(50), nullable=False)
    make_up_bag_id = db.Column(db.Integer,db.ForeignKey('make_up_bag.id'),nullable=False)
    
class Lips(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    lip_liner = db.Column(db.String(50), nullable=False)
    lipstick = db.Column(db.String(50), nullable=False)
    lipgloss = db.Column(db.String(50), nullable=False)
    make_up_bag_id = db.Column(db.Integer,db.ForeignKey('make_up_bag.id'),nullable=False)


if __name__ == "__main__":
    app.run(debug==True,host='0.0.0.0')