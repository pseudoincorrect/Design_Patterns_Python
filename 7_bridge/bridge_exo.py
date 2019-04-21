
# class Shape:
#     def __init__(self):
#         self.name = None
#
#
# class Triangle(Shape):
#     def __init__(self):
#         super().__init__()
#         self.name = 'Triangle'
#
#
# class Square(Shape):
#     def __init__(self):
#         super().__init__()
#         self.name = 'Square'
#
#
# class VectorSquare(Square):
#     def __str__(self):
#         return f'Drawing {self.name} as lines'
#
#
# class RasterSquare(Square):
#     def __str__(self):
#         return f'Drawing {self.name} as pixels'

# imagine VectorTriangle and RasterTriangle are here too

import unittest
from abc import ABC, abstractmethod
import os

class Shape:
    def __init__(self, name, renderer):
        self.renderer = renderer
        self.name = name
    def __str__(self):
        return 'Drawing {} as {}'.format(self.name, self.renderer.what_to_render_as())

class Triangle(Shape):
    def __init__ (self, renderer):
        super().__init__("Triangle", renderer)

class Square(Shape):
    def __init__ (self, renderer):
        super().__init__("Square", renderer)


class Renderer(ABC):
    @abstractmethod
    def what_to_render_as(self):
        pass
        
class RasterRenderer(Renderer):
    def what_to_render_as(self):
        return "pixels"
       
class VectorRenderer(Renderer):
    def what_to_render_as(self):
        return "lines"


if __name__ == "__main__":
    os.system('clear') 
    print(str(Triangle(RasterRenderer())))
    print(str(Square(VectorRenderer())))
    
# TODO: reimplement Shape, Square, Triangle and Renderer/VectorRenderer/RasterRenderer
# str(Triangle(RasterRenderer())) # Drawing Triangle as Pixels