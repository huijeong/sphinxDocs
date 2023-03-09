"""
Lumache - Python library for cooks and food lover doggy.

This is a Python docstring, we can use reStructuredText syntax here!
I'm lumache.py file. append the api in this file.

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
    """Raised if the kind is Unexsist."""

    pass

def select_menu(kind=None):
    """
    Return the random menu as a string.

    :param kind: Optional "organic" of menu.
    :type kind: str or None
    :raise lumache.UnexsistKindError: If the kind is unexsist.
    :return: The menu name.
    :rtype: str
    """
    return "puppuccino"


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

