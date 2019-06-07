import cv2
from base_camera import BaseCamera
import numpy as np
from skimage import io
import sys
run_face_expression = None
try:
    run_face_expression = int(sys.argv[1])
except:
    print("type \"python3 app.py 0\" for close face expression")
    print("type \"python3 app.py 1\" for open face expression")
    sys.exit(0)

cascPath = 'haarcascade_frontalface_dataset.xml'  # dataset
faceCascade = cv2.CascadeClassifier(cascPath)

if run_face_expression:
    from keras.models import load_model
    model = load_model('model.h5')
    model._make_predict_function()


def predict_emotion(face_image_gray):
    resized_img = cv2.resize(face_image_gray, (48, 48),
                             interpolation=cv2.INTER_AREA)
    image = resized_img.reshape(1, 48, 48, 1) / 255.
    res = np.argmax(model.predict(image))
    return res


class Camera(BaseCamera):
    video_source = 0

    @staticmethod
    def set_video_source(source):
        Camera.video_source = source

    @staticmethod
    def frames():
        global run_face_expression
        camera = cv2.VideoCapture(Camera.video_source)
        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')

        while True:
            # read current frame
            _, frame = camera.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE)

            # Draw a rectangle around the faces
            BaseCamera.res = 7
            for (x, y, w, h) in faces:
                face_image_gray = gray[y:y+h, x:x+w]
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                if run_face_expression:
                    BaseCamera.res = predict_emotion(face_image_gray)
            # encode as a jpeg image and return it
            yield cv2.imencode('.jpg', frame)[1].tobytes()
