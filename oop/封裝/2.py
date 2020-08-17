class Rectangle:

    def __init__(self, width, height):
        self.hidden_width = width
        self.hidden_height = height

    def get_width(self):
        return self.hidden_width

    def get_height(self, height):
        return self.hidden_height

    def set_width(self, width):
        self.hidden_width = width

    def set_height(self, height):
        self.hidden_height = height

    def getarea(self):
        return self.hidden_width*self.hidden_height


# r = Rectangle(5, 2)
# r.set_width(10)
# r.set_height(20)
# print(r.getarea())
