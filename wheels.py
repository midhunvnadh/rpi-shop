import cv2
from motor_driver import motorL, motorR
from time import sleep

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_upperbody.xml'
)

video_width = 320
video_height = 240

camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, video_width)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, video_height)
camera.set(cv2.CAP_PROP_FPS, 10)


def wheels():
    while True:
        ret, frame = camera.read()
        frame = cv2.flip(frame, 1)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        humans = face_cascade.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100)
        )

        curr_x = 0
        is_close = False
        for (x, y, w, h) in humans:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(frame, f"x:{w}", (x+w-100, y-5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 1)
            if (w > 350):
                is_close = True
            curr_x = int(x + w/2)
            break

        if (len(humans) == 0):
            is_close = False

        cv2.putText(frame, "x", (int((video_width) / 2), 15),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

        if (curr_x != 0):
            offset = curr_x - int((video_width) / 2)
            cv2.putText(
                frame,
                "x",
                (curr_x-10, 15),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.9,
                (255, 0, 0),
                2
            )
            cv2.putText(frame, f"Offset: {offset}", (10, int(video_height-100)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
            if (is_close):
                cv2.putText(frame, f"Object is near!", (100, 160),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
            if (not is_close):
                if (offset < -30):
                    print("Motor L moving forward!")
                    motorL.move_forward(0.05)
                    motorL.stop()
                elif (offset > 30):
                    print("Motor R moving forward!")
                    motorR.move_forward(0.05)
                    motorR.stop()

        cv2.imshow('Object Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    camera.release()
    cv2.destroyAllWindows()
