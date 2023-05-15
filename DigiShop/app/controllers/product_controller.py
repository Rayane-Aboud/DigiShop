import os
import secrets
from app import app,db
from PIL import Image


def update_product_pic(form_picture_data):
    random_hex = secrets.token_hex(8)
    _,f_ext = os.path.splitext(form_picture_data.filename)
    pic_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path,'static/product_pics',pic_fn)
    output_size=(300,300)
    img = Image.open(form_picture_data)
    img.thumbnail(output_size)
    img.save(picture_path)
    return pic_fn

