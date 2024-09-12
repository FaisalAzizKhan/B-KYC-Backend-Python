# app\Controller\deepFaceController.py

from flask import request, jsonify
from app.Model.deepFaceModel import DeepFaceModel
from PIL import Image 
import easyocr
import io
 
# DeepFace configuration
def verify_images(req: request):
   
    if 'img1' not in req.files or 'img2' not in req.files:
        return jsonify({'error': 'Both images are required'}), 400

    img1 = req.files['img1']
    img2 = req.files['img2']

    # backends = [ 'opencv', 'ssd', 'dlib', 'mtcnn', 'fastmtcnn', 'retinaface', 'mediapipe', 'yolov8', 'yunet', 'centerface' ]
    # models = ["VGG-Face", "Facenet", "Facenet512", "OpenFace", "DeepFace", "DeepID", "ArcFace", "Dlib", "SFace", "GhostFaceNet"]
    models = ["VGG-Face", "Facenet", "ArcFace"]
    backends = [ 'opencv',  'retinaface',  'yolov8' ]

    try:
        verifyResults = DeepFaceModel.verify_images(img1, img2, models, backends) 
        # analyzeResults = DeepFaceModel.analyze_images(img1, img2, models, backends) 

        return jsonify(verifyResults)
    except Exception as e:
        return jsonify({'error': str(e)}), 500 

# EasyOCR configuration
def extract_text_from_images(req: request):

    if 'image1' not in req.files: return jsonify({'error': 'Image file is required'}), 400

    image_file = req.files['image1']
    try:
        image_bytes = image_file.read()
        image = Image.open(io.BytesIO(image_bytes))

        if image.mode != 'RGB':
            image = image.convert('RGB')

        reader = easyocr.Reader(['en']) 
        results = reader.readtext(image_bytes)
        extracted_text = ' '.join([result[1] for result in results])

        return jsonify({'extracted_text': extracted_text}), 200
    
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500
