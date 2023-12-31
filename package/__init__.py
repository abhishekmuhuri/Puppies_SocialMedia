from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap


app = Flask(__name__, template_folder='../templates',static_folder='../static')
Bootstrap(app)

app.config['SECRET_KEY'] = 'my-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

#login_manager = LoginManager(app)
#login_manager.login_view = 'login'  # Specify the login view
