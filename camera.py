import cv2
from keras.models import load_model
import numpy as np
from skimage import io

cascPath = 'haarcascade_frontalface_dataset.xml'  # dataset
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)  # 0 for web camera live stream
model = load_model('model.h5')
model._make_predict_function()


def predict_emotion(face_image_gray):
    global cnt
    resized_img = cv2.resize(face_image_gray, (48, 48),
                             interpolation=cv2.INTER_AREA)
    image = resized_img.reshape(1, 48, 48, 1) / 255.
    res = np.argmax(model.predict(image))
    res = 7
    return res


def camera_stream():
    while True:
        # Capture frame-by-frame
        res = 7
        ret, frame = video_capture.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            face_image_gray = gray[y:y+h, x:x+w]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            res = predict_emotion(face_image_gray)

        # Display the resulting frame in browser
        return cv2.imencode('.jpg', frame)[1].tobytes(), res
