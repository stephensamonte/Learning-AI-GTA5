# Archive | These are compoents of read me there are no longer in use

## [NOT IN USE] Installing pyscreenshot 
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