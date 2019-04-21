import os

class GraphicObject:
    def __init__(self, color=None):
        self._name = "group"
        self.color = color
        self.children = []
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def _print(self, st, depth):
        if (self.color == None):
            st.append("*" * depth + self.name + "\n")
            for child in self.children:
                child._print(st, depth+1)
        else:
            st.append("*" * depth + self.name + self.color + "\n")

    def __str__(self):
        st = []
        self._print(st, 0)
        return "".join(st)
    

class Circle(GraphicObject):
    @property
    def name(self): return "Circle"

class Square(GraphicObject):
    @property
    def name(self): return "Square"


if __name__ == '__main__':
    os.system('clear') 
    drawing = GraphicObject()
    drawing.name = 'My Drawing'
    drawing.children.append(Square('Red'))
    drawing.children.append(Circle('Yellow'))

    group = GraphicObject()  # no name
    group.children.append(Circle('Blue'))
    group.children.append(Square('Blue'))
    drawing.children.append(group)

    print(drawing)
