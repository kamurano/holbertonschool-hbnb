from datetime import datetime
from flask import Blueprint, jsonify, request

from Model.amenity import Amenity
from Repository.amenity_repository import AmenityRepository


amenity_controller = Blueprint('amenity_controller', __name__)

amenity_manager = UserRepository()

@amenity_controller.route('/amenitys', methods=['POST'])
def create_amenity():
    data = request.get_json()
    email = data['email']
    first_name = data['first_name']
    last_name = data['last_name']
    amenity = User(email, first_name, last_name)
    valid, msg = amenity_manager.create_amenity(amenity)
    if not valid:
        return jsonify({"message": "User not created", "error": msg})
    return jsonify(amenity.__dict__)


@amenity_controller.route('/amenitys', methods=['GET'])
def get_amenitys():
    amenitys = amenity_manager.get_amenitys()
    return jsonify(amenitys)


@amenity_controller.route('/amenitys/<amenity_id>', methods=['GET'])
def get_specific(amenity_id):
    amenity = amenity_manager.get_amenity_details(amenity_id)
    return jsonify(amenity)


@amenity_controller.route('/amenitys/<amenity_id>', methods=['PUT'])
def update_amenitys(amenity_id):
    old_data = amenity_manager.get_amenity_details(amenity_id)
    print(old_data)
    data = request.get_json()
    email = data['email']
    first_name = data['first_name']
    last_name = data['last_name']
    
    amenity = User(email, first_name, last_name)
    amenity.id = amenity_id
    amenity.created_at = old_data["created_at"]
    amenity.updated_at = datetime.now().isoformat()
    valid, msg = amenity_manager.update_amenity(amenity_id, amenity)
    if not valid:
        return jsonify({"message": "User not updated", "error": msg})
    return jsonify(amenity.__dict__)


@amenity_controller.route('/amenitys/<amenity_id>', methods=['DELETE'])
def delete_amenitys(amenity_id):
    valid, msg = amenity_manager.delete_amenity(amenity_id)
    if not valid:
        return jsonify({"message": "User not deleted", "error": msg})
    return jsonify({"message": "User deleted successfully"})
