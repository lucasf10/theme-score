from flask import Flask
from views import home, themes, vote_thumbs_up, vote_thumbs_down
from models import db

app = Flask(__name__)

app.config['MONGODB_HOST'] = 'mongodb://localhost:27017/theme-score_db'
app.debug = True

db.init_app(app)

# Routes
app.add_url_rule('/', view_func=home, methods=['GET', 'POST'])
app.add_url_rule('/vote_thumbs_up/<video_id>', view_func=vote_thumbs_up, methods=['POST', ])
app.add_url_rule('/vote_thumbs_down/<video_id>', view_func=vote_thumbs_down, methods=['POST', ])
app.add_url_rule('/themes', view_func=themes, methods=['GET', 'POST'])

if __name__ == "__main__":
    app.run()
