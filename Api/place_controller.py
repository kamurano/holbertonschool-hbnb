from datetime import datetime
from flask import Blueprint, jsonify, request

from Model.place import Place
from Repository.place_repository import PlaceRepository


place_controller = Blueprint('place_controller', __name__)

place_manager = PlaceRepository()

@place_controller.route('/places', methods=['POST'])
def create_place():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    address = data.get('address')
    city = data.get('city')
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    host_id = data.get('host_id')
    number_of_rooms = data.get('number_of_rooms')
    number_of_bathrooms = data.get('number_of_bathrooms')
    price_per_night = data.get('price_per_night')
    max_guests = data.get('max_guests')
    amenity_ids = data.get('amenity_ids')
    place = Place(name, description, address, city, latitude, longitude, host_id, number_of_rooms, number_of_bathrooms, price_per_night, max_guests, amenity_ids)
    valid, msg = place_manager.create_place(place)