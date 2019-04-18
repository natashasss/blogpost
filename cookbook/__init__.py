import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'

#### database setup ####
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:r00tpassw0rd@localhost:5433/onlinecookbook'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
#Migrate(app,db)

#### login configs ####
login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'users.login'



#### Blueprint configs ####

from cookbook.core.views import core
from cookbook.users.views import users
from cookbook.blog_posts.views import blog_posts
from cookbook.error_pages.handlers import error_pages

app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(blog_posts)
app.register_blueprint(error_pages)