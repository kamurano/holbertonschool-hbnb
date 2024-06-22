# from datetime import datetime
# import uuid
# CurrentTime = datetime.now()
# UniqueId = uuid.uuid4()

# class City:
#     def __init__(self, name, country_code):
#         self.id = UniqueId
#         self.name = name
#         self.country_code = country_code

#     def __str__():
#         return "Hello Guys"

#     def details():
#         return "DICT"


# class Country:
#     def __init__(self, name, country_code, cities):
#         self.name = name
#         self.country_code = country_code
#         self.cities = cities

# class Amenitie:
#     def __init__(self, name):
#         self.id = UniqueId
#         self.name = name

#     def __str__():
#         return "Helllo"

# class Place:
#     def __init__(self, name, description, address, city, latitude, longitude, host_id, number_of_rooms, number_of_bathtooms, price_per_night, maxx_guests, amenity_ids, reviews):
#         pass
#     def __str__():
#         return "Heleki bilmirem bu nedi"

# class Reviews:
#     def __init__(self, place_id, user_id, rating, comment):
#         self.id = UniqueId
#         self.place_id = place_id
#         self.user_id = user_id
#         self.rating = rating
#         self.comment = comment

#     def __str__():
#         return "REVIEEWS RETURNERERERER"

# class User:
#     def __init__(self, email, password, first_name, last_name):
#         self.id = UniqueId
#         self.email = email
#         self.password = password
#         self.first_name = first_name
#         self.last_name = last_name

#     def __str__():
#         return "user"





class CountryCitiesRepository:
    def __init__(self, countries, cities):
        self.countries = countries
        self.cities = cities
    def __str__():
        return "CountryCities"
    def get_all_countries():
        pass
    def get_all_cities():
        pass
    def get_country_details(country_code):
        pass
    def get_city_details(city_id):
        pass
    def get_country_cities(country_code):
        pass
    def create_new_city(name, country_code):
        pass
    def update_city(city_id):
        pass
    def delete_city(city_id):
        pass

class AmenitiesRepository:
    def __init__(self, amenities):
        self.amenities = amenities

    def __str__():
        return "Amenities Repo"

    def get_all_amenities():
        pass

    def get_amenity_details(amenity_id):
        pass

    def create_new_amenity(amenity_name):
        pass

    def update_amenity(amenity_id):
        pass

    def delete_amenity(amenity_id):
        pass

class AmenitiesService:

    def __init__():
        pass

    def __str__():
        pass

    def validaete_amenity(city_name):
        pass

class PlacesRepository:
    def __init__(self, places):
        self.places = places

    def __str__():
        return "Places Repo"

    def get_all_places():
        pass

    def get_place_details(place_id):
        pass

    def create_new_place(name, description, address, city_id, latitude, longitude, host_id, number_of_rooms, number_of_bathrooms, price_per_night, max_guests, amenity_ids):
        pass

    def update_place(place_id):
        pass

    def delete_place(place_id):
        pass

class PlacesService:
    def __init__():
        pass

    def __self__():
        return "Place service"

    def validate_place(country, city, amenities):
        pass

    def validate_coordinates(latitude, longitude):
        pass

    def validate_quantity(number):
        pass