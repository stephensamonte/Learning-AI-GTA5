
import numpy as np
import cv2
import pyscreenshot as ImageGrab
import time

def screen_capture():
    
    last_time = time.time()

    while (True): 
        # grab fullscreen
        # im = ImageGrab.grab()

        # Capture a section of the screen
        screenImg = ImageGrab.grab(bbox=(50,50,800,640))  # X1,Y1,X2,Y2

        print('Loop took {} seconds',format(time.time()-last_time))
        
        # Displays image in new window
        # cv2.imshow('test', np.array(screenImg))
        
        # Convert color from BGR to RGB and display in a window 
        cv2.imshow('window', cv2.cvtColor(np.array(screenImg), cv2.COLOR_BGR2RGB))

        last_time = time.time()
        
        # show image in a window
        # screenImg.show()

        # Exit when escape key is pressed
        key = cv2.waitKey(33)
        if key==27:
            cv2.destroyAllWindows()
            break


# Run program
if __name__ == '__main__':
    screen_capture()
