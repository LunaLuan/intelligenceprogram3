import cv2
import numpy as np


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
    
def visualyze_triangle(inputs, ouputs):
    img = np.ones((500, 500, 3), np.uint8)
    
    for i in inputs:
        x = i[0]
        y = i[1]

        cv2.line(img,(x, y),(x, y),(255, 0, 0),3)
        
    for o_index in range(0, len(outputs), 3):
        p1 = ouputs[o_index]
        p2 = ouputs[o_index + 1]
        p3 = ouputs[o_index + 2]
        
        cv2.line(img, p1, p2,(0, 0, 255),1)
        cv2.line(img, p2, p3,(0, 0, 255),1)
        cv2.line(img, p3, p1,(0, 0, 255),1)
 
        
    cv2.imshow('test', img)
    cv2.waitKey(0)
    

inputs = get_points('test_case_3.in')  
outputs = get_points('test_case_3.out') 

visualyze_triangle(inputs, outputs)  

