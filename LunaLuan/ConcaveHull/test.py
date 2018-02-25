import numpy as np
import math
from scipy.spatial import Delaunay

def get_points(file_name):
    f = open(file_name, 'r')
    n = int(f.readline())
    
    points = []
    for i in range(n):
        numStr = f.readline().split()
        
        x = int(numStr[0])
        y = int(numStr[1])
        
        points.append([x, y])
    
    return points

def generate_file_input(file_name, points):
    f = open(file_name, 'w')
    f.write(str(len(points)) + "\n")
    for p in points:
        f.write(str(p[0]) + " " + str(p[1]) + "\n")


def distance(p1, p2):
    import math
    
    deltaX = 1.0 * (p1[0] - p2[0])
    deltaY = 1.0 * (p1[1] - p2[1])
    
    return math.sqrt(deltaX * deltaX + deltaY * deltaY)

def radius(tri):
    a = distance(tri[0], tri[1])
    b = distance(tri[1], tri[2])
    c = distance(tri[2], tri[0])
    
    s = (a + b + c) / 2.0
    
    t = a * b * c
    m = math.sqrt(16 * s * (s - a) * (s - b) * (s - c))
    return t / m
    


points = np.array(get_points("test_case_3.in"))
tri = Delaunay(points)

points_in_file = []


for t in points[tri.simplices]:
    print radius(t)
    if radius(t) > 60:
        continue
    
    points_in_file.append(t[0])
    points_in_file.append(t[1])
    points_in_file.append(t[2])
    
    # break
    
generate_file_input("test_case_3.out", points_in_file)

