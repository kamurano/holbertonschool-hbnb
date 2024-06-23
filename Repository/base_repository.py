import json
import os

from Persistence.IPersistence import IPersistenceManager

class BaseRepository(IPersistenceManager):
    def __init__(self):
        self.FILE_PATH = "data.json"
        
        if not os.path.isfile(self.FILE_PATH):
            with open(self.FILE_PATH, "w") as file:
                json.dump({}, file)
        
            
    def save(self, entity):
        entity_id = entity.id
        entity_type = type(entity).__name__
        data = self._load()
        if entity_type not in data:
            data[entity_type] = {}
        data[entity_type][entity_id] = entity.__dict__
        with open(self.FILE_PATH, "w") as file:
            json.dump(data, file)        

    def get(self, entity_id, entity_type):
        data = self._load()
        if entity_type not in data:
            return None
        if entity_id not in data[entity_type]:
            return None
        return data[entity_type][entity_id]

    def update(self, entity):
        entity_id = entity.id
        entity_type = type(entity).__name__
        data = self._load()
        if entity_type not in data:
            return None
        if entity_id not in data[entity_type]:
            return None
        data[entity_type][entity_id] = entity.__dict__
        with open(self.FILE_PATH, "w") as file:
            json.dump(data, file)
        
    def delete(self, entity_id, entity_type):
        data = self._load()
        if entity_type not in data:
            return None
        if entity_id not in data[entity_type]:
            return None
        del data[entity_type][entity_id]
        with open(self.FILE_PATH, "w") as file:
            json.dump(data, file)
        
    def _load(self):
        with open(self.FILE_PATH, "r") as file:
            return json.load(file)