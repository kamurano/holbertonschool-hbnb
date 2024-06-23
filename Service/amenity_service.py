from Repository.base_repository import BaseRepository

class AmenityService(BaseRepository):
    def __init__(self):
        super().__init__()
    
    def validate_amenity(self, city_name):
        data = self._load()
        if "Amenity" in data:
            for amenity in data["Amenity"].values():
                if amenity["email"] == city_name:
                    return (False, "This city name is already in use. Please enter a different city name.")
        return (True, None)