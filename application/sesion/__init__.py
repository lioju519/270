from flask import Blueprint

sesion = Blueprint('sesion', __name__, static_folder='static', template_folder='templates')

from . import routes