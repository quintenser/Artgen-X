class Line(object):

    def __init__(self, vertices, color):
        self.vertices = vertices
        self.color = color

    def json(self):
        """Return a JSON version of the current object

        Return:
            dict: the object
        """
        return self.__dict__
