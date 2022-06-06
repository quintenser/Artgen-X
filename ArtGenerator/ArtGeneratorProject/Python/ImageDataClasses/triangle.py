class Triangle(object):

    def __init__(self, width, height, position, angle, color):
        self.width = width
        self.height = height
        self.position = position
        self.angle = angle
        self.color = color

    def json(self):
        """Return a JSON version of the current object

        Return:
            dict: the object
        """
        return self.__dict__
