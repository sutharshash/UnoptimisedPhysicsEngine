import cv2
import numpy

Viewport = numpy.zeros((600, 600, 3), dtype=numpy.uint8)
while True:
    cv2.imshow("Black Blank", Viewport)