# from application import app, db
# from application.models import Make_up_bag, Face, Eyes, Lips 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from application import routes

@app.route('/add')
def add():
    new_owner = Make_up_bag(name="Sudi")
    db.session.add(new_owner)
    db.session.commit()
    return "Added make-up bag owner to database"

@app.route('/read')
def read():
    all_owners = make_up_bag.query.all()
    owners_string = ""
    for make_up_bag in all_owners:
        owners_string += "<br>"+ make_up_bag.name
    return owners_string

@app.route('/update/<name>')
def update(name):
    first_new_owner = make_up_bag.query.first()
    first_new_owner.name = name
    db.session.commit()
    return first_new_owner.name

# @app.route('/delete/<name>')
# def delete(name):
#     delete_first_new_owner=Games.query.first()
#     db.session.delete(delete_first_new_owner)
#     db.session.commit()
#     return name