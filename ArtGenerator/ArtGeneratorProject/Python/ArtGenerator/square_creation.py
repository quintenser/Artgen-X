from Utility.utility import random_float_value, random_float_value_based_on_percentage, random_color, random_int_value
from ImageDataClasses.square import Square


def generate_square(draw_image, image_width, image_height):
    """Create a square with random values.

    Args:
        draw_image (DrawImage): the DrawImage the square should be created on
        image_width (int): the width of the image
        image_height (int): the height of the image

    Returns:
        Square: Containing the square properties
    """
    square_width = random_float_value_based_on_percentage(5, image_width, 30, image_width)
    square_height = random_float_value_based_on_percentage(5, image_height, 30, image_height)
    position = (random_float_value(0, image_width) - (square_width / 2),
                random_float_value(0, image_height) - (square_height / 2))

    # square_shape = [(position),(shape properties)]
    rectangle_shape = [position, (position[0] + square_width, position[1] + square_height)]

    # Create square and fill or outline with given color
    color = random_color()
    is_filled = True
    line_width = int(random_float_value_based_on_percentage(0.5, image_width, 1, image_width))

    if(random_int_value(0, 100) <= 60):
        draw_image.rectangle(rectangle_shape, fill=color)
        is_filled = True
    else:
        draw_image.rectangle(rectangle_shape, outline=color,  width=line_width)
        is_filled = False

    return Square(square_width, square_height, position, color, line_width, is_filled)


def recreate_square(draw_image, square):
    """Recreate the circle by given square_properties.

    Args:
        draw_image (DrawImage): the DrawImage the circle should be created on
        circle (Circle): Circle properties that should be used

    Returns:
        Circle: Containing the circle properties
    """
    # Square_shape = [(location properties),(shape properties)]
    x, y = square.position
    rectangle_shape = [square.position, (x + square.width, y + square.height)]

    # recreate the square and fill or outline with given color
    if(random_int_value(0, 100) <= 60):
        draw_image.rectangle(rectangle_shape, fill=square.color)
        is_filled = True
    else:
        draw_image.rectangle(rectangle_shape, outline=square.color,  width=square.line_width)
        is_filled = False

    return Square(square.width, square.height, square.position, square.color, square.line_width, square.is_filled)
