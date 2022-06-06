import random


def clamp(num, min_value, max_value):
    """"Clamp the given value

    Args:
        num (float): value to clamp
        min_value (float): minimum value
        max_value (float): maximum value

    Returns:
        [type]: [description]
    """
    return max(min(num, max_value), min_value)


def random_int_value(min, max):
    """Create random int value between min en max value.

    Args:
        min (int): minimum value
        max (int): maximum value

    Returns:
        int: random value
    """
    return random.randint(int(min), int(max))


def random_float_value(min, max):
    """Create random float value between min en max value.

    Args:
        min (float): minimum value
        max (float): maximum value

    Returns:
        float: random value rounded to 2 decimals
    """
    return round(random.uniform(min, max), 2)


def percentage_of_value(percentage, value):
    """Calculates and returns part of the given value based on the given percentage.

    Args:
        percentage (float): percentage of value you want to be calculated
        value (float): the value to be used

    Returns:
        float: part of given value based on given percentage
    """
    return percentage / 100 * value


def random_float_value_based_on_percentage(percentage1, value1, percentage2, value2):
    """Calculates random value of the given value based on the given percentage.

    Args:
        percentage1 (float): first value percentage
        value1 (float): value first percentage uses
        percentage2 (float): second value percentage
        value2 (float): value second percentage uses

    Returns:
        float: random value depending on percentages given
    """
    return random_float_value(percentage_of_value(percentage1, value1), percentage_of_value(percentage2, value2))


def random_color():
    """Return random color tuple, Example (255, 255, 255).

    Returns:
        tuple(int): random color
    """
    return (random_int_value(0, 255), random_int_value(0, 255), random_int_value(0, 255))
