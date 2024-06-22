from Persistence.IPersistence import IPersistence

class BaseRepository(IPersistence):

    def save(self, entity):
        pass

    def get(self, entity_id, entity_type):
        pass

    def update(self, entity):
        pass


    def delete(self, id):
        pass
