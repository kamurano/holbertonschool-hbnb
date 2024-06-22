from basemodel import BaseModel

class Amenitie(BaseModel):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return self.id