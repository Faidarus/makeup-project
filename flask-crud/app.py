from application import app, models , db, routes
from application.models import Make_up_bag, Face, Eyes, Lips
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


app.config['SECRET_KEY'] = 'manchester123'


#creating forms for my data to be inputed 

class Make_up_bagform(FlaskForm):
    third_name = StringField('Name')
    submit = SubmitField('Add Name')

class Faceform(FlaskForm):
    face_primer_product= StringField('Face Primer')
    foundation_product= StringField('Foundation')
    bronzer_product= StringField('Bronzer')
    blush_product= StringField('Blush')
    make_up_bag_id = IntegerField ('ID')
    submit = SubmitField('Add products')

class Eyesform(FlaskForm):
    eye_concealer_product= StringField('Eye Concealer')
    eye_shadow_product= StringField('Eye Shadow')
    eye_liner_product= StringField('Eye liner')
    mascara_product= StringField('Mascara')
    eye_brow_pencil_product= StringField('Eyebrow Pencil')
    make_up_bag_id = IntegerField ('ID')
    submit = SubmitField('Add products')

class Lipsform(FlaskForm):
    lip_liner_product= StringField('Lip liner')
    lipstick_product= StringField('Lipstick')
    lipgloss_product= StringField('Lipgloss')
    make_up_bag_id = IntegerField ('ID')
    submit = SubmitField('Add products')

#using @app.route to route to my forms 

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
@app.route('/make_up_bag', methods=['GET', 'POST'])
def make_up_bag():
    error = ""
    form = Make_up_bagform()

    if request.method=='POST':
        third_name = form.third_name.data
        
        if len(third_name) == 0:
            error = "Please input name"
        else:
            new_owner = models.Make_up_bag(name=form.third_name.data)
            db.session.add(new_owner)
            db.session.commit()
            return redirect('/face')
    make_up_bag_owner = models.Make_up_bag.query.all()
    return render_template('make_up_bag.html',title="Make-up bag", form=form, make_up_bag_owner=make_up_bag_owner, message=error)


@app.route('/face/<int:make_up_id>', methods=['GET', 'POST'])
def face(make_up_bag_id):
    error = ""
    form = Faceform()
    form.make_up_bag_id.data = make_up_bag_id

    if request.method=='POST':
        face_primer_product = form.face_primer_product.data
        foundation_product = form.foundation_product.data
        bronzer_product = form.bronzer_product.data
        blush_product = form.blush_product.data
        make_up_bag_id = make_up_bag_id
        
        if len(face_primer_product) == 0 or len(foundation_product) == 0 or len(bronzer_product) == 0 or len(blush_product) == 0:
            error = "Please input face products"
        
        else:
            new_face_products=models.Face(face_primer=form.face_primer_product.data, foundation=form.foundation_product.data, bronzer=form.bronzer_product.data, blush=form.blush_product.data,make_up_bag_id=make_up_bag_id)
            db.session.add(new_face_products)
            db.session.commit()
            return redirect('/make_up_bag')
    make_up_bag_owner = models.Make_up_bag.query.all()
    return render_template('face.html', title="Face Products", form=form, make_up_bag_owner=make_up_bag_owner, message=error)


@app.route('/eyes/<int:make_up_id>', methods=['GET', 'POST'])
def eyes(make_up_bag_id):
    error = ""
    form = Eyesform()
    form.make_up_bag_id.data = make_up_bag_id

    if request.method=='POST':
        eye_concealer_product = form.eye_concealer_product.data
        eye_shadow_product = form.eye_shadow_product.data
        eye_liner_product = form.eye_liner_product.data
        mascara_product = form.mascara_product.data
        eye_brow_pencil_product = form.eye_brow_pencil_product.data
        make_up_bag_id = make_up_bag_id
        
        if len(eye_concealer_product) == 0 or len(eye_shadow_product) == 0 or len(eye_liner_product) == 0 or len(mascara_product ) == 0 or len(eye_brow_pencil_product) == 0:
            error = "Please input eyes products"
        else:
            new_eyes_products=models.Eyes(eye_concealer=form.eye_concealer_product.data, eye_shadow=form.eye_shadow_product.data, eye_liner=form.eye_liner_product.data, mascara=form.mascara_product.data, eye_brow_pencil=form.eye_brow_pencil_product.data, make_up_bag_id=make_up_bag_id)
            db.session.add(new_eyes_products)
            db.session.commit()
            make_up_bag_owner = models.Make_up_bag.query.all()
            return redirect('/make_up_bag')
    
    return render_template('eyes.html',title="Eye Products", form=form, make_up_bag_owner=make_up_bag_owner, message=error)


@app.route('/lips/<int:make_up_id>', methods=['GET', 'POST'])
def lips(make_up_bag_id):
    error = ""
    form = Lipsform()
    form.make_up_bag_id.data = make_up_bag_id

    if request.method=='POST':
        lip_liner_product = form.lip_liner_product.data
        lipstick_product = form.lipstick_product.data
        lipgloss = form.lipgloss_product.data
        make_up_bag_id = make_up_bag_id
        
        if len(lip_liner_product) == 0 or len(lipstick_product) == 0 or len(lipgloss) == 0:
            error = "Please input lips products"
        
        else:
            new_lips_products=models.Lips(lip_liner=form.lip_liner_product.data, lipstick=form.lipstick_product.data, lipgloss=form.lipgloss_product.data, make_up_bag_id=make_up_bag_id)
            db.session.add(new_lips_products)
            db.session.commit()
            make_up_bag_owner = models.Make_up_bag.query.all()
            return redirect('/make_up_bag')
    
    return render_template('lips.html',title="Lip Products", form=form, make_up_bag_owner=make_up_bag_owner, message=error)

# @app.route('/face/delete/<face_primer>') # this will not work because face_primer is an input not something in the route 
# def delete(face_primer):
#     delete_first_face_primer=Face.query.first()
#     db.session.delete(delete_first_face_primer)
#     db.session.commit()
#     return face_primer

# @app.route('/face/delete/, methods=['DELETE'])
# def delete():
#       forms = faceform()
#       if request.method=='DELETE':
#           face_primer_product = form.face_primer_product.data
#           foundation_product = form.foundation_product.data
#           bronzer_product = form.bronzer_product.data
#           blush_product = form.blush_product.data
#     delete_new_face_products=Face.query.first()
#     db.session.delete(delete_new_face_products)
#     db.session.commit()
#     return 'Delted your face products'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')