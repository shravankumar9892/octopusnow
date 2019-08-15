from flask import Flask
from app.config import Config
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object(Config)
# Add these to the config.py file

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = '465'
app.config['MAIL_PASSWORD'] = 'Keralaonam9892'
app.config['MAIL_USERNAME'] = 'shravankumarshetty9892@gmail.com' 
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)
from app import routes
