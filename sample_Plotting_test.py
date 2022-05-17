# Python for undergraduate Engineers
# Ref: https://pythonforundergradengineers.com/plotting-sin-cos-with-matplotlib.html
# Program demonstrating basic use of a Python library by plotting a function
# If you can not access these libraries, make sure they are installed with PIP
# and that you are using the correct interpreter for Python (settings)
# From within VS Code, select a Python 3 interpreter by opening the Command Palette 
# Ctrl+Shift+P), start typing the Python: Select Interpreter command 
# to search, then select the command. 
# You can also use the Select Python Environment option 
# on the Status Bar if available (it may already show a 
# selected interpreter, too):
import numpy as np
from matplotlib import pyplot as plt
print('starting plot....(see seperate window for plot on toolbar')
# Set up x axis
x=np.arange(0,100,1)  # start,stop,step
# set up y axis
y = 4*((-1)**(x+1)/(2*x-1))
plt.title("Function Plot")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.plot(x,y)
plt.show()
