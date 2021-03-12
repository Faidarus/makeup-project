from application import app, models , db, routes
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
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
    submit = SubmitField('Add products')

class Eyesform(FlaskForm):
    eye_concealer_product= StringField('Eye Concealer')
    eye_shadow_product= StringField('Eye Shadow')
    eye_liner_product= StringField('Eye liner')
    mascara_product= StringField('Mascara')
    eye_brow_pencil_product= StringField('Eyebrow Pencil')
    submit = SubmitField('Add products')

class Lipsform(FlaskForm):
    lip_liner_product= StringField('Lip liner')
    lipstick_product= StringField('Lipstick')
    lipgloss_product= StringField('Lipgloss')
    submit = SubmitField('Add products')

#using @app.route to route to my forms 

@app.route('/make_up_bag')
def make_up_bag():
    error ""
    forms = Make_up_bagform()

if (request.method=='POST'):
        third_name = form.third_name.data
    
    if len(third_name) == 0:
        error = "Please input name"
        else:
            new_owner = models.Make_up_bag(third_name = form.third_name.data)
            db.session.add(new_owner)
            db.session.commit()
            return 'Please input Face Products'
            return redirect('/face')    
    return render_template('make_up_bag.html', form=form, message=error)


@app.route('/face')
def face():
    error ""
    forms = faceform()

    if (request.method=='POST'):
        face_primer_product = form.face_primer_product.data
        foundation_product = form.foundation_product.data
        bronzer_product = form.bronzer_product.data
        blush_product = form.blush_product.data

    if len(face_primer_product) == 0 or len(foundation_product) == 0 or len(bronzer_product) or len(blush_product):
        error = "Please input products"
        else:
            return 'Great, thank you!'
            return redirect('/make_up_bag.html')
    
    return render_template('face.html', form=form, message=error)

@app.route('/eyes')
def eyes():
    error ""
    forms = eyesform()

    if (request.method=='POST'):
        eye_concealer_product = form.eye_concealer_product.data
        eye_shadow_product = form.eye_shadow_product.data
        eye_liner_product = form.eye_liner_product.data
        mascara_product = form.mascara_product.data
        eye_brow_pencil_product = form.eye_brow_pencil_product.data

    if len(eye_concealer_product) == 0 or len(eye_shadow_product) == 0 or len(eye_liner_product) or len(mascara_product ) or len(eye_brow_pencil_product):
        error = "Please input products"
        else:
            return 'Great, thank you!'
            return redirect('/make_up_bag.html')
    
    return render_template('eyes.html', form=form, message=error)

@app.route('/lips')
def lips():
    error ""
    forms = lipsform()

    if (request.method=='POST'):
        lip_liner_product = form.eye_concealer_product.data
        lipstick_product = form.eye_shadow_product.data
        lipgloss = form.eye_liner_product.data
        

    if len(lipstick_product) == 0 or len( lipgloss) == 0 or len(lipgloss):
        error = "Please input products"
        else:
            return 'Great, thank you!'
            return redirect('/make_up_bag.html')
    
    return render_template('lips.html', form=form, message=error)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')