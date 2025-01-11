from flask import Blueprint, send_from_directory
import os

photos_bp = Blueprint('photos', __name__)

@photos_bp.route('/photos/<path:subpath>')
def get_photo(subpath):
    directory = os.path.join(os.getcwd(), 'images')
    return send_from_directory(directory, subpath)