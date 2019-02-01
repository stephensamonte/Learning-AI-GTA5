
## This file is for checking to see if your 
## environment is set up correctly 

# Check if opencv-python is set up correctly 

print("-------- Package Versions ------- ")

import cv2
print("opencv: " + cv2.__version__)

# Check numpy
import numpy as np
print("numpy: " + np.__version__)

# # Check pyscreenshot to capture images. 
# # This is no longer being used as it was replaced by mss
# import pyscreenshot as ImageGrab
# print("pyscreenshot: " + ImageGrab.__version__)

import mss
print("mss:" + mss.__version__)
