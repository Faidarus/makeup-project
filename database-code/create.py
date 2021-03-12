from app import db, Make_up_bag, Face, Eyes, Lips

db.drop_all()
db.create_all()

first_name = Make_up_bag(name = 'Fatima Aidarus')
second_name = Make_up_bag(name = 'Ilham Aidarus')

db.session.add(first_name)
db.session.commit()

db.session.add(second_name)
db.session.commit()

face_products_one= Face(face_primer='Wonderglow Face Primer', foundation='Nars Sheer Glow', bronzer='Bobbi Brown Bronzer', blush= 'Cheek To Chic',make_up_bag_id=1)
face_products_two = Face(face_primer='Veil Mineral Primer', foundation='Vanish Seamless Finish Foundation Stick',bronzer='MAC Bronzer', blush= 'Cloud Paint',make_up_bag_id=2)

db.session.add(face_products_one)
db.session.commit()

db.session.add(face_products_two)
db.session.commit()

eyes_products_one = Eyes(eye_concealer='Pro Filter Instant Retouch Concealer', eye_shadow='Charlotte Darling Palette',eye_liner= 'Hyper Precise All Day Liner', mascara='False Lash Effect Mascara' ,eye_brow_pencil='Goof Proof Eyebrow Pen',make_up_bag_id=1)
eyes_products_two = Eyes(eye_concealer='Magic Away Concealer', eye_shadow='18T Truth or Bare Artistry Palette',eye_liner= 'Eye Studio Gel Liner',mascara= 'Scandaleyes Reloaded',eye_brow_pencil='Micro Brow Eyebrow Pencil',make_up_bag_id=2)

db.session.add(eyes_products_one)
db.session.commit()

db.session.add(eyes_products_two)
db.session.commit()

lips_products_one = Lips(lip_liner='NYX Professional Makeup Lip Liner Pencil', lipstick='Charlottae Tilbury Lipstick', lipgloss='Kiko lipgloss',make_up_bag_id=1)
lips_products_two = Lips(lip_liner='MAC Lip Pencil', lipstick='MAC Lipstick',lipgloss='Pat Mcgrath Lipgloss',make_up_bag_id=2 )

db.session.add(lips_products_one)
db.session.commit()

db.session.add(lips_products_two)
db.session.commit()