class Circle(object):

    def __init__(self, width, height, position, color, line_width, is_filled):
        self.width = width
        self.height = height
        self.position = position
        self.color = color
        self.line_width = line_width
        self.is_filled = is_filled

    def json(self):
        """Return a JSON version of the current object

        Return:
            dict: the object
        """
        return self.__dict__
