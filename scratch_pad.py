import math
import numpy as np
from matplotlib import pyplot as plt
# Generate a list of values for x
n_list = list(np.arange(0, 100, 1))
# x must be an element of the list each time we iterate
plt.title("Function Plot")  # Caption for the title
plt.xlabel("x axis caption")  # Caption for the X Axis
plt.ylabel("y axis caption")  # Caption for the Y Axis
for x in n_list: # calculate y for each value of x
    y=(math.sqrt((1+(((x+1)**2)/16))*9)+1)
    plt.plot(x, y)  # This actually creates the plot
plt.show()  # Because nothing happens if you don't do this