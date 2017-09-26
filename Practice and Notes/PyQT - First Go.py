import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon  

# 1) Basic Widget - Window
# http://zetcode.com/gui/pyqt5/firstprograms/
if __name__ == '__main__':
    
    app = QApplication(sys.argv) # every pyqt5 app needs an app object
                                 # argv is a list of cmd line args
    
    w = QWidget() # create base class for UI object, called a window
    w.resize(250,150) # resize
    w.move(300,300) # location on screen
    w.setWindowTitle('Simple') # window title text
    w.show() # displays on screen, before this it's just an object in memory
    
    sys.exit(app.exec_()) # ensures a clean exit when exit() is called
                          # app.exec_() is us entering the main loop of the app
                          
# 2) Basic Widget with Icon
# http://zetcode.com/gui/pyqt5/firstprograms/
class Example(QWidget): # create class which inherits from QWidget
    
    def __init__(self): # Example class constructor
        super(Example, self).__init__() # returns parent of Example (i.e. QWidget) and calls its constructor
        
        self.initUI() # create GUI by calling initUI method
        
    def initUI(self): # GUI creation method
        
        self.setGeometry(300,300,300,220) # combines resize(300,300) and move(300,220)
        self.setWindowTitle('Icon') # set title
        self.setWindowIcon(QIcon('web.png')) # set icon
        
        self.show() # show window
        
if __name__ == '__main__': # call main method
    
    app = QApplication(sys.argv) # create app
    ex = Example() # create class instance/object
    sys.exit(app.exec_()) # run main loop of app
    
# 3) Crop Simulation Tutorial
# https://pythonschool.net/pyqt/creating-a-basic-pyqt-application/
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class CropWindow(QMainWindow):
    """this class creates a main window to observe the frowth of a simulation"""
    
    # constructor
    def __init__(self):
        super(CropWindow, self).__init__() # call super class of constructor
        self.setWindowTitle("Crop Simulator") # set window title
        
def main(): # main method
    crop_simulation = QApplication(sys.argv) # create new application , enables cmd params/args
    crop_window = CropWindow() # create instance of main window
    crop_window.show() # make window visible
    crop_window.raise_() # raise instance to top of stack
    crop_simulation.exec_() # monitor appilcaton for events
    
if __name__ == '__main__':
    main() # main method, call main function (above)
