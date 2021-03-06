# Learning-AI-GTA5

GTA 5 is the closest simulation of living life. The end goal of this project is to create a general AI that understands its surroundings and can make decisions on its own. If we humans can drive a car in GTA5 with just visual input then this AI should be able to too.

Disclaimer: I don't expect to succeed at creating a general AI. I do expect to create a program that can play GTA 5 well. I think it will be a mash up of multiple AIs. 

This is just a high aiming project to challenge me to learn new things. 

# NOTE: This project is no longer being worked on because I need a computer with a more powerful GPU. 
Currently I have a laptop with an integrated graphics card. It is is not powerful enought for machine learning training that I wish to do for this project. 

## Latest Showcase Video: 
[![Latest Showcase](https://img.youtube.com/vi/I6uy5MXM1rs/0.jpg)](https://www.youtube.com/watch?v=I6uy5MXM1rs)

# Current Goals: 
- Research How to make a general AI
- Use OpenCV to detect objects 
- Determine where the road is. 
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
- This is a python program that is being modified in the [Visual Studio Code](https://code.visualstudio.com/). This project utilizes [Python Interpreter Install](https://www.python.org/downloads/), [Python Visual Studio Code Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python), [Python OpenCV](https://pypi.org/project/opencv-python/), [numpy](http://www.numpy.org/), and [pyscreenshot Website](https://pypi.org/project/pyscreenshot/). To run this project you will have to install python, python OpenCV, and numpy. 

# Setting Up Visual Studio:  
1. Install [Python Interpreter Install](https://www.python.org/downloads/). When setting it up select to add python as an environment path. 
2. Add [Python Visual Studio Code Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) by selecting install. Check to make sure that the python interpreter you installed is being used. 
3. (Optional) Set up Visual Studio Code to open a bash terminal. Make sure that python is in the path of the bash terminal. Note: you don't have to use the terminal in visual studio you can just use a terminal not opened in visual studio. 
4. pip exists in your terminal if python is in the path. To add python to the path run the Pytho Interpreter SetUp and choose to add python to the path. 


DEPRICATED: This is a python program that is being modified in the [Python IDLE terminal](https://www.python.org/downloads/)

## Installing Python 
- To install python follow the: [Python Windows Install](https://www.python.org/downloads/) 

## Installing Python OpenCV 
- To install OpenCV for python follow this: https://pypi.org/project/opencv-python/ Run: `pip install opencv-python`
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


## Installing TensorFlow 


## Check to see everything is set up correctly
- Run `$ python testEnvironment.py`. You should see the version numbers of installed packages.
- Results: <br/>
	$ opencv: 4.0.0 <br/>
	$ numpy: 1.15.4 <br/>
	$ pyscreenshot: 0.5.1 <br/>

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
- 2019.01.31 Created ScreenCapture.py and updated read me on how to install pyscreenshot to capture computer screen. I was getting about 3 frames per second which is terrible. [Showcase](https://www.youtube.com/watch?v=nY062Zz0kbM&feature=youtu.be)
- 2019.01.31 Created MssScreenCapture.py and removed ScreenCapture.py. Mss captures frames at 45 FPS which is a big improvement from 3 frames per second with pyscreenshot [Showcase](https://www.youtube.com/watch?v=AZWjkMOSMxU&feature=youtu.be)
- 2019.01.31 Added image processing: Black&White, GaussianBlur, EdgeDeteciton, and line detection. [Showcase](https://www.youtube.com/watch?v=I6uy5MXM1rs&feature=youtu.be)


# References
- Used for while loop when to capture video[capture-video-data-from-screen-in-python](https://stackoverflow.com/questions/35097837/capture-video-data-from-screen-in-python)
- Used for screen capture [Python MSS](https://python-mss.readthedocs.io/examples.html)
- [Stephen Tan's OpenCV Leaf Angle Detection](https://github.com/stephensamonte/OpenCV-Leaf-Angle-Distribution-Detection)
