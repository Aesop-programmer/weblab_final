import matplotlib.pyplot as plt
import numpy as np
import time
import os.path
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
x = list()
y = list()
z = list()
file = open('xyz_plot.txt', 'r')
for line in file.readlines():
    a = line.split(',')
    a[-1] = a[-1][0:-2]
    x.append(a[0])
    y.append(a[1])
    z.append(a[2])
    plt.scatter(x, y, z)
    plt.show()
    plt.pause(0.0001)
plt.close()
