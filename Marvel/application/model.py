from application import db, app


class Comic(db.Document):
    name = db.StringField(unique=True)
    description = db.StringField(unique=True)
    comicStrip = db.ListField()
    stories =  db.ListField()
    events =  db.ListField()
    series =  db.ListField()

class Creator(db.Document):
    fullName =  db.StringField()
    creatorComics =  db.StringField()
    creatorStories =  db.StringField()
    creatorEvents =  db.StringField()
    creatorSeries =  db.StringField()
    modified = db.DateField()

class Story(db.Document):
    title =  db.StringField()
    storyDesc =  db.StringField()
    type = db.StringField()
    storyComic =  db.StringField()
    characters =  db.StringField()
    creator =  db.StringField()


