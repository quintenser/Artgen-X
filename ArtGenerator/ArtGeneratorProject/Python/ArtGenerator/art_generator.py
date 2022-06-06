from PIL import Image, ImageDraw
from Resources import config
from copy import copy
from fileManager import FileManager
from Algorithm.evolutionary_algorithm import create_offspring, add_parent, reset_algorithm
from Utility.utility import random_color
from ArtGenerator.circle_creation import generate_circle, recreate_circle
from ArtGenerator.line_creation import generate_line, recreate_line
from ArtGenerator.square_creation import generate_square, recreate_square
from ArtGenerator.triangle_creation import generate_triangle, recreate_triangle
import ImageDataClasses.image

config = FileManager.readDefaultConfig()
image_id = 0
generation = 0
generations_until_algorithm_is_used = config.generations_until_algorithm_is_used
last_generated_images = {}


def generate_art():
    """Starts the art generation process depending on the current generation.

    Args:
        id (int): the id of the chosen image

    Returns:
        Image: Containing the image and the image generation id
    """

    if (generation <= generations_until_algorithm_is_used):
        return generate_random_art()
    else:
        return generate_art_based_on_parents()


def generate_random_art():
    """Generate art with default values given by C# frontend.

    Returns:
        Image: Containing the image and the image generation id
    """
    config = FileManager.readDefaultConfig()

    image_width = config.imageWidth
    image_height = config.imageHeight

    color = random_color()
    image = Image.new("RGB", (image_width, image_height), color)

    # Create a empty Image class to save the created image properties in.
    image_config = ImageDataClasses.image.Image(image_width, image_height, color, [], [], [], [])

    draw_image = ImageDraw.Draw(image)

    # Draw lines on the image and save the created line properties in the image properties.
    for _ in range(config.lineAmount):
        image_config.lines.append(generate_line(draw_image, image_width, image_height))

    # Draw squares on the image and save the created square properties in the image properties.
    for _ in range(config.squareAmount):
        image_config.squares.append(generate_square(draw_image, image_width, image_height))

    # Draw circles on the image and save the created circle properties in the image properties.
    for _ in range(config.circleAmount):
        image_config.circles.append(generate_circle(draw_image, image_width, image_height))

    # Draw triangles on the image and save the created triangle properties in the image properties.
    for _ in range(config.triangleAmount):
        image_config.triangles.append(generate_triangle(draw_image, image_width, image_height))

    image_id = increment_image_id()

    # Write the created image properties to a json file.
    add_image_to_generated_images_list(image_id, image_config)

    # Line below can be used to create a json file with image properties if needed
    # FileManager.writeJsonFile(f"id_{image_id}_starting_image", image_config.json())
    return (image, image_id)


def generate_art_based_on_parents():
    """Generate art based on liked parents.

    Args:
        id (int): the id of the given image

    Returns:
        Image: Containing the image and the image generation id
    """
    image_properties = create_offspring()

    image_width = image_properties.imageWidth
    image_height = image_properties.imageHeight

    background_color = image_properties.background_color
    image = Image.new("RGB", (image_width, image_height), background_color)

    # Create a empty Image class to save the created image properties in.
    image_config = ImageDataClasses.image.Image(image_width, image_height, background_color, [], [], [], [])

    draw_image = ImageDraw.Draw(image)
    # Draw lines on the image and save the created line properties in the image properties.
    for line in image_properties.lines:
        image_config.lines.append(recreate_line(draw_image, image_width, line))

    # Draw squares on the image and save the created square properties in the image properties.
    for square in image_properties.squares:
        image_config.squares.append(recreate_square(draw_image, square))

    # Draw circles on the image and save the created circle properties in the image properties.
    for circle in image_properties.circles:
        image_config.circles.append(recreate_circle(draw_image, circle))

    # Draw triangles on the image and save the created triangle properties in the image properties.
    for triangle in image_properties.triangles:
        image_config.triangles.append(recreate_triangle(draw_image, triangle))

    image_id = increment_image_id()

    add_image_to_generated_images_list(image_id, image_config)

    # Line below can be used to create a json file with image properties if needed
    # FileManager.writeJsonFile(f"id_{image_id}_starting_image", image_config.json())
    return (image, image_id)


def add_image_to_generated_images_list(id, image):
    """Add the created image to the temporary image list so it can be moved to the parents list when liked.

    Args:
        id (int): id of the image
        image (Image): Image properties
    """
    global last_generated_images
    last_generated_images[id] = image


def add_image_to_parents(id):
    """Add the liked image to parents list.

    Args:
        id (int): id of the image
    """
    global last_generated_images
    image = last_generated_images[id]
    add_parent(image)
    increment_generation()

    return copy(image), generation


def increment_image_id():
    """Increment the image id.

    Returns:
        int: the current id that should be used
    """
    global image_id
    image_id += 1
    return image_id


def increment_generation():
    """Increment the image generation number.

    Returns:
        int: the current generation the generator is on
    """
    global generation
    generation += 1
    return generation


def reset_generation():
    """Reset current generation to 0 and reset algorithm.

    Returns:
        bool: was reset was successfull
    """
    global generation
    global image_id
    global last_generated_images
    generation = 0
    last_generated_images = {}
    image_id = 0
    reset_algorithm()
    return True
