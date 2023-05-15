from flask import Blueprint,render_template,redirect,url_for,abort,request
from flask_login import login_required,current_user
from app.controllers.product_controller import update_product_pic
from app.forms.product_form import ProductForm,DeleteProductForm
from app.forms.request_form import RequestForm
from app.models.model import Product
from app import db

#definition of the blueprint
product_bp = Blueprint('product_bp', __name__, url_prefix='/products')


@product_bp.route('/',methods=['GET','POST'])
@login_required
def get_products():
    form = RequestForm()
    if form.validate_on_submit():
        #add submit actions
        return redirect(url_for("product_bp.get_products"))
    page = request.args.get('page',1,type=int)
    products=Product.query.order_by(Product.date_posted.desc()).paginate(page=page,per_page = 5)
    return render_template('productView/products.html',title="products",form =form,products=products)


#create product route
@product_bp.route('/create',methods=['GET','POST'])
@login_required
def create_product():
    form = ProductForm()
    
    if form.validate_on_submit():
        product = Product(product_name=form.product_name.data,description = form.description.data,price=form.price.data,location=form.location.data,brand=form.brand.data,category=form.category.data,seller=current_user)
        if form.picture.data:
            product.picture = update_product_pic(form.picture.data)
        db.session.add(product)
        db.session.commit()
        
        return redirect(url_for('main.home'))
    return render_template('productView/cre_upd_product.html',title="add product",
                           form=form, legend = 'New Product')
    
    

#get a specefic product
@product_bp.route('/<int:product_id>')
def get_product(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('productView/product.html',title=product.product_name,product=product)



#update product route
@product_bp.route('/<int:product_id>/update',methods=['GET','POST'])
@login_required
def update_product(product_id):
    product=Product.query.get_or_404(product_id)
    if product.seller != current_user:
        abort(403)
    form = ProductForm()
    
    if form.validate_on_submit():
        product.product_name=form.product_name.data
        product.price=form.price.data
        product.location = form.location.data
        product.brand=form.brand.data
        product.category = form.category.data
        product.description=form.description.data
        if form.picture.data:
            product.picture = update_product_pic(form.picture.data)
        
        
        db.session.commit()
        return redirect(url_for('product_bp.get_product',product_id=product.id))
    
    elif request.method == 'GET':
        form.product_name.data=product.product_name
        form.price.data=product.price
        form.description.data= product.description
        form.brand.data=product.brand
        form.location.data=product.location
        form.category.data=product.category
        
    return render_template('productView/cre_upd_product.html',title='Update product',form=form,legend='update post')


#delete a specefic product
@product_bp.route('/<int:product_id>/delete',methods=['GET','POST'])
@login_required
def delete_product(product_id):
    
    product=Product.query.get_or_404(product_id)
    if product.seller!= current_user:
        abort(403)
    
    form=DeleteProductForm()
    
    if form.validate_on_submit():
        db.session.delete(product)
        db.session.commit()
        return redirect(url_for('product_bp.get_products'))
    else:
        print(form.errors)
        
    
    return render_template('productView/delete_product.html',form=form,product=product)
    