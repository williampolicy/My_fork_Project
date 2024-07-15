# namedtuple function accepts the following arguments to generate a class
from collections import namedtuple
>>> Point = namedtuple('Point',['x','y'])
>>> point = Point(100, 200)
>>> point
    Point(x=100, y=200)

# Which let you use both unpacking and iteration to access
>>> x, y = point
>>> print(f'({x}, {y})')
    (100, 200)
>>> for coordinate in point:
        print(coordinate)
    100
    200