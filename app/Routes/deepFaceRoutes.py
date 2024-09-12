# app/Routes/deepFaceRoutes.py
from flask import Blueprint, request
from app.Controller.deepFaceController import verify_images, extract_text_from_images
from app.Flask.middleware import require_secret_key

bp = Blueprint('api', __name__)

@bp.route('/verify', methods=['POST'])
# @require_secret_key
def verify_images_route(): 
    return verify_images(request)


@bp.route('/extractText_fromImages', methods=['POST'])
# @require_secret_key
def extract_text_route(): 
    return extract_text_from_images(request)