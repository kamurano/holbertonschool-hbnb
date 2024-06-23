from datetime import datetime
from flask import Blueprint, jsonify, request

from Model.user import User
from Repository.user_repository import UserRepository


user_controller = Blueprint('user_controller', __name__)

user_manager = UserRepository()

@user_controller.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    email = data.get('email')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    user = User(email, first_name, last_name)
    valid, msg = user_manager.create_user(user)
    if not valid:
        return jsonify({"message": "User not created", "error": msg})
    return jsonify(user.__dict__)
    

@user_controller.route('/users', methods=['GET'])
def get_users():
    users = user_manager.get_users()
    return jsonify(users)


@user_controller.route('/users/<user_id>', methods=['GET'])
def get_specific(user_id):
    valid, msg = user_manager.get_user_details(user_id)
    if not valid:
        return jsonify({"message": "User not found", "error": msg})
    return jsonify(msg)


@user_controller.route('/users/<user_id>', methods=['PUT'])
def update_users(user_id):
    valid, old_data = user_manager.get_user_details(user_id)
    if not valid:
        msg = old_data
        return jsonify({"message": "User not updated", "error": msg})
    data = request.get_json()
    email = data['email']
    first_name = data['first_name']
    last_name = data['last_name']
    
    user = User(email, first_name, last_name)
    user.id = user_id
    user.created_at = old_data["created_at"]
    user.updated_at = datetime.now().isoformat()
    valid, msg = user_manager.update_user(user_id, user)
    if not valid:
        return jsonify({"message": "User not updated", "error": msg})
    return jsonify(user.__dict__)


@user_controller.route('/users/<user_id>', methods=['DELETE'])
def delete_users(user_id):
    valid, msg = user_manager.delete_user(user_id)
    if not valid:
        return jsonify({"message": "User not deleted", "error": msg})
    return jsonify({"message": "User deleted successfully"})
