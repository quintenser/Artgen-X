from Utility.utility import random_int_value, random_float_value, clamp
from ImageDataClasses.image import Image
from fileManager import FileManager

config = FileManager.readDefaultConfig()

parents = []
max_parents = config.max_parents

mutation_chance = config.small_mutation_chance
big_mutation_chance = config.big_mutation_chance
small_mutation_max_value = 20
big_mutation_max_value = 70


def add_parent(image):
    """Add image to parents list.

    Args:
        image (Image): Image that should be added
    """
    parents.append(image)
    if len(parents) > max_parents:
        del parents[0]


def reset_algorithm():
    """Reset algorithm
    """
    global parents
    parents = []


def create_offspring():
    """Create new image properties based on liked parents.

    Returns:
        Image: image properties
    """
    child = combine_parents()
    if will_mutate():
        return mutate_child(child, mutation_type())
    return child


def select_random_parent():
    """Select random parent form parents list.

    Returns:
        Image: image properties
    """
    return parents[random_int_value(0, len(parents) - 1)]


def select_random_from_list(list):
    """Select random element form given list.

    Args:
        list ([]): the list a item should be selected from

    Returns:
        Object: a object from the list (type can change depending on the given list)
    """
    return list[random_int_value(0, len(list) - 1)]


def combine_parents():
    """Selects random parents and combines their properties into a new child.

    Returns:
        Image: image properties
    """
    parent = select_random_parent()
    lines = []
    lines_amount = len(parent.lines)
    for _ in range(lines_amount):
        parent = select_random_parent()
        lines.append(select_random_from_list(parent.lines))

    parent = select_random_parent()
    squares = []
    squares_amount = len(parent.squares)
    for _ in range(squares_amount):
        parent = select_random_parent()
        squares.append(select_random_from_list(parent.squares))

    parent = select_random_parent()
    circles = []
    circles_amount = len(parent.circles)
    for _ in range(circles_amount):
        parent = select_random_parent()
        circles.append(select_random_from_list(parent.circles))

    parent = select_random_parent()
    triangles = []
    triangle_amount = len(parent.triangles)
    for _ in range(triangle_amount):
        parent = select_random_parent()
        triangles.append(select_random_from_list(parent.triangles))

    parent = select_random_parent()
    return Image(parent.imageWidth, parent.imageHeight, parent.background_color, lines, squares, circles, triangles)


def will_mutate(): return random_int_value(0, 100) <= mutation_chance


def mutation_type():
    """Get the value that should be used for the mutations.

    Returns:
        float: mutation value
    """
    if random_int_value(0, 100) <= big_mutation_chance:
        return big_mutation_max_value
    return small_mutation_max_value


def mutate_child(child, mutation):
    """Mutate values of child.

    Args:
        child (Image): image properties
        mutation (float): mutation value

    Returns:
        Image: image properties
    """
    if will_mutate():
        child.background_color = color_mutation(child.background_color, mutation)

    for i in range(len(child.lines)):
        child.lines[i] = mutate_line(child.lines[i], mutation)

    for i in range(len(child.squares)):
        child.squares[i] = mutate_square(child.squares[i], mutation)

    for i in range(len(child.circles)):
        child.circles[i] = mutate_circle(child.circles[i], mutation)

    for i in range(len(child.triangles)):
        child.triangles[i] = mutate_triangle(child.triangles[i], mutation)

    return child


def mutate_line(line, mutation):
    """Mutate the values of a Line.

    Args:
        line (Line): Line properties
        mutation (float): mutation value

    Returns:
        Line: Line properties
    """
    if will_mutate():
        line.color = color_mutation(line.color, mutation)

    for i in range(len(line.vertices) - 1):
        if will_mutate():
            x, y = line.vertices[i]
            line.vertices[i] = (value_mutation_float(x, mutation), value_mutation_float(y, mutation))
    return line


def mutate_square(square, mutation):
    """Mutate the values of a Square.

    Args:
        square (Square): Square properties
        mutation (float): mutation value

    Returns:
        Square: Square properties
    """
    if will_mutate():
        square.width = value_mutation_float(square.width, mutation)
        square.height = value_mutation_float(square.height, mutation)

    if will_mutate():
        x, y = square.position
        square.position = (value_mutation_float(x, mutation), value_mutation_float(y, mutation))

    if will_mutate():
        square.color = color_mutation(square.color, mutation)
    return square


def mutate_circle(circle, mutation):
    """Mutate the values of a Circle.

    Args:
        circle (Circle): Circle properties
        mutation (float): mutation value

    Returns:
        Circle: Circle properties
    """
    if will_mutate():
        circle.width = value_mutation_float(circle.width, mutation)
        circle.height = value_mutation_float(circle.height, mutation)

    if will_mutate():
        x, y = circle.position
        circle.position = (value_mutation_float(x, mutation), value_mutation_float(y, mutation))

    if will_mutate():
        circle.color = color_mutation(circle.color, mutation)
    return circle


def mutate_triangle(triangle, mutation):
    """Mutate the values of a Triangle.

    Args:
        triangle (Triangle): Triangle properties
        mutation (float): mutation value

    Returns:
        Triangle: Triangle properties
    """
    if will_mutate():
        triangle.width = value_mutation_float(triangle.width, mutation)
        triangle.height = value_mutation_float(triangle.height, mutation)

    if will_mutate():
        x1, y1 = triangle.position
        x2, y2 = triangle.angle
        triangle.position = (value_mutation_float(x1, mutation), value_mutation_float(y1, mutation))
        triangle.angle = (value_mutation_float(x2, mutation), value_mutation_float(y2, mutation))

    if will_mutate():
        triangle.color = color_mutation(triangle.color, mutation)
    return triangle


def value_mutation_float(value, mutation):
    """Changes the value by a random amount depending on the 'mutation_value'.

    Args:
        value (float): value to mutate

    Returns:
        float: mutated value
    """
    return random_float_value((100 - mutation) / 100 * value, (100 + mutation) / 100 * value)


def color_mutation(color, mutation):
    """Changes the color value by a random amount depending on the 'mutation_value'.

    Args:
        color (tuple(int)): tuple values to mutate

    Returns:
        tuple(int): mutated color
    """
    r, g, b = color
    r = random_int_value((100 - mutation) / 100 * r, (100 + mutation) / 100 * r)
    r = clamp(r, 0, 255)
    g = random_int_value((100 - mutation) / 100 * g, (100 + mutation) / 100 * g)
    g = clamp(g, 0, 255)
    b = random_int_value((100 - mutation) / 100 * b, (100 + mutation) / 100 * b)
    b = clamp(b, 0, 255)
    return (r, g, b)
