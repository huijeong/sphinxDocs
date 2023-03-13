Usage
=====

.. _installation:

installation
------------

To use Hodu to make pet food, first install it using pip:

.. code-block:: console

   (.venv) $ pip install lumache


Get menu
---------
If you want to get the menu list for your wonderful dinner,
run this command line:

.. code-block:: console
   $ hodu get-menu-list



Now you can see the all menu lists for doggy!



Select menu
-------------
You can choose any menu for your dinner. we can provide any recipes as you want!
just select by use ``lumache.select_menu`` function:

.. autofunction:: lumache.select_menu

The ``organic`` parameter should be either ``"puppuccino"``, ``"chewstick"``,
or ``"jelly"``. Otherwise, :py:func:`lumache.select_menu`
will raise an exception

.. autoexception:: lumache.UnexsistKindError

For example:

>>> import lumache
>>> lumache.select_menu()
'puppuccino'


next step is create the recipies for this menu.


Creating recipes
-----------------

To retrieve a list of random ingredients,
you can use the ``lumache.get_random_ingredients()`` function:

.. autofunction:: lumache.get_random_ingredients

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. autoexception:: lumache.InvalidKindError

For example:

>>> import lumache
>>> lumache.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']

