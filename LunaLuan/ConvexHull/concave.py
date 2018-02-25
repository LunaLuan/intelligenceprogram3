import cv2
import numpy as np

def concave_hull(points):
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
    return lower[:-1] + upper[:-1]

def get_points(file_name):
    f = open(file_name, 'r')
    n = int(f.readline())
    
    points = []
    for i in range(n):
        numStr = f.readline().split()
        
        x = int(numStr[0])
        y = int(numStr[1])
        
        points.append((x, y))
    
    return points

def visualyze(inputs, ouputs):
    img = np.ones((500, 500, 3), np.uint8)
    
    for i in inputs:
        x = i[0]
        y = i[1]

        cv2.line(img,(x, y),(x, y),(255, 0, 0),2)
        
#     for o_index in range(len(outputs) - 1):
#         p1 = ouputs[o_index]
#         p2 = ouputs[o_index + 1]
#         
#         cv2.line(img, p1, p2,(0, 0, 255),1)
#         
#     p1 = ouputs[0]
#     p2 = ouputs[len(outputs) - 1]
#         
#     cv2.line(img, p1, p2,(0, 0, 255),1) 
#         
    cv2.imshow('test', img)
    cv2.waitKey(0)
    
    

    

inputs = get_points('test_case_3.in')  
outputs = get_points('triangle.in') 

visualyze(inputs, outputs)  

