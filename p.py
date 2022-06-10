import numpy as np
import matplotlib.pyplot as plt
i = 0
x = [[1,2,3],[4,5,6],[7,8,9]]
y = [1,1,1]
x = np.array(x,np.float64())
y = np.array(y,np.float64())
while True and i< 1000:
    i = i +1
    x.tolist()
    f = open("xyz.txt","w")
    for j in range (3):
        f.write(str(x[j][0])+","+str(x[j][1])+","+str(x[j][2])+"\n")
    f.close()
    

