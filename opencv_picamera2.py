#!/usr/bin/python3

import cv2

from picamera2 import Picamera2
import libcamera

cv2.startWindowThread()

picam2 = Picamera2()
config = picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)})
config["transform"] = libcamera.Transform(hflip=0, vflip=1)
picam2.configure(config)
picam2.start()

while True:
    im = picam2.capture_array()
    cv2.imshow("Camera", im)