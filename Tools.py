import numpy as np
from random import randint
import matplotlib.path as mpltPath

def convex_hull(np_points):
    """Computes the convex hull of a set of 2D points.

    Input: an iterable sequence of (x, y) pairs representing the points.
    Output: a list of vertices of the convex hull in counter-clockwise order,
      starting from the vertex with the lexicographically smallest coordinates.
    Implements Andrew's monotone chain algorithm. O(n log n) complexity.
    """
    points = tuple(map(tuple, np_points))
    # Sort the points lexicographically (tuples are compared lexicographically).
    # Remove duplicates to detect the case we have just one unique point.
    points = sorted(set(points))

    # Boring case: no points or a single point, possibly repeated multiple times.
    if len(points) <= 1:
        return points

    # 2D cross product of OA and OB vectors, i.e. z-component of their 3D cross product.
    # Returns a positive value, if OAB makes a counter-clockwise turn,
    # negative for clockwise turn, and zero if the points are collinear.
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    # Build lower hull 
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Build upper hull
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # Concatenation of the lower and upper hulls gives the convex hull.
    # Last point of each list is omitted because it is repeated at the beginning 
    # of the other list. 
    
    return (np.asarray(lower[:-1]), np.asarray(upper[:-1]))

def isInsideCircle(x, y, center_x, center_y, radius):
   dx = abs(x-center_x)
   dy = abs(y-center_y)
   R = radius
   if dx>R : 
      return False
   if dy>R : 
      return False
   if dx + dy <= R : 
      return True
   if dx^2 + dy^2 <= R^2 : 
      return True
   else: 
      return False
   
def testDensity(lower, upper, radius, n0ofTest):
   xMin = lower[0][0]
   xMax = upper[0][0]
   yMin = 999
   yMax = 0
   for i in range(int(upper.size/2)-1):
      if yMax < upper[i][1]:
         yMax = upper[i][1]
   for i in range(int(lower.size/2)-1):
      if yMin > lower[i][1]:
         yMin = lower[i][1]
   if xMin + radius >= xMax - radius or yMin + radius >= yMax - radius:
      return False
   testPoint = []
   for i in range(0,n0ofTest):
      xTest = randint(xMin + radius, xMax - radius)
      yTest = randint(yMin + radius, yMax - radius)
      while(True):         
         path = mpltPath.Path(tuple(map(tuple,np.concatenate((lower, upper), axis=0))))
         inside = path.contains_points([[xTest,yTest]])  
         if inside[0] == True:
            testPoint.append([xTest,yTest])
            break
         else:            
            xTest = randint(xMin + radius, xMax - radius)
            yTest = randint(yMin + radius, yMax - radius)
   return np.asarray(testPoint)