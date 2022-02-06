from flask import Blueprint, jsonify, request
from models import books_model
books_blueprint = Blueprint('books', __name__)

# localhost:8080/api/books
@books_blueprint.route('/', methods=['GET'])
def get_all_books():
    print('get_all_books')
    print(request.user)
    return jsonify(books_model.get_books_all()), 200


# localhost:8080/api/books/<int:id>
@books_blueprint.route('/<int:id>', methods=['GET'])
def get_book_by_id(id):
    return jsonify(books_model.get_book_by_id(id)), 200

@books_blueprint.route('/', methods=['POST'])
def create_new_book():
    data = request.json
    print(data)
    return jsonify(books_model.add_book(data['title'],data['author'], data['first_sentence'], data['year_published'] )), 201

@books_blueprint.route('/<int:id>', methods=['DELETE'])
def delete_book_by_id(id):
    return jsonify(books_model.delete_book_by_id(id)), 200