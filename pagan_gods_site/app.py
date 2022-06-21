import os

from flask import Flask
# from dotenv import load_dotenv

from pagan_gods_site.ext import db, site
from pagan_gods_site.ext.site import navbar

def create_app():
	"""Factory"""
	app = Flask(__name__)
	
	app.secret_key = os.getenv('SESSION_SECRET_KEY')
	# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../tables/database.db'
    #app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://srzcpwgrdpducd:e2d91d2a7a092b77807b9d218e9bae8ef2cb1562a12513fe8577c015900e9871@ec2-52-203-118-49.compute-1.amazonaws.com:5432/dfv2ku5nod2ui'

	db.init_app(app)
	navbar.nav.init_app(app)
	site.init_app(app)

	return app

# load_dotenv()