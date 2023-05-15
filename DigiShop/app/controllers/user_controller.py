import secrets
import os
from PIL import Image
from app import app
from app import bcrypt, db
from app.models.model import User
from app.routes.user_bp import current_user

#adds user to the database by inserting it from a form 
def register_user(form):
    hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    user = User(firstname=form.firstname.data, familyname=form.familyname.data, username=form.username.data,
                email=form.email.data, password=hashed_password)
    db.session.add(user)
    db.session.commit()



#saves the picture uploaded by the user and a path to it in the server
def update_user_pic(form_picture_data):
    random_hex = secrets.token_hex(8)
    _,f_ext = os.path.splitext(form_picture_data.filename)
    pic_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path,'static/profile_pics',pic_fn)
    output_size=(125,125)
    img = Image.open(form_picture_data)
    img.thumbnail(output_size)
    img.save(picture_path)
    return pic_fn



#update the full profile.. calls the update_user_pic function
def update_user(form): 
    if form.picture.data:
        picture_file = update_user_pic(form.picture.data)
        current_user.image_file = picture_file
    current_user.username = form.username.data
    current_user.email = form.email.data
    db.session.commit()
    
    
def update_user_password(form,user):
    hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    user.password = hashed_password
    db.session.commit()