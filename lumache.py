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

class UnexsistKindError(Exception):
    """Raised if the arg1 is unexsist."""

    pass


def select_menu(arg1:int, arg2:int):
    """
    Return the random menu as a int.

    :param arg1: first select number.
    :param arg2: second select number.
    :raise lumache.UnexsistKindError: If the arg1 is unexsist.
    :return: The final menu number.
    :rtype: int

    :example:
    >>> a=1
    >>> b=2
    >>> select_menu(a, b)
        3

    """
    return a + b


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

