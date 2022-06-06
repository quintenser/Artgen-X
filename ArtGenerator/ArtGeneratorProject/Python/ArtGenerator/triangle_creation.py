from Utility.utility import random_float_value, random_float_value_based_on_percentage, random_color, random_int_value
from ImageDataClasses.triangle import Triangle


def generate_triangle(draw_image, image_width, image_height):
    """Create a triangle with random values.

    Args:
        draw_image (DrawImage): the DrawImage the triangle should be created on
        image_width (int): the width of the image
        image_height (int): the height of the image

    Returns:
        Triangle: Containing the triangle properties
    """
    triangle_width = random_float_value_based_on_percentage(-30, image_width, 30, image_width)
    triangle_height = random_float_value_based_on_percentage(-30, image_height, 30, image_height)

    position = (random_float_value(0, image_width) - (triangle_width / 2),
                random_float_value(0, image_height) - (triangle_height / 2))

    angle = (random_float_value_based_on_percentage(-30, image_height, 30, image_height),
             random_float_value_based_on_percentage(-30, image_height, 30, image_height))

    # triangle_shape = [(position),(shape properties), (angle properties)]
    triangle_shape = [position, (position[0] + triangle_width, position[1] + triangle_height), (position[0] + angle[0], position[1] + angle[1])]

    # Create triangle and fill with the given color
    color = random_color()

    draw_image.polygon(triangle_shape, fill=color)

    return Triangle(triangle_width, triangle_height, position, angle, color)


def recreate_triangle(draw_image, triangle):
    """Recreate the triangle with the given triangle_properties.

    Args:
        draw_image (DrawImage): the DrawImage the circle should be created on
        triangle (Triangle): Triangle properties that should be used

    Returns:
        Triangle: Containing the triangle properties
    """
    # Triangle_shape = [(location properties),(shape properties),(angle properties)]
    x1, y1 = triangle.position
    x2, y2 = triangle.angle
    triangle_shape = [triangle.position, (x1 + triangle.width, y1 + triangle.height), (x1 + x2, y1 + y2)]

    # recreate the triangle and fill with given color
    draw_image.polygon(triangle_shape, fill=triangle.color)

    return Triangle(triangle.width, triangle.height, triangle.position, triangle.angle, triangle.color)
