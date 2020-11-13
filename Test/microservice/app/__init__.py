from flask import Flask, current_app
from flask_cors import CORS
from flaskext.mysql import MySQL
from app.cath.cath import cath_bp

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    CORS(app)
	
    mysql = MySQL()
    mysql.init_app(app)
    app_ctx = app.app_context()
    app_ctx.push()
    current_app.db_connection = mysql.connect()

    app.register_blueprint(cath_bp)

    return app