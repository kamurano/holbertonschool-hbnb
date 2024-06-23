from Repository.base_repository import BaseRepository
from Service.user_service import UserService
from Model.user import User


class UserRepository(UserService):
    def __init__(self):
        super().__init__()
    
    def get_users(self):
        data = self._load()
        return list(data["User"].values())
    
    def get_user_details(self, user_id):
        
        return self.get(user_id, "User")
        
    
    def create_user(self, user):
        valid, msg = self.validate_email(user.email)
        if not valid:
            return (False, msg)
        if not self.validate_creds(user.first_name, user.last_name):
            return (False, msg)
        self.save(user)
        return (True, user.id)
    
    def update_user(self, user_id, user):
        valid, msg = self.validate_email(user.email)
        if not valid:
            return (False, msg)
        if not self.validate_creds(user.first_name, user.last_name):
            return (False, msg)
        data = self._load()
        if user_id not in data["User"]:
            return (False, "User not found")
        self.update(user)
        return (True, None)
    
    def delete_user(self, user_id):
        data = self._load()
        if user_id not in data["User"]:
            return (False, "User not found")
        self.delete(user_id, "User")
        return (True, None)