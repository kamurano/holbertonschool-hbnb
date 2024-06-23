from Repository.base_repository import BaseRepository
from Service.amenity_service import AmenityService

class AmenityRepository(AmenityService):
    def __init__():
        super().__init__()
    
    def get_all_amenities():
        data = self._load()
    
    def get_amenity_details(self, amenity_id):
        return self.get(amenity_id, "Amenity")

    def create_new_amenity(self, amenity_name):
        pass

    
    def update_amenity(self, amenity_id, amenity):
        data = self._load()
        if amenity_id not in data["Amenity"]:
            return (False, "Amenity not found")
        self.update(amenity)
        return (True, None)
    
    def delete_amenity(self, amenity_id):
        data = self._load()
        if amenity_id not in data["Amenity"]:
            return None
        self.delete(amenity_id, "Amenity")
        return "Amenity deleted successfully"