import numpy as np
import matplotlib.pyplot as plt

#1
plt.plot([1,2,3,4]) #plot these values where [1,2,3,4] are the y values, [0,1,2,3] (i.e. indexes) are the x values
plt.ylabel('y axis') #set y axis text label

#2
plt.plot([1,2,3,4],[1,4,9,16]) #plot x and y values

#3
plt.plot([1,2,3,4], [1,4,9,16], 'ro') #'ro' represents colour and type of plots
plt.axis([0, 6, 0, 20]) #sets axes

#4
t = np.arange(0.,5.,0.2) #evenly spaced points from 0 to 5 with 0.2 intervals
plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g^') #plot 3 lines with different values and styles

plt.show() #show graph