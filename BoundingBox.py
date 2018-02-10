import matplotlib.pyplot as plt
import numpy as np

input = np.loadtxt("testInput.txt", dtype='i', delimiter=' ')
xMax = 0
yMax = 0
xMin = 999
yMin = 999
for i in range(int(input.size/2)-1):
    if input[i][0]>xMax:
        xMax = input[i][0]
    if input[i][1]>yMax:
        yMax = input[i][1]
    if input[i][0]<xMin:
        xMin = input[i][0]
    if input[i][1]<yMin:
        yMin = input[i][1]
plt.scatter(input[:,0],input[:,1])
plt.plot([xMin,xMin],[yMin,yMax],'r')
plt.plot([xMin,xMax],[yMax,yMax],'r')
plt.plot([xMax,xMax],[yMax,yMin],'r')
plt.plot([xMax,xMin],[yMin,yMin],'r')
plt.show()