
from scipy.spatial import distance as dist
from imutils.video import VideoStream
from imutils import face_utils
from threading import Thread
import numpy as np
import playsound
import argparse
import imutils
import time
import dlib
import cv2

def IsDrowsy():
        
    def alarm_ring(path):
        
        playsound.playsound(path)

    def EAR(eyes):
        
        vertical_1 = dist.euclidean(eyes[1], eyes[5])
        vertical_2 = dist.euclidean(eyes[2], eyes[4])

        horizontal = dist.euclidean(eyes[0], eyes[3])


        eye_aspect_ratio = (vertical_1 + vertical_2) / (2.0 * horizontal)


        return eye_aspect_ratio
    

    argp = argparse.ArgumentParser()
    argp.add_argument("-p", "--shape-predictor", default="shape_predictor_68_face_landmarks.dat",
        help="facial landmark predictor file path")
    argp.add_argument("-a", "--alarm", type=str, default="alert.wav",
        help=".WAV alarm file path")
    argp.add_argument("-w", "--camera", type=int, default=0,
        help="index of camera on system")
    args = vars(argp.parse_args())
    

    EAR_CLOSED_THRESH = 0.2
    FRAMES_THRESH = 48


    COUNT = 0
    RING = False


    print("[INFO] loading facial landmark predictor...")
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(args["shape_predictor"])


    (leftEyeStart, leftEyeEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
    (righttEyeStart, rightEyeEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]


    print("[INFO] starting video stream thread...")
    #vs = VideoStream(src=args["camera"]).start()
    vs = cv2.VideoCapture(0)
    time.sleep(1.0)

    while True:
        
        success, frame = vs.read()
        # h,w,l = frame.shape
        # v1 = w/2
        # v2 = h/2
        # frame = cv2.resize(frame, (v1,v2))
        frame = cv2.resize(frame, (450,400))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


        rects = detector(gray, 0)

        
        for rect in rects:
            
            shape = predictor(gray, rect)
            shape = face_utils.shape_to_np(shape)

            
            Eye_left = shape[leftEyeStart:leftEyeEnd]
            Eye_right = shape[righttEyeStart:rightEyeEnd]
            EAR_left = EAR(Eye_left)
            EAR_right = EAR(Eye_right)

            
            eye_aspect_ratio = (EAR_left + EAR_right) / 2.0

            
            leftEyeHull = cv2.convexHull(Eye_left)
            rightEyeHull = cv2.convexHull(Eye_right)
            cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
            cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

            
            if eye_aspect_ratio < EAR_CLOSED_THRESH:
                COUNT += 1

                
                if COUNT >= FRAMES_THRESH:
                    
                    if not RING:
                        RING = True

                        
                        if args["alarm"] != "":
                            t = Thread(target=alarm_ring,
                                args=(args["alarm"],))
                            t.deamon = True
                            t.start()

                    
                    cv2.putText(frame, "DROWSINESS ALERT!", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

            
            else:
                COUNT = 0
                RING = False

            
            cv2.putText(frame, "EAR: {:.2f}".format(eye_aspect_ratio), (300, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    
        
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
    

        if key == ord("q"):
            break


    cv2.destroyAllWindows()
    #vs.stop()
    vs.release()

IsDrowsy()