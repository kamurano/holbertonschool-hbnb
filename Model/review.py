from basemodel import BaseModel

class Reviews(BaseModel):
    def __init__(self, place_id, user_id, rating, comment):
        super().__init__()
        self.place_id = place_id
        self.user_id = user_id
        self.rating = rating
        self.comment = comment

    def __str__(self):
        return self.id