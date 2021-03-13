from flask import url_for
from flask_testing import TestCase
from app import app, db, models 

# creating base class 

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="mysql+pymysql://root@35.189.66.154/mymakeupbag_data",
                SECRET_KEY='manchester123',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

# testing if all froms input section in my @app.route works     

    def setUp(self):
        
        db.create_all()
        test_owner = Make_up_bag(third_name="Sudi")

        db.session.add(test_owner)
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def setUp(self):
        
        db.create_all()
        test_face = Face(face_primer_product="MAC Face Primer", foundation_product="Lancome Teint Idole Ultra Foundation", bronzer_product="Fenty Beauty Bronzer", blush_product="Lancome blush")

        db.session.add(test_face)
        db.session.commit()

    def setUp(self):
        
        db.create_all()
        test_eyes = Eyes(eye_concealer_product="MAC Concealer", eye_shadow_product="MAC eyeshadow", eye_liner_product="MAC eyeliner", mascara_product="MAC mascara", eye_brow_pencil_product="MAC eyebrow pencil")       
        
        db.session.add(test_eyes)
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def setUp(self):
        
        db.create_all()
        test_lips = Lips(lip_liner_product="Pat McGrath Lipstick", lipstick_product="Pat McGrath Lipliner", lipgloss="Pat McGrath Lipgloss")

        db.session.add(test_lips)
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()

# tesing if my @app.route status is working 

class TestViews(TestBase):
    def test_make_up_bag_get(self):
        response = self.client.get(url_for('make_up_bag'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Sudi', response.data)

class TestViews(TestBase):
    def test_face_get(self):
        response = self.client.get(url_for('face'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'MAC Face Primer','Lancome Teint Idole Ultra Foundation','Fenty Beauty Bronzer','Lancome blush', response.data)

class TestViews(TestBase):
    def test_eyes_get(self):
        response = self.client.get(url_for('eyes'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'MAC Concealer', 'MAC eyeshadow', 'MAC eyeliner', 'MAC mascara', 'MAC eyebrow pencil', response.data)

class TestViews(TestBase):
    def test_lips_get(self):
        response = self.client.get(url_for('lips'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Pat McGrath Lipstick', 'Pat McGrath Lipliner', 'Pat McGrath Lipgloss', response.data)

#testing if my input was added 

class TestAdd(TestBase):
    def test_add_post(self):
        response = self.client.post(
            url_for('make_up_bag'),
            data = dict(third_name="Niya"),
            follow_redirects=True
        )
        self.assertIn(b'Niya',response.data)

class TestAdd(TestBase):
    def test_add_post(self):
        response = self.client.post(
            url_for('face'),
            data = dict(face_primer_product="MAC Face Primer", foundation_product="Lancome Teint Idole Ultra Foundation", bronzer_product="Fenty Beauty Bronzer", blush_product="Lancome blush"),
            follow_redirects=True
        )
        self.assertIn(b'MAC Face Primer','Lancome Teint Idole Ultra Foundation','Fenty Beauty Bronzer','Lancome blush',response.data)

class TestAdd(TestBase):
    def test_add_post(self):
        response = self.client.post(
            url_for('eyes'),
            data = dict(eye_concealer_product="MAC Concealer", eye_shadow_product="MAC eyeshadow", eye_liner_product="MAC eyeliner", mascara_product="MAC mascara", eye_brow_pencil_product="MAC eyebrow pencil"),
            follow_redirects=True
        )
        self.assertIn(b'MAC Concealer', 'MAC eyeshadow', 'MAC eyeliner', 'MAC mascara', 'MAC eyebrow pencil',response.data)


class TestAdd(TestBase):
    def test_add_post(self):
        response = self.client.post(
            url_for('lips'),
            data = dict(lip_liner_product="Pat McGrath Lipstick", lipstick_product="Pat McGrath Lipliner", lipgloss="Pat McGrath Lipgloss"),
            follow_redirects=True
        )
        self.assertIn(b'Pat McGrath Lipstick', 'Pat McGrath Lipliner', 'Pat McGrath Lipgloss',response.data)


