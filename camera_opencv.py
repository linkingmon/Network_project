import cv2
from base_camera import BaseCamera
cascPath = 'haarcascade_frontalface_dataset.xml'  # dataset
faceCascade = cv2.CascadeClassifier(cascPath)

class Camera(BaseCamera):
    video_source = 0

    @staticmethod
    def set_video_source(source):
        Camera.video_source = source

    @staticmethod
    def frames():
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
            for (x, y, w, h) in faces:
                face_image_gray = gray[y:y+h, x:x+w]
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                # res = predict_emotion(face_image_gray)
            # encode as a jpeg image and return it
            yield cv2.imencode('.jpg', frame)[1].tobytes()
