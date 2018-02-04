import matplotlib.pyplot as plt
import numpy as np

N = 20
x = np.random.rand(N)
y = np.random.rand(N)
xMax = 0
yMax = 0
xMin = 999
yMin = 999
for i in range(N):
    if x[i]>xMax:
        xMax = x[i]
    if y[i]>yMax:
        yMax = y[i]
    if x[i]<xMin:
        xMin = x[i]
    if y[i]<yMin:
        yMin = y[i]
plt.scatter(x,y)
plt.plot([xMin,xMin],[yMin,yMax])
plt.plot([xMin,xMax],[yMax,yMax])
plt.plot([xMax,xMax],[yMax,yMin])
plt.plot([xMax,xMin],[yMin,yMin])
plt.show()