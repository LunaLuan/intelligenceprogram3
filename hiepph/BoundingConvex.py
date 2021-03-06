class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class QuadTree():
    def __init__(self, points, rectangle):
        self.coord = rectangle
        xmin, ymin, xmax, ymax = rectangle

        # get only points in rectangle
        self.points = []
        for point in points:
            if xmin <= point.x && point.x <= xmax && ymin <= point.y && point.y <= ymax:
                self.points.append(point)

    def separate(self, D):
        # makes 4 children
        x1, y1, x2, y2 = self.coord
        # |0 1|
        # |2 3|
        children = [
            QuadTree(self.points, [x1, y1, (x1+x2)/2, (y1+y2)/2]),
            QuadTree(self.points, [(x1+x2)/2, y1, (x1+x2)/2, (y1+y2)/2]),
            QuadTree(self.points, [(x1+x2)/2, (y1+y2)/2, (x1+x2)/2, y2]),
            QuadTree(self.points, [(x1+x2)/2, (y1+y2/2), x2, y2])
        ]

        # check density (number of points in coord) in each child
        res = set()
        for child in children:
            if len(child.points) <= D:
                # update set of bounding coord
                xchild1, ychild1, xchild2, ychild2 = child.coord
                res.update(set({Point(xchild1, ychild1), Point(xchild1, ychild2),
                                Point(xchild2, ychild1), Point(xchild2, ychild2)}))
            else:
                res.update(child.separate(D))

        # Return set of points of bounding box
        return res


def boundingRectangle(points):
    X, Y = [], []
    for point in points:
        X.append(point.x)
        Y.append(point.y)

    return [min(X), min(Y), max(X), max(Y)]


def boundingConvex(points, D):
    # corner case
    if len(points) == 0:
        return []
    if len(points) == 1:
        return [points[0].x, points[0].y]

    # find rectangle bounding box
    rec = boundingRectangle(points)

    # initialize quadtree
    t = QuadTree(points, rec)

    # continuouslly separate until reach threshold D
    return t.separate(D)
