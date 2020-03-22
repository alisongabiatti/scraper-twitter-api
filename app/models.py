from app import db
import datetime


# Tweets Class
class Tweets(db.Model):
    __tablename__ = 'tweets'
    id = db.Column(db.Integer, primary_key=True)
    hashtag = db.Column(db.String(120))
    name = db.Column(db.String(120))
    followers = db.Column(db.Integer)
    date = db.Column(db.DateTime())
    text = db.Column(db.Text)
    location = db.Column(db.String(120))
    lang = db.Column(db.String(120))
    update_time = db.Column(db.DateTime(), default=datetime.datetime.now())

    def __init__(self, hashtag, name, followers, date, text, location, lang, update_time):
        self.hashtag = hashtag
        self.name = name
        self.followers = followers
        self.date = date
        self.text = text
        self.location = location
        self.lang = lang
        self.update_time = datetime.datetime.now()
