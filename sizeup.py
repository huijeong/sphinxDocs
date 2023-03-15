"""
Sizeup - Python library for food fighter doggy. try it double x2!

This is a Python docstring, we can use reStructuredText syntax here!

.. code-block:: python

    # Import sizeup
    import sizeup


"""

__version__ = "0.1.1"



def size_up(food:str, size:str):
    """
    Return the random menu as a index number.

    :param str food: return a random food name as string.
    :param str size: choose the size between large, xlarge, 2xlarge.
    :return: return food name and that size.
    :rtype: str

    :example:
    >>> food = "chew stick"
    >>> size = "xlarge"
    >>> size_up(food, size)
        "chew stick xlarge"

    """
    return food + size




