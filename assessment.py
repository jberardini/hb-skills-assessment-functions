# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5% 

def calculate_cost_plus_tax(state_abbrev, item_cost, tax = 0.05):
    "Takes a state abbreviation, item cost, and state tax amount to calculate total item cost"""

    if state_abbrev == "CA":
        total_cost = item_cost + item_cost * 0.07
        return total_cost
    else:
        total_cost = item_cost + item_cost * tax
        return total_cost

#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or 
#        "blackberry".

#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function 
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.

def is_berry(fruit):
    """Takes a fruit name as a string and returns True if strawberry, cherry, or blackberry"""

    if fruit == "strawberry" or fruit == "cherry" or fruit == "blackberry":
        return True
    else:
        return False

def shipping_cost(fruit):
    """Calculates shipping cost based on fruit name"""

    if is_berry(fruit) == True:
        shipping_cost = 0
    elif is_berry(fruit) == False:
        shipping_cost = 5

    return shipping_cost

#2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.
#
#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.(
#
#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you 
#        from?" depending on what `is_hometown()` evaluates to.

def is_hometown(town_name):
    """Takes town name as a string and evaluates to true if Yorktown and false otherwise"""

    if town_name == "Yorktown":
        return True
    else:
        return False

def full_name(first_name, last_name):
    """Takes strings of first name and last name and returns a concatenated string with first and last name"""

    full_name = first_name + " " + last_name
    return full_name

def hometown_greeting(town_name, first_name, last_name):
    """Takes a home town, first name, and last name and prints greeting message """

    name = full_name(first_name, last_name)

    if is_hometown(town_name) == True:
        print "Hi {}, we're from the same place!".format(name)
    elif is_hometown(town_name) == False:
        print "Hi {}, where are you from?".format(name)

#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()`` 
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.

# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call 
#    addfive with y = 5. Call again with y = 20.

# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.

#####################################################################