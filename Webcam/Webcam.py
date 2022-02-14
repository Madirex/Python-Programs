import cv2
import numpy as np
import ctypes

class Webcam:
    def __init__(self):
        ctypes.windll.user32.MessageBoxW(0, "MANTENER presionada la tecla para que haga efecto:\n- Tecla q: Salir\n- Tecla w: Modo normal\n- Tecla e: Escala de grises\n- Tecla r: Escala de grises ignorando el color rojo", "Información", 0)

        webcam = cv2.VideoCapture(0)
        actual_type = 0

        while webcam.isOpened():
            ret, frame = webcam.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            if cv2.waitKey(1) == ord('q'):
                break
            if cv2.waitKey(1) == ord('w'):
                actual_type = 0
            if cv2.waitKey(1) == ord('e'):
                actual_type = 1
            if cv2.waitKey(1) == ord('r'):
                actual_type = 2
            
            actual_frame = frame
            if actual_type == 1:
                actual_frame = gray
            if actual_type == 2:
                ret, mask = cv2.threshold(frame[:, :,2], 190, 255, cv2.THRESH_BINARY)
                mask3 = np.zeros_like(frame)
                mask3[:, :, 0] = mask
                mask3[:, :, 1] = mask
                mask3[:, :, 2] = mask

                red = cv2.bitwise_and(frame, mask3)

                gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                frame  = cv2.cvtColor(gray_scale, cv2.COLOR_GRAY2BGR)
                gray_scale = cv2.bitwise_and(frame, 255 - mask3)
                actual_frame =  gray_scale + red
            
            self.detect_face_and_eye(actual_frame)

            cv2.imshow('webcam', actual_frame)
        webcam.release()
        cv2.destroyAllWindows()

    def detect_face_and_eye(self, actual_frame):
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
        faces = face_cascade.detectMultiScale(actual_frame, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(actual_frame, (x, y), (x + w, y + h), (255, 0, 0), 5)
            roi_gray = actual_frame[y:y+w, x:x+w]
            roi_color = actual_frame[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 5)


if __name__ == '__main__':
    Webcam()