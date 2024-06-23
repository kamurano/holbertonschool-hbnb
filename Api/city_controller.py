from datetime import datetime
from flask import Blueprint, jsonify, request

from Model.city import City
from Repository.city_repository import CityRepository


city_controller = Blueprint('city_controller', __name__)

city_manager = CityRepository()

@city_controller.route('/countries', methods=['GET'])
def get_countries():
    countries = city_manager.get_all_countries()
    return jsonify(countries)


@city_controller.route("/countries/<country_code>")
def get_country_details(country_code):
    valid, msg = city_manager.get_country_details(country_code)
    if not valid:
        return jsonify({"message": "Country not found", "error": msg})
    return jsonify(msg)


@city_controller.route("/countries/<country_code>/cities")
def get_country_cities(country_code):
    cities = city_manager.get_country_cities(country_code)
    return jsonify(cities)


@city_controller.route("/cities", methods=['POST'])
def create_city():
    data = request.get_json()
    name = data.get('name')
    country_code = data['country_code']
    city = City(name, country_code)
    valid, msg = city_manager.create_new_city(city)
    if not valid:
        return jsonify({"message": "City not created", "error": msg})
    return jsonify(city.__dict__)


@city_controller.route("/cities", methods=["GET"])
def get_cities():
    cities = city_manager.get_all_cities()
    return jsonify(cities)

@city_controller.route("/cities/<city_id>", methods=["GET"])
def get_city_details(city_id):
    valid, msg = city_manager.get_city_details(city_id)
    if not valid:
        return jsonify({"message": "City not found", "error": msg})
    return jsonify(msg)