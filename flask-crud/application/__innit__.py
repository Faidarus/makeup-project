from flask_sqlalchemy import SQLAlchemy 
from flask import Flask
from application import routes

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root@35.189.66.154/mymakeupbag_data"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=True
db = SQLAlchemy(app)