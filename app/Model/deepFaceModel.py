from deepface import DeepFace
import os

class DeepFaceModel:
    @staticmethod
    def verify_images(img1, img2, models, backends):
        results = []
        # Save images temporarily
        img1_path = 'img1_temp.jpg'
        img2_path = 'img2_temp.jpg'

        img1.save(img1_path)
        img2.save(img2_path)

        try:
            # Iterate through all backends and models for face detection and verification
            for backend in backends:
                for model_name in models:
                    try:
                        result = DeepFace.verify(img1_path, img2_path, model_name=model_name, detector_backend=backend)
                        results.append({f'{backend}_{model_name}': result})
                    except Exception as e:
                        results.append({f'{backend}_{model_name}': str(e)})
        finally:
            # Clean up temporary files
            if os.path.exists(img1_path):
                os.remove(img1_path)
            if os.path.exists(img2_path):
                os.remove(img2_path)

        return results

    @staticmethod
    def analyze_images(img1, img2, models, backends):
        analysis_results = []
        # Save images temporarily
        img1_path = 'img1_temp.jpg'
        img2_path = 'img2_temp.jpg'

        img1.save(img1_path)
        img2.save(img2_path)

        try:
            # Iterate through all backends and models for face detection and analysis
            for backend in backends:
                for model_name in models:
                    try:
                        result = DeepFace.analyze(img1_path, img2_path, models=model_name, detector_backend=backend)
                        analysis_results.append({f'{backend}_{model_name}': result})
                    except Exception as e:
                        analysis_results.append({f'{backend}_{model_name}': str(e)})
        finally:
            # Clean up temporary files
            if os.path.exists(img1_path):
                os.remove(img1_path)
            if os.path.exists(img2_path):
                os.remove(img2_path)

        return analysis_results
