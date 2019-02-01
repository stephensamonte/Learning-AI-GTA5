
# Adapted from: https://python-mss.readthedocs.io/examples.html

# This records about 45 frames per second on my comptuer 

import time
import cv2
import mss
import numpy

import Logic

def screen_capture():
    with mss.mss() as sct:
        # Part of the screen to capture
        monitor = {"top": 150, "left": 0, "width": 800, "height": 640}

        while "Screen capturing":
            last_time = time.time()

            # Get raw pixels from the screen, save it to a Numpy array
            img = numpy.array(sct.grab(monitor))

            # # Display the picture
            # cv2.imshow("OpenCV/Numpy normal", img)

            # Display the picture in grayscale
            # cv2.imshow('OpenCV/Numpy grayscale',
            #            cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))

            # Process the image
            image_processing(img)

            print("fps: {}".format(1 / (time.time() - last_time)))

            # Press "q" to quit
            if cv2.waitKey(25) & 0xFF == ord("q"):
                cv2.destroyAllWindows()
                break

def image_processing(img): 
    # Image Processing and determine action to commit to
    base = Logic.CommandCenter()
    base.command(img)


# Run program
if __name__ == '__main__':
    screen_capture()