class Image(object):

    def __init__(self, width, height, background_color, lines, squares, circles, triangles):
        self.imageWidth = width
        self.imageHeight = height
        self.background_color = background_color
        self.lines = lines
        self.squares = squares
        self.circles = circles
        self.triangles = triangles

    def json(self):
        """Return a JSON version of the current object

        Return:
            dict: the object
        """
        self_dict = self.__dict__

        lines_dict = []
        for line in self.lines:
            lines_dict.append(line.json())
        self_dict["lines"] = lines_dict

        squares_dict = []
        for square in self.squares:
            squares_dict.append(square.json())
        self_dict["squares"] = squares_dict

        circles_dict = []
        for circle in self.circles:
            circles_dict.append(circle.json())
        self_dict["circles"] = circles_dict

        triangles_dict = []
        for triangle in self.triangles:
            triangles_dict.append(triangle.json())
        self_dict["triangles"] = triangles_dict

        return self_dict
