from flask_mongoengine import MongoEngine

db = MongoEngine()


class Theme(db.Document):

    name = db.StringField(max_length=200, required=True)
    score = db.DecimalField(default=0)

    def update_score(self):
        related_videos = Video.objects(theme=self)
        score = 0
        for video in related_videos:
            score += video.score
        self.score = score
        self.save()


class Video(db.Document):

    title = db.StringField(max_length=200, required=True)
    score = db.DecimalField(default=0)
    thumbs_up = db.IntField(default=0)
    thumbs_down = db.IntField(default=0)
    theme = db.ReferenceField(Theme, required=True)

    def add_thumbs_up(self):
        self.thumbs_up += 1
        self.save()
        self.update_score()

    def add_thumbs_down(self):
        self.thumbs_down += 1
        self.save()
        self.update_score()

    def update_score(self):
        self.score = self.thumbs_up - (self.thumbs_down/2)
        self.save()
        self.theme.update_score()
