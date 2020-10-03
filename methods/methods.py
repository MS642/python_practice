"""
    Practice questions and solution added to the functions with asserts to verify
"""


def lesser_of_two_evens(a, b):
    """
    # LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even,
    # but returns the greater if one or both numbers are odd

    :param a: int
    :param b: int
    :return: boolean
    """
    if a % 2 == 0 and b % 2 == 0:
        return a if a < b else b
    else:
        return a if a > b else b


assert lesser_of_two_evens(2,4) == 2

assert lesser_of_two_evens(2,5) == 5


def animal_crackers(text):
    """
    ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
    :param text: string
    :return: boolean
    """
    first = text[0]
    last = text.split()[1][0]
    return first == last


# Check
assert animal_crackers('Levelheaded Llama') == True
# Check
assert animal_crackers('Crazy Kangaroo') == False


def makes_twenty(n1, n2):
    """
        MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of
        the integers is 20. If not, return False
        makes_twenty(20,10) --> True
        makes_twenty(12,8) --> True
        makes_twenty(2,3) --> False
    """
    return n1 == 20 or n2 == 20 or n1+n2 == 20


# Check
assert makes_twenty(20, 10) == True
# Check
assert makes_twenty(2, 3) == False


def old_macdonald(name):
    """
        OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
        old_macdonald('macdonald') --> MacDonald

        Note: 'macdonald'.capitalize() returns 'Macdonald'
    """

    result = []
    result[:0] = name
    result[0] = name[0].upper()
    result[3] = name[3].upper()
    return ''.join(result)


# Check
assert old_macdonald('macdonald') == 'MacDonald'


def master_yoda(sent):
    """
    MASTER YODA: Given a sentence, return a sentence with the words reversed
    master_yoda('I am home') --> 'home am I'
    master_yoda('We are ready') --> 'ready are We'
    """
    result = []
    result[:-1] = sent.split()
    return ' '.join(reversed(result))


assert master_yoda('I am home') == 'home am I'

assert master_yoda('We are ready') == 'ready are We'


def almost_there(num):
    """
    ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200¶
    almost_there(90) --> True
    almost_there(104) --> True
    almost_there(150) --> False
    almost_there(209) --> True

    NOTE: abs(num) returns the absolute value of a number

    """
    return abs(100 - num) <= 10 or abs(200 - num) <= 10


assert almost_there(90) == True
assert almost_there(104) == True
assert almost_there(150) == False
assert almost_there(209) == True
