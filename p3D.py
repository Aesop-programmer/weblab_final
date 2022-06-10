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
mod_time = time.ctime(os.path.getmtime('xyz_plot.txt'))
k = 0


def draw():
    new_mtime = time.ctime(os.path.getmtime('xyz3.txt'))
    global x
    global y
    global z
    global k
    if new_mtime != mod_time:
        k = k + 70
        mod_time = new_mtime
        file = open('xyz_plot.txt', 'r')
        for line in file.readlines()[k-70:k-1]:
            a = line.split(',')
            a[-1] = a[-1][0:-2]
            x.append(a[0])
            y.append(a[1])
            z.append(a[2])
            plt.scatter(x, y, z)
            plt.show()
            plt.pause(0.0001)


while(True):
    draw()
plt.close()
