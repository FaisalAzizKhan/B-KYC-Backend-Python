# app/Repository/deepFaceRepository.py

from app.Model.deepFaceModel import DeepFaceModel

def verify_images(img1, img2):
    return DeepFaceModel.verify_images(img1, img2)
