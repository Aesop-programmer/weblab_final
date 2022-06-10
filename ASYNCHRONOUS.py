import numpy as np
from numpy.linalg import inv, norm

import data_receiver
from mathlib import *
from plotlib import *
from main import *
import time
import os.path
import numpy as np
import pandas as pd

file = open('xyz3.txt','r')
data_1 = []

for line in file.readlines():
    a = line.split(',')
    if(len(a)==9):
        a[-1] = a[-1][0:-1]
        data_1.append(a)
data = np.array(data_1, dtype=np.float64)
tracker = IMUTracker(sampling=1000)
init_list = tracker.initialize(data[5:30])
a_nav, orix, oriy, oriz = tracker.attitudeTrack(
                data[30:], init_list)
a_nav_filtered = tracker.removeAccErr(a_nav, filter=False)
v = tracker.zupt(a_nav_filtered, threshold=0.2)
p = tracker.positionTrack(a_nav_filtered, v)
f= open("xyz_plot.txt","w")
p.tolist()
for j in range(len(p)):
    f.write(str(p[j][0])+","+str(p[j][1])+","+str(p[j][2])+"\n")
f.close()