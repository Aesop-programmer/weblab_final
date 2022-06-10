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
mod_time = time.ctime(os.path.getmtime('xyz3.txt'))
k = 0
p_final = np.array()


def load():
    global mod_time
    global k
    global p_final
    new_mtime = time.ctime(os.path.getmtime('xyz3.txt'))
    if new_mtime != mod_time:
        k = k+1
        mod_time = new_mtime
        file = open('xyz3.txt', 'r')
        data_1 = []
        j = 0
        for line in file.readlines()[(k-1)*100:k*100]:
            a = line.split(',')
            if(len(a) == 9):
                a[-1] = a[-1][0:-2]
                data_1.append(a)
        if(k > 1):
            data = np.array(data_1, dtype=np.float64)
            tracker = IMUTracker(sampling=100)
            # init
            init_list = tracker.initialize(data[5:30])
            # EKF
            a_nav, orix, oriy, oriz = tracker.attitudeTrack(
                data[30:], init_list)
            # filter a_nav
            a_nav_filtered = tracker.removeAccErr(a_nav, filter=False)
            # get velocity
            v = tracker.zupt(a_nav_filtered, threshold=0.2)
            # get position
            if(k == 1):
                p = tracker.positionTrack(a_nav_filtered, v)
                p_final = p[-1]
            else:
                p = tracker.positionTrack(a_nav_filtered, v)
                p = p.__add__(p_final)
                p_final = p[-1]
            print(p)


while(True):
    load()
