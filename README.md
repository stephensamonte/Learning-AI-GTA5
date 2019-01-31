# Learning-AI-GTA5

GTA 5 is the closest simulation of living life. The end goal of this project is to create a general AI that understands its surroundings and can make decisions on its own.

Disclaimer: I don't expect to succeed at creating a general AI. I do expect to create a program that can play GTA 5 well. I think it will be a mash up of multiple AIs. 

# Current Goals: 
- Capture the screen with OpenCV in python 
- Create functions to call Keyboard interaction

# Game Environment 
- We are getting getting a comptuer to play [GTA 5](https://www.rockstargames.com/V/) so you have to install GTA 5 on your computer.

## Installing GTA 5
- Install GTA 5 onto your computer. I baught [GTA 5 from Steam for $30](https://store.steampowered.com/sale/gta/). 

## Installing Mods for GTA 5 
Optional: You may install GTA 5 mods to have God mode control over the Game Environment. 
The purpose of mods is to beable to control the environment. I added 2 Tesla Car mods and sort of God Mode mod which allows me to control the traffic, weather, spawn cars, etc. 

I made this for others who wish add mods: [2018.12.24 How to Install GTA 5 Mods](https://docs.google.com/document/d/1k3z26HRxOlJ-v-ALhVgJuAP70ht3Ny2YI8Lj5H43o_I/edit?usp=sharing)


# Programming Environment: 
- This is a python program that is being modified in the [Python IDLE terminal](https://www.python.org/downloads/). This project utilizes [Python OpenCV](https://pypi.org/project/opencv-python/), [numpy](http://www.numpy.org/), and [pyscreenshot Website](https://pypi.org/project/pyscreenshot/). To run this project you will have to install python, python OpenCV, and numpy. 


## Installing Python 
- To install python follow the: [Python Windows Install](https://www.python.org/downloads/) 

## Installing Python OpenCV 
- To install OpenCV for python follow this: https://pypi.org/project/opencv-python/
- Verify that you have installed opencv-python by opening a python script shell (IDLE terminal) and runnign the following. IF correctly installed you should see what version of openCV you have installed. <br />
	Script: <br />
		>>> import cv2 <br />
		>>> cv2.__version__ <br />
	Result: <br />
		>>> '3.4.5'

## Installing Python Numpy 
- To install numpy run `pip install numpy` in a terminal. 
- Verify that you have numpy installed by opening a python script shell (IDLE terminal) and running the following. If correctly installed you should see what verion of numpy you have installed.: <br />
	Script: <br />
		>>> import numpy as np <br />
		>>> np.__verion__ <br />
	Result: <br />
		>>> '1.13.1' 

## Alternatives to setting up your environemnt: (DON'T DO THIS. IT IS A MORE COMPLICATED WAY TO SET UP YOUR MACHINE) 
- OpenCV Python install on windows: [installing OpenCV](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_setup/py_setup_in_windows/py_setup_in_windows.html#install-opencv-python-in-windows) 
1) Install Python 2.7: [Download](http://python.org/ftp/python/2.7.5/python-2.7.5.msi)
2) Install Numpy for python: [Download](http://sourceforge.net/projects/numpy/files/NumPy/1.7.1/numpy-1.7.1-win32-superpack-python2.7.exe/download)
3) Installing OpenCV 4.0.0: [Download](https://sourceforge.net/projects/opencvlibrary/files/)


## Installing pyscreenshot 
- [pyscreenshot Website](https://pypi.org/project/pyscreenshot/) is to be able to capture the screen of a computer. 
- [Pyscreenshot GitHub Project](https://github.com/ponty/pyscreenshot)
- Install pyscreenshot by running: `pip install pyscreenshot`
- pyscreenshot depends on 'Pillow' so install [Pillow](https://pillow.readthedocs.io/en/stable/) (Ubuntu: sudo apt-get install python-pil). Run `pip install Pillow`
- Verify that you have pyscreenshot installed by opening a python script shell (IDLE terminal) and running the following. If correctly installed you should see what verion of pyscreenshot you have installed.: <br />
	Script: <br />
		>>> import pyscreenshot as ImageGrab <br />
		>>> ImageGrab.__verion__ <br />
	Result: <br />
		>>> '0.5.1'

## Installing TensorFlow 


# Run the program
- Open the .py file in the Python IDLE terminal and hit run. 

# Journal: 
- 2018.12.23 Got interested in project.
- 2018.12.24 Learned how to install GTA 5 mods. Found out that I did not have enought memory with my full 500 gb external hard drive and internal 256 gb hard drive. 
- 2018.12.25 Christmas recieved amazon giftcards from Tita Faye and Tito Omar
- 2018.01.02 Ordered 4 tb external hard drive. 
- 2019.01.06 Recieved and Installed GTA 5 on 4 tb Hard Drive and installed mods. 
- 2019.01.07 Created GitHub Repository and readme.md file. Also added License.
- 2019.01.19 Added Screen Capture Function
- 2019.01.29 Set up computer environment for this project and added it to the README.md. Removed old screen capture program.
- 2019.01.31 Created ScreenCapture.py and updated read me on how to install pyscreenshot to capture computer screen. 

# References
- Used for while loop when to capture video[capture-video-data-from-screen-in-python](https://stackoverflow.com/questions/35097837/capture-video-data-from-screen-in-python)


