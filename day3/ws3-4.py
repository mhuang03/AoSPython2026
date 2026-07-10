# Problem 4: Collinear Points
# Design a function that accepts a list of n tuples, each representing the coordinates
# of a point in 2D space, and returns True if all the points are collinear, and False otherwise.
# Two or more points are collinear if they all lie on the same straight line.
# Hint: Use the slope formula to calculate the slope of the line between points.

def slope(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    if x1 == x2:
        return None

    return (y2 - y1) / (x2 - x1)

def collinear(points):
    if len(points) <= 2:
        return True

    m = slope(points[0], points[1])
    for pt in points[2:]:
        if slope(pt, points[0]) != m:
            return False
    return True


print(collinear([(0,0), (1,1), (2,2)]))
print(collinear([(0,3), (1,6), (2,9)]))
print(collinear([(0,0), (1,2), (1,1)]))
print(collinear([(1,0), (1,2), (1,1)]))