from Utility.utility import random_float_value, random_float_value_based_on_percentage, random_color, random_int_value
from ImageDataClasses.circle import Circle


def generate_circle(draw_image, image_width, image_height):
    """Create a circle with random values.

    Args:
        draw_image (DrawImage): the DrawImage the circle should be created on
        image_width (int): the width of the image
        image_height (int): the height of the image

    Returns:
        Circle: Containing the circle properties
    """
    circle_width = random_float_value_based_on_percentage(5, image_width, 30, image_width)
    circle_height = random_float_value_based_on_percentage(5, image_height, 30, image_height)
    circle_x = random_float_value(0, image_width) - (circle_width / 2)
    circle_y = random_float_value(0, image_height) - (circle_height / 2)

    # circle_shape = [(position),(shape properties)]
    circle_shape = [(circle_x, circle_y), (circle_x + circle_width, circle_y + circle_height)]

    # Create circle and fill or outline with given color
    color = random_color()
    is_filled = True
    line_width = int(random_float_value_based_on_percentage(0.5, image_width, 1, image_width))

    if(random_int_value(0, 100) <= 60):
        draw_image.ellipse(circle_shape, fill=color)
        is_filled = True
    else:
        draw_image.ellipse(circle_shape, outline=color,  width=line_width)
        is_filled = False

    return Circle(circle_width, circle_height, (circle_x, circle_y), color, line_width, is_filled)


def recreate_circle(draw_image, circle):
    """Recreate the circle by given circle_properties.

    Args:
        draw_image (DrawImage): the DrawImage the circle should be created on
        circle (Circle): Circle properties that should be used

    Returns:
        Circle: Containing the circle properties
    """
    x, y = circle.position
    # Circle_shape = [(location properties),(shape properties)]
    circle_shape = [circle.position, (x + circle.width, y + circle.height)]

    # Create circle and fill or outline with given color
    if(circle.is_filled == True):
        draw_image.ellipse(circle_shape, fill=circle.color)
    else:
        draw_image.ellipse(circle_shape, outline=circle.color, width=circle.line_width)

    return Circle(circle.width, circle.height, circle.position, circle.color, circle.line_width, circle.is_filled)
