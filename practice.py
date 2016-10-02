"""
Skills function assessment.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE:

    >>> hello_world()
    Hello World

    >>> say_hi("Balloonicorn")
    Hi Balloonicorn

    >>> print_product(3, 5)
    15

    >>> repeat_string("Balloonicorn", 3)
    BalloonicornBalloonicornBalloonicorn

    >>> print_sign(3)
    Higher than 0

    >>> print_sign(0)
    Zero

    >>> print_sign(-3)
    Lower than 0

    >>> is_divisible_by_three(12)
    True

    >>> is_divisible_by_three(10)
    False

    >>> num_spaces("Balloonicorn is awesome!")
    2

    >>> total_meal_price(30)
    34.5

    >>> total_meal_price(30, .3)
    39.0

    >>> sign_and_parity(3)
    ['Odd', 'Positive']

    >>> sign_and_parity(-2)
    ['Even', 'Negative']

PART TWO:

    >>> full_title("Balloonicorn")
    'Engineer Balloonicorn'

    >>> full_title("Jane Hacks", "Hacker")
    'Hacker Jane Hacks'

    >>> write_letter("Jane Hacks", "Hacker", "Balloonicorn")
    Dear Hacker Jane Hacks, I think you are amazing! Sincerely, Balloonicorn

"""
################################################################################

# PART ONE

# 1. Write a function called 'hello_world' that does not take any arguments and
#    prints "Hello World".

def hello_world():
    """Prints 'hello world'"""

    print "Hello World"


# 2. Write a function called 'say_hi' that takes a name as a string and
#    prints "Hi" followed by the name.

def say_hi(name):
    """Prints 'Hi [name]'"""

    print "Hi {}".format(name)


# 3. Write a function called 'print_product' that takes two integers and multiplies
#    them together. Print the result.

def print_product(integer1, integer2):
    """Takes two integers and multiplies them together"""

    print integer1 * integer2


# 4. Write a function called 'repeat_string' that takes a string and an integer and
#    prints the string that many times

def repeat_string(string, n):
    """Prints string n number of times"""

    print string * n


# 5. Write a function called 'print_sign' that takes an integer and prints "Higher
#    than 0" if higher than zero and "Lower than 0" if lower
#    than zero. If the integer is 0 print "Zero".

def print_sign(integer):
    """Determines whether an integer is greater than, less than, or equal to zero"""

    if integer > 0:
        print "Higher than 0"

    elif integer < 0:
        print "Lower than 0"

    elif integer == 0:
        print "Zero"

    else:
        print "Not a valid integer"



# 6. Write a function called 'is_divisible_by_three' that takes an integer and returns a
#    boolean (True or False), depending on whether the number
#    is evenly divisible by 3.

def is_divisible_by_three(integer):
    """Takes an integer and returns a boolean based on whether the number is divisble by three"""

    if integer % 3 == 0:
        return True
    else:
        return False

# 7. Write a function called 'num_spaces' that takes a sentence as one string and
#    returns the number of spaces.

def num_spaces(sentence):
    """Takes a sentence as a string and returns the number of spaces"""




# 8. Write a function called 'total_meal_price' that can be passed a meal price and a
#    tip percentage. It should return the total amount paid
#    (price + price * tip). **However:** passing in the tip
#    percentage should be optional; if not given, it should
#    default to 15%.

def total_meal_price(meal_price, tip = 0.15):
    """Takes a meal price and a tip percentage and returns the total meal price (plus tip)"""

    total_meal_price = meal_price + meal_price * tip
    return total_meal_price


# 9. Write a function called 'sign_and_parity' that takes an integer as an argument and
#    returns two pieces of information as strings ---
#    "Positive" or "Negative" and "Even" or "Odd". The two strings
#    should be returned in a list.
#
#    Then, write code that shows the calling of this function
#    on a number and unpack what is returned into two
#    variables --- sign and parity (whether it's even or odd).
#    Print sign and parity

def sign_and_parity(integer):
    """Returns a list that contains two items: (1) Even or Odd and (2) Positive or Negative"""
    if integer > 0:
        sign = ["Positive"]
    elif integer < 0:
        sign = ["Negative"]

    if integer % 2 == 0:
        parity = ["Even"]
    elif integer % 2 == 1:
        parity = ["Odd"]

    sign_and_parity_list = parity + sign
    return sign_and_parity_list

number_sign_and_parity = sign_and_parity(3)
number_parity, number_sign = number_sign_and_parity

print number_parity
print number_sign



################################################################################
# PART TWO

# 1. Turn the block of code from the directions into a function.
#    Take a name and a job title as parameters, making it so the
#    job title defaults to "Engineer" if a job title is not passed in.
#    Return the person's title and name in one string.

# 2. Given a recipient name & job title and a sender name,
#    print the following letter:
#
#       Dear JOB_TITLE RECIPIENT_NAME, I think you are amazing!
#       Sincerely, SENDER_NAME.
#
#    Use the function from #1 to construct the full title for the letter's
#    greeting.

def full_title(name, job_title = "Engineer"):
    """Takes a job title and name and returns both as a single string"""

    return job_title + " " + name

    
def write_letter(contact_info, sender_name):
    """Prints a letter with the format:

       Dear JOB_TITLE RECIPIENT_NAME, I think you are amazing!
       Sincerely, SENDER_NAME.
    """
    print "Dear {}, I think you are amazing!".format(contact_info)
    print "Sincerely, {}".format(sender_name)

contact_info = full_title("Karen", "Teacher")
write_letter(contact_info, "Jill")



#####################################################################
# END OF PRACTICE: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
