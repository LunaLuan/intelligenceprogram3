from sklearn.datasets.samples_generator import make_moons

import cv2
import numpy as np

import random
from math import cos
import math


def generate_file_input(file_name, points):
    f = open(file_name + ".in",'w')
    f.write(str(len(points)) + "\n")
    for p in points:
        f.write(str(p[0]) + " " + str(p[1]) + "\n")

def test_case1():
    # random points
    img = np.ones((500, 500, 3), np.uint8)
    n = 10
    points = []
    
    for i in range(n):
        x = random.randint(10, 490)
        y = random.randint(10, 490)
        cv2.line(img,(x, y),(x, y),(255, 0, 0),3)
        
        points.append((x, y))
        
    generate_file_input('test_case_1', points)
    cv2.imshow('Test case 1', img)
    cv2.waitKey(0)
    
def test_case2():
    # random large points
    img2 = np.ones((500, 500, 3), np.uint8)
    n = 100
    points = []
    
    for i in range(n):
        x = random.randint(10, 490)
        y = random.randint(10, 490)
        # print (x, y)
        cv2.line(img2,(x, y),(x, y),(255, 0, 0),3)
        points.append((x, y))
        
    generate_file_input('test_case_2', points)
    cv2.imshow('test case 2', img2)
    cv2.waitKey(0)
    
def test_case3():
    pass
    
def test_case4():
    # first region:
    # random points
    img = np.ones((500, 500, 3), np.uint8)
    n = 100
    points = []
    
    for i in range(n):
        x = random.randint(10, 290)
        y = random.randint(10, 290)
        # print (x, y)
        cv2.line(img,(x, y),(x, y),(255, 0, 0),3)
        points.append((x, y))
        
    for i in range(n):
        x = random.randint(300, 490)
        y = random.randint(300, 490)
        # print (x, y)
        cv2.line(img,(x, y),(x, y),(255, 0, 0),3)
        points.append((x, y))
        
    generate_file_input('test_case_4', points)
    cv2.imshow('test case 4', img)
    cv2.waitKey(0)
    
def test_case5():
    img = np.ones((500, 500, 3), np.uint8)
    n = 100
    points = []
    
    for i in range(n):
        x = random.randint(10, 190)
        y = random.randint(10, 190)
        # print (x, y)
        cv2.line(img,(x, y),(x, y),(255, 0, 0),3)
        points.append((x, y))
        
    for i in range(n):
        x = random.randint(300, 490)
        y = random.randint(300, 490)
        # print (x, y)
        cv2.line(img,(x, y),(x, y),(255, 0, 0),3)
        points.append((x, y))
        
    generate_file_input('test_case_5', points)
    cv2.imshow('test case 5', img)
    cv2.waitKey(0)
    

test_case1()
test_case2()
test_case3()
test_case4()
test_case5()