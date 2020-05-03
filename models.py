from app import db

class Player(db.Model):
    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key=True)
    first = db.Column(db.String(), nullable=False)
    last = db.Column(db.String(), nullable=False)
    team = db.Column(db.String())

    def __init__(self, first, last, team):
        self.first = first
        self.last = last
        self.team = team

    def insert(self): 
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def serialize(self):
        return {
            'id': self.id,
            'firstname': self.first,
            'lastname': self.last,
            'birthdate': self.team,
        }

    def __repr__(self):
        return '<id {}>'.format(self.id)


class Game(db.Model):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)
    home_away = db.Column(db.String(), nullable=False)
    venue = db.Column(db.String())

    def __init__(self, home_away, venue):
        self.home_away = home_away
        self.venue = venue

    def insert(self): 
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
    
    def serialize(self): 
        return {
            'id': self.id,
            'home_away': self.home_away,
            'venue': self.venue
        }

    def __repr__(self): 
        return '<id {}>'.format(self.id)