from Utility.utility import random_float_value, random_int_value, percentage_of_value, random_color
from ImageDataClasses.line import Line


def generate_line(draw_image, image_width, image_height):
    """Create a line with random values.

    Args:
        draw_image (DrawImage): the DrawImage the line should be created on
        image_width (int): the width of the image
        image_height (int): the height of the image

    Returns:
        Line: Containing the Line properties
    """
    line_vertices = []

    for _ in range(random_int_value(2, 4)):
        line_vertices.append((random_float_value(0, image_width), random_float_value(0, image_height)))

    color = random_color()
    draw_image.line(line_vertices, fill=color, width=int(percentage_of_value(0.8, image_width)))

    return Line(line_vertices, color)


def recreate_line(draw_image, image_width, line):
    """Recreate the line by given line_properties.

    Args:
        draw_image (DrawImage): the DrawImage the line should be created on
        line (Line): Line properties that should be used

    Returns:
        Line: Containing the Line properties
    """
    draw_image.line(line.vertices, line.color, width=int(percentage_of_value(0.8, image_width)))
    return Line(line.vertices, line.color)
