import cv2
import numpy as np

import random


def generate_file_input(file_name, points):
    f = open(file_name + ".in", 'w')
    f.write(str(len(points)) + "\n")
    for p in points:
        f.write(str(p[0]) + " " + str(p[1]) + "\n")


def test_case1():
    img = np.ones((500, 500, 3), np.uint8)
    n = 10
    points = []

    for i in range(n):
        x = random.randint(10, 490)
        y = random.randint(10, 490)
        cv2.line(img, (x, y), (x, y), (255, 0, 0), 3)

        points.append((x, y))

    generate_file_input('test_case_1', points)
    cv2.imshow('Test case 1', img)
    cv2.waitKey(0)


def test_case2():
    img2 = np.ones((500, 500, 3), np.uint8)
    n = 100
    points = []

    for i in range(n):
        x = random.randint(10, 490)
        y = random.randint(10, 490)
        # print (x, y)
        cv2.line(img2, (x, y), (x, y), (255, 0, 0), 3)
        points.append((x, y))

    generate_file_input('test_case_2', points)
    cv2.imshow('Test case 2', img2)
    cv2.waitKey(0)


def test_case3():
    img = np.ones((500, 500, 3), np.uint8)
    n = 200
    points = []
    i = 0

    while i < n:
        x = random.randint(0, 490)
        y = random.randint(- 490, 490)

        if ((x * x + y * y) > 10000) and ((x * x + y * y) < 40000):
            x += 250
            y += 250

            cv2.line(img, (x, y), (x, y), (255, 0, 0), 3)
            i += 1

            points.append((x, y))

    generate_file_input('test_case_3', points)
    cv2.imshow('Test case 3', img)
    cv2.waitKey(0)


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
        cv2.line(img, (x, y), (x, y), (255, 0, 0), 3)
        points.append((x, y))

    for i in range(n):
        x = random.randint(300, 490)
        y = random.randint(300, 490)
        # print (x, y)
        cv2.line(img, (x, y), (x, y), (255, 0, 0), 3)
        points.append((x, y))

    generate_file_input('test_case_4', points)
    cv2.imshow('Test case 4', img)
    cv2.waitKey(0)


def test_case5():
    img = np.ones((500, 500, 3), np.uint8)
    n = 100
    points = []

    for i in range(n):
        x = random.randint(10, 190)
        y = random.randint(10, 190)
        # print (x, y)
        cv2.line(img, (x, y), (x, y), (255, 0, 0), 3)
        points.append((x, y))

    for i in range(n):
        x = random.randint(300, 490)
        y = random.randint(300, 490)
        # print (x, y)
        cv2.line(img, (x, y), (x, y), (255, 0, 0), 3)
        points.append((x, y))

    generate_file_input('test_case_5', points)
    cv2.imshow('Test case 5', img)
    cv2.waitKey(0)


def test_case6():
    img = np.ones((500, 500, 3), np.uint8)
    n = 200
    points = []
    i = 0

    while i < n:
        x = random.randint(0, 490)
        y = random.randint(- 490, 490)

        if ((x * x + y * y) >= 10000) and ((x * x + y * y) <= 40000):
            x += 250
            y += 250

            cv2.line(img, (x, y), (x, y), (255, 0, 0), 3)
            i += 1

            points.append((x, y))

    for i in range(10):
        x = random.randint(0, 100)
        y = random.randint(0, 100)

        x += 250
        y += 250

        cv2.line(img, (x, y), (x, y), (255, 0, 0), 3)
        points.append((x, y))

    generate_file_input('test_case_6', points)
    cv2.imshow('Test case 6', img)
    cv2.waitKey(0)

def test_case7():
    img = np.ones((500, 500, 3), np.uint8)
    n = 200
    points = []
    i = 0

    while i < n:
        x = random.randint(0, 490)
        y = random.randint(- 490, 490)

        if ((x * x + y * y) > 10000) and ((x * x + y * y) < 40000):
            x += 250
            y += 250

            cv2.line(img, (x, y), (x, y), (255, 0, 0), 3)
            i += 1

            points.append((x, y))

    for i in range(10):
        x = random.randint(-10, 10)
        y = random.randint(-10, 10)

        x += 250
        y += 250

        cv2.line(img, (x, y), (x, y), (255, 0, 0), 3)
        points.append((x, y))

    generate_file_input('test_case_7', points)
    cv2.imshow('test case 7', img)
    cv2.waitKey(0)





test_case1()
test_case2()
test_case3()
test_case4()
test_case5()
test_case6()
test_case7()