import cv2
import numpy as np
from openpyxl.styles.builtins import output

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

        cv2.line(img,(x, y),(x, y),(255, 0, 0),3)
        
    for o_index in range(len(outputs) - 1):
        p1 = ouputs[o_index]
        p2 = ouputs[o_index + 1]
        
        cv2.line(img, p1, p2,(0, 0, 255),1)
        
    p1 = ouputs[0]
    p2 = ouputs[len(outputs) - 1]
        
    cv2.line(img, p1, p2,(0, 0, 255),1) 
        
    cv2.imshow('test', img)
    cv2.waitKey(0)
    

inputs = get_points('4_points.out')  
outputs = get_points('triangle.in') 

visualyze(inputs, outputs)  

