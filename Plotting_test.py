# Python for undergraduate Engineers
# Ref: https://pythonforundergradengineers.com/plotting-sin-cos-with-matplotlib.html
# Program demonstrating basic use of a Python library by plotting a function
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
