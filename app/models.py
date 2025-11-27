from app import db

class Anime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    gifs = db.relationship('Gif', backref='anime')

    def __repr__(self):
        return f"<Anime {self.title}>"
    
class Gif(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(200), nullable=False)
    anime_id = db.Column(db.Integer, db.ForeignKey('anime.id'), nullable=False)

    def __repr__(self):
        return f"<Gif {self.path} for Anime ID {self.anime_id}>"