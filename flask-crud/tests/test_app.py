from flask import url_for
from flask_testing import TestCase
from app import app
from application import db, models
from application.models import Make_up_bag, Face, Eyes, Lips

#unit test commands 
# pytest
# pytest --cov=app
# pytest --cov-config=.coveragec --cov=.
# pytest --cov=app --cov-report=term-missing
# pytest --cov . --cov-report html

# creating base class 

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

# testing if all froms input section in my @app.route works     

    def setUp(self):
        
        db.create_all()

        test_owner = Make_up_bag(name="Sudi")
        test_face = Face(face_primer="MAC Face Primer", foundation="Lancome Teint Idole Ultra Foundation", bronzer="Fenty Beauty Bronzer", blush="Lancome blush", make_up_bag_id=1)
        test_eyes = Eyes(eye_concealer="MAC Concealer", eye_shadow="MAC eyeshadow", eye_liner="MAC eyeliner", mascara="MAC mascara", eye_brow_pencil="MAC eyebrow pencil", make_up_bag_id=1)
        test_lips = Lips(lip_liner="Pat McGrath Lipstick", lipstick="Pat McGrath Lipliner", lipgloss="Pat McGrath Lipgloss", make_up_bag_id=1)
        db.session.add(test_owner)
        db.session.add(test_face)
        db.session.add(test_eyes)
        db.session.add(test_lips)
        db.session.commit()
    
    # def tearDown(self):
    #     db.session.remove()
    #     db.drop_all()

    

# tesing if my @app.route status is working 

class TestViews(TestBase):

    def test_make_up_bag_get(self):
        response = self.client.get(url_for('make_up_bag'))
        self.assertEqual(response.status_code, 200)
        # self.assertIn(b'name="Sudi"', response.data)

    def test_face_get(self):
        response = self.client.get(url_for('face',make_up_bag_id=1))
        self.assertEqual(response.status_code, 200)
        # self.assertIn(b'face_primer="MAC Face Primer", foundation="Lancome Teint Idole Ultra Foundation", bronzer="Fenty Beauty Bronzer", blush="Lancome blush", make_up_bag_id=1',  response.data)

    def test_eyes_get(self):
        response = self.client.get(url_for('eyes',make_up_bag_id=1))
        self.assertEqual(response.status_code, 200)
        # self.assertIn(b'eye_concealer="MAC Concealer", eye_shadow="MAC eyeshadow", eye_liner="MAC eyeliner", mascara="MAC mascara", eye_brow_pencil="MAC eyebrow pencil", make_up_bag_id=1', response.data)

    def test_lips_get(self):
        response = self.client.get(url_for('lips',make_up_bag_id=1))
        self.assertEqual(response.status_code, 200)
        # self.assertIn(b'lip_liner="Pat McGrath Lipstick", lipstick="Pat McGrath Lipliner", lipgloss="Pat McGrath Lipgloss", make_up_bag_id=1', response.data)
    
    def test_delete_get(self):
        response = self.client.get(url_for('delete',lips_id=1),follow_redirects=True)
        self.assertEqual(response.status_code,200 )
        assert b'Pat McGrath Lipliner'
    
    def test_update_get(self):
        response = self.client.get(url_for('update',lips_id=1),follow_redirects=True)
        self.assertEqual(response.status_code,200 )
        assert b'Pat McGrath Lipliner'
        
#testing if my input was added 

class TestAdd(TestBase):
    def test_add_post(self):
        response = self.client.post(
            url_for('make_up_bag'),
            data = dict(name="Niya"),
            follow_redirects=True
        )
        # self.assertIn(b"Niya",response.data)

    def test_add_face_post(self):
        response = self.client.post(
            url_for('face',make_up_bag_id=1),
            data = dict(face_primer="MAC Face Primer", foundation="Lancome Teint Idole Ultra Foundation", bronzer="Fenty Beauty Bronzer", blush="Lancome blush", make_up_bag_id=1),
            follow_redirects=True
        )
        self.assertIn(b'MAC Face Primer', response.data)

    def test_add_eyes_post(self):
        response = self.client.post(
            url_for('eyes',make_up_bag_id=1),
            data = dict(eye_concealer="MAC Concealer", eye_shadow="MAC eyeshadow", eye_liner="MAC eyeliner", mascara="MAC mascara", eye_brow_pencil="MAC eyebrow pencil", make_up_bag_id=1),
            follow_redirects=True
        )
        self.assertIn(b'MAC Concealer', response.data)


    def test_add_lips_post(self):
        response = self.client.post(
            url_for('lips',make_up_bag_id=1),
            data = dict(lip_liner="Pat McGrath Lipstick", lipstick="Pat McGrath Lipliner", lipgloss="Pat McGrath Lipgloss", make_up_bag_id=1),
            follow_redirects=True
        )
        self.assertIn(b'Pat McGrath Lipstick' ,response.data)
    



