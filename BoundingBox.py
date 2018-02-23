import matplotlib.pyplot as plt
import numpy as np
SAMPLE_RADIUS = 36
N0_OF_TEST = 4
import Tools

#Read input and draw convex hull polygon
input = np.loadtxt("input2.txt", dtype='i', delimiter=' ')
plt.scatter(input[:,0],input[:,1],s=6*6)
(outputLower, outputUpper) = Tools.convex_hull(input)
for i in range(int(outputLower.size/2)-1):
   plt.plot([outputLower[i][0],outputLower[i+1][0]],[outputLower[i][1],outputLower[i+1][1]],'r')
for i in range(int(outputUpper.size/2)-1):
   plt.plot([outputUpper[i][0],outputUpper[i+1][0]],[outputUpper[i][1],outputUpper[i+1][1]],'g')
plt.plot([outputLower[-1][0],outputUpper[0][0]],[outputLower[-1][1],outputUpper[0][1]],'y')
plt.plot([outputUpper[-1][0],outputLower[0][0]],[outputUpper[-1][1],outputLower[0][1]],'y')

#Draw sample circles inside polygon
sample_circles = Tools.testDensity(outputLower, outputUpper, SAMPLE_RADIUS, N0_OF_TEST)
plt.scatter(sample_circles[:,0],sample_circles[:,1],s=SAMPLE_RADIUS*SAMPLE_RADIUS, facecolors='none', edgecolors='k')
plt.show()

#Count N0 of points inside sample circles
points_inside = 0
for point in input:
   for circle in sample_circles:
      if Tools.isInsideCircle(point[0], point[1], circle[0], circle[1], SAMPLE_RADIUS):
         points_inside+=1
print(points_inside)         