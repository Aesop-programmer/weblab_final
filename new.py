from turtle import position
from matplotlib import projections
import serial
from main import *
import numpy as np
from numpy.linalg import inv, norm
import time
import data_receiver
from mathlib import *
from plotlib import *

import matplotlib.pyplot as plt


f = open('xyz3.txt', 'w')


class SerialArduino:
    def __init__(self):
        self.number = -1
        self.data = []
        self.numpydata = []
        self.init_list = []
        self.p = []
        self.tracker = IMUTracker(sampling=1000)

        get_inputbtn = int(input('input 0 to start: '))
        if get_inputbtn == 0:
            ser = serial.Serial('COM3',  baudrate=115200)
        while True and get_inputbtn == 0:
            plt.ion()
            line = ser.readline()
            self.check_inf(line)
            if self.number > 30:
                fig = plt.figure()
                
                fig.clf()
                fig.suptitle("drawing")
                ax = fig.add_subplot(111,projections="3d")
                ax.scatter3D(self.numpyposition, marker="o")
                ax.set_xlabel("X")
                ax.set_ylabel("Y")
                ax.set_zlabel("Z")
                plt.pause(0.01)
    
        plt.ioff()
        plt.show()
        ser.close()

    def check_inf(self, input_inf):
        self.number = self.number+1
        if input_inf != b'':
            get_cm = str(input_inf).split("'")[1].split("\\")[0]
            print('input_inf: ', get_cm)
            f.writelines(get_cm+"\n")
            a = get_cm.split(',')
            for item in a:
                item = float(item)
            self.data.append(a)
            self.numpydata = np.array(self.data, dtype=np.float)
            if(self.number == 30):
                self.init_list = self.tracker.initialize(self.numpydata[5:30])
                self.positions = []
                self.p = np.array([[0, 0, 0]]).T
                self.numpyposition = []
            elif(self.number > 30):
                a_nav, orix, oriy, oriz = self.tracker.attitudeTrack(
                    self.numpydata[self.number], self.init_list)
                a_nav_filtered = self.tracker.removeAccErr(a_nav, filter=False)
                v = self.tracker.zupt(a_nav_filtered, threshold=0.2)
                at = a_nav[0, np.newaxis].T
                vt = v[0, np.newaxis].T
                self.p = self.p + vt * self.dt + 0.5 * at * self.dt**2
                self.positions.append(self.p.T[0])
                self.numpyposition = np.array(self.positions)
            else:
                print(self.number)


if __name__ == '__main__':

    try:
        SerialArduino()

    except KeyboardInterrupt:
        print("Shutting down")
        f.close()
