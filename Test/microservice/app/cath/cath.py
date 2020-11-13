from flask import Blueprint, jsonify, current_app
from app.cath.datamodule import *
from app.decorators import requires_login

cath_bp = Blueprint('cath_bp', __name__)

#@requires_login()
@cath_bp.route('/getCaths')
def getCaths():
    conn = current_app.db_connection
    return jsonify(get_caths(conn))
