class DefaultConfig(object):

    def __init__(self, width, height, circleAmount, squareAmount, lineAmount, triangleAmount, generations_until_algorithm_is_used, small_mutation_chance, big_mutation_chance, max_parents):
        self.imageWidth = width
        self.imageHeight = height
        self.circleAmount = circleAmount
        self.squareAmount = squareAmount
        self.lineAmount = lineAmount
        self.triangleAmount = triangleAmount
        self.generations_until_algorithm_is_used = generations_until_algorithm_is_used
        self.small_mutation_chance = small_mutation_chance
        self.big_mutation_chance = big_mutation_chance
        self.max_parents = max_parents

    def json(self):
        """Return a JSON version of the current object

        Return:
            dict: the object
        """
        return self.__dict__
