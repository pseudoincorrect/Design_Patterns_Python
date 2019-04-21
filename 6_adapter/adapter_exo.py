import unittest

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

class Square:
    def __init__(self, side=0):
        self.side = side

class SquareToRectangleAdapter:
    def __init__(self, square):
        self.square = square

    @property
    def width(self):
        return self.square.side

    @property
    def height(self):
        return self.square.side
        

class Wrong_SquareToRectangleAdapter:
    def __init__(self, square):
        self.width = square.side
        self.height = square.side

def calculate_area(rc):
    return rc.width * rc.height

class adapterTests(unittest.TestCase):
    def test_SquareToRectangleAdapter(self):
        sq = Square(3)
        area = calculate_area(SquareToRectangleAdapter(sq))
        wrong_area = calculate_area(Wrong_SquareToRectangleAdapter(sq))
        self.assertEqual(9, area)
        self.assertEqual(9, wrong_area)
        
 
if __name__ == '__main__':
    sq = Square(3)
    adapt = Wrong_SquareToRectangleAdapter(sq)
    print(adapt.height)
    
    # unittest.main()