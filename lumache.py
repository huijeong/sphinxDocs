"""
Lumache - Python library for cooks and food lover doggy.

This is a Python docstring, we can use reStructuredText syntax here!

.. code-block:: python

    # Import lumache
    import lumache

    # Call the function to choose the menu
    select_menu(kind="organic")

    # Call next function to cook
    get_random_ingredients(kind=["cheeses"])
"""

__version__ = "0.1.0"


class InvalidKindError(Exception):
    """Raised if the kind is invalid."""

    pass

class UnexsistTypeError(Exception):
    """Raised if the parameter is not Integer."""

    pass


def select_menu(arg1:int, arg2:int):
    """
    Return the random menu as a index number.

    :param arg1: first select number.
    :param arg2: second select number.
    :raise lumache.UnexsistTypeError: If the parameter is not Integer.
    :return: The final menu's index number.
    :rtype: int

    :example:
    >>> a=1
    >>> b=2
    >>> select_menu(a, b)
        3

    """
    return arg1 + arg2


def get_random_ingredients(kind=None):
    """
    Return a list of random ingredients as strings.

    :param kind: Optional "kind" of ingredients.
    :type kind: list[str] or None
    :raise lumache.InvalidKindError: If the kind is invalid.
    :return: The ingredients list.
    :rtype: list[str]
    """
    return ["shells", "gorgonzola", "parsley"]

