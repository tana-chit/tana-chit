import cv2
from djitellopy import Tello

tello = Tello()
tello.connect()

tello.streamon()
frame_read = tello.get_frame_read()

tello.takeoff()
tello.move_up(160)
tello.move_forward(100)
cv2.imwrite("picture.png", frame_read.frame)
time.sleep(3)
tello.land()
