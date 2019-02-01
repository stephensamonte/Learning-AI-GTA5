
# Adapted from: https://github.com/stephensamonte/OpenCV-Leaf-Angle-Distribution-Detection
import math
import numpy as np
import cv2

def getEdges(blur_gray):    
    # Canny Edge Detection
    low_threshold = 50
    high_threshold = 250
    edges = cv2.Canny(blur_gray, low_threshold, high_threshold, apertureSize = 3)

    # Disaply Blurred Image
    #cv2.imshow('Edges image',edges)
    #Save Image
    cv2.imwrite("Edges.jpg", edges)
    return edges
    
# URL: https://docs.opencv.org/3.4/db/d5c/tutorial_py_bg_subtraction.html
def getCountour(image):
    # Retrieve photo 

    # Make a copy of the image
    im = np.copy(originalImage)
    #imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(image, 127, 255, 0)
    im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #extract contour data
    cnt = contours[0]
    M = cv2.moments(cnt)
    print("Moment", M)    
    
    cv2.drawContours(im, contours, -1, (255,0,0), 3)
    cv2.imwrite("contour.jpg", im)
    #cv2.imshow('contour',hierarchy)
    #return contours


def extractLines(edges):
    # Line Detection
    # This returns an array of r and theta values 
    #lines = cv2.HoughLines(edges,4,np.pi/180, 80)
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 85, maxLineGap=40)

    angle = 0.0
    count_stem_lines = 0

    for line in lines:
        x1, y1, x2, y2 = line[0]
        # add lines to image
        #cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)
    

    #cv2.imshow("Image lines", img)
    cv2.imwrite("verticalLines.jpg", vertical)
    