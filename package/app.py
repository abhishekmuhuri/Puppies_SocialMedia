from package import app, db, migrate
from package.models import User, Puppy
from flask import render_template
from routes import *


if __name__ == '__main__':
    app.run(debug=True)
