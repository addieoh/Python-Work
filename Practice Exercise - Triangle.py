import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_origin(self):
        return (self.x**2 + self.y**2)**0.5

    def euclidean_distance(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

    def manhattan_distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def angle_between(self, other):
        vert = other.y - self.y
        horiz = other.x - self.x
        return math.atan2(vert, horiz) 

def near_equality(v, w):
    if abs(w-v) <= (10**-6):
        return True
    else:
        return False
        
class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def side_lengths(t):
        a = (Point.euclidean_distance(p2, p1))
        b = (Point.euclidean_distance(p2, p3))
        c = (Point.euclidean_distance(p1, p3))
        return (a, b, c)
    
    def angles(t):
        a = (Point.euclidean_distance(p2, p1))
        b = (Point.euclidean_distance(p2, p3))
        c = (Point.euclidean_distance(p1, p3))
        d = math.acos(((c**2)-(a**2)-(b**2)) / (-2*a*b))
        e = math.asin((a * math.sin(d)) / c)
        f = (math.pi - d - e)
        return [f, e, d]
        
    def side_classification(t):
        a = (Point.euclidean_distance(p1, p2))
        b = (Point.euclidean_distance(p2, p3))
        c = (Point.euclidean_distance(p1, p3))
        if (near_equality(a, b) == True):
            if (near_equality(b, c) == True):
                return "equilateral"
            else:
                return "isosceles"
        elif (near_equality(b, c) == True):
            return "isosceles"
        elif (near_equality(a, c) == True):
            return "isosceles"
        else:
            return "scalene"
        
    def angle_classification(t):
        a = (Point.euclidean_distance(p2, p1))
        b = (Point.euclidean_distance(p2, p3))
        c = (Point.euclidean_distance(p1, p3))
        d = math.acos(((c**2)-(a**2)-(b**2)) / (-2*a*b))
        e = math.asin((a * math.sin(d)) / c)
        f = (math.pi - d - e)
        g = math.pi / 2
        h = math.pi / 3
        if (near_equality(d, g) == True) or (near_equality(e, g) == True) or (near_equality(f, g) == True):
            return "right"
        elif (near_equality(d, h) == True) or (near_equality(e, h) == True) or (near_equality(f, h) == True):
            return "equiangular"
        elif (d > g) or (e > g) or (f > g):
            return "obtuse"
        else:
            return "acute"

    def is_right(t):
        a = (Point.euclidean_distance(p2, p1))
        b = (Point.euclidean_distance(p2, p3))
        c = (Point.euclidean_distance(p1, p3))
        d = math.acos(((c**2)-(a**2)-(b**2)) / (-2*a*b))
        e = math.asin((a * math.sin(d)) / c)
        f = (math.pi - d - e)
        g = math.pi / 2
        if near_equality(d, g) == True:
            return True
        elif near_equality(e, g) == True:
            return True
        elif near_equality(f, g) == True:
            return True
        else:
            return False

    def perimeter(t):
        a = (Point.euclidean_distance(p2, p1))
        b = (Point.euclidean_distance(p2, p3))
        c = (Point.euclidean_distance(p1, p3))
        return (a+b+c)
    
    def area(t):
        a = (Point.euclidean_distance(p2, p1))
        b = (Point.euclidean_distance(p2, p3))
        c = (Point.euclidean_distance(p1, p3))
        s = ((a + b + c)/2)
        g = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return (g)

p1 = Point(1, 2)
p2 = Point(2, 3)
p3 = Point(3, 2)
t = Triangle(p1, p2, p3)
