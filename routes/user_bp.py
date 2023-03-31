from flask import Blueprint
#from controllers.user_controller import index_user, create_user, show_user, update_user, delete_user

user_bp = Blueprint('user_bp',__name__)
"""
user_bp.route('/',methods=['GET'])(index_user)
user_bp.route('/create',methods=['POST'])(create_user)
user_bp.route('/<int:user_id>',methods=['GET'])(show_user)
user_bp.route('/<int:user_id>/edit',methods =['POST'])(update_user)
user_bp.route('/<int:user_id>',methods=['DELETE'])(delete_user)
"""