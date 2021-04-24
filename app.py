from flask import Blueprint
from flask_restful import Api
from resources.Hello import Hello
from resources import Category,Comment

api_bp = Blueprint('api', __name__)
api = Api(api_bp)
# Route

api.add_resource(Category.CategoryResource, '/category')
api.add_resource(Comment.CommentResource, '/comment')
