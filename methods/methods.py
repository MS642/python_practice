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


def has_33(num):
    """
    Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

    has_33([1, 3, 3]) → True
    has_33([1, 3, 1, 3]) → False
    has_33([3, 1, 3]) → False
    :param num: list
    :return: boolean

    """
    total = ''.join(str(n) for n in num)
    return "33" in total


assert has_33([1, 3, 3]) == True
assert has_33([1, 3, 1, 3]) == False
assert has_33([3, 1, 3]) == False


def paper_doll(name):
    """
    PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
    paper_doll('Hello') --> 'HHHeeellllllooo'
    paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
    :param name: string
    :return result: string
    """
    result = []
    for char in name:
        for i in range(3):
            result.append(char)
    return ''.join(result)


assert paper_doll('Hello') == 'HHHeeellllllooo'
assert paper_doll('Mississippi') == 'MMMiiissssssiiissssssiiippppppiii'


def blackjack(x, y, z):
    """
    BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
    If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally,
    if the sum (even after adjustment) exceeds 21, return 'BUST'
    blackjack(5,6,7) --> 18
    blackjack(9,9,9) --> 'BUST'
    blackjack(9,9,11) --> 19
    :param x: int between 1 and 11
    :param y: int between 1 and 11
    :param z: int between 1 and 11
    :return: return sum if less than 21 else 'BUST'
    """
    total = x + y + z
    return total if total <= 21 else total - 10 if x == 11 or y == 1 or z == 11 else 'BUST'


assert blackjack(5, 6, 7) == 18
assert blackjack(9, 9, 9) == 'BUST'
assert blackjack(9, 9, 11) == 19


def summer_69(arr):
    """
    SUMMER OF '69: Return the sum of the numbers in the array,
    except ignore sections of numbers starting with a 6 and
    extending to the next 9 (every 6 will be followed by at least one 9).
    Return 0 for no numbers.
    summer_69([1, 3, 5]) --> 9
    summer_69([4, 5, 6, 7, 8, 9]) --> 9
    summer_69([2, 1, 6, 9, 11]) --> 14
    :param arr: array of num
    :return sum: sum of numbs not between 69
    """
    total = 0
    found_6 = False
    for num in arr:
        if found_6:
            if num == 9:
                found_6 = False
            continue
        else:
            if num == 6:
                found_6 = True
                continue
            total += num
    return total


assert summer_69([1, 3, 5]) == 9
assert summer_69([4, 5, 6, 7, 8, 9]) == 9
assert summer_69([2, 1, 6, 9, 11]) == 14


def spy_game(nums):
    """
    SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
     spy_game([1,2,4,0,0,7,5]) --> True
     spy_game([1,0,2,4,0,5,7]) --> True
     spy_game([1,7,2,0,4,5,0]) --> False
    :param nums: array of int
    :return: boolean if received 007
    """
    zeros = 2
    for n in nums:
        if n == 0:
            zeros -= 1
        if n == 7 and zeros <= 0:
            return True
    return False


assert spy_game([1, 2, 4, 0, 0, 7, 5]) == True
assert spy_game([1, 0, 2, 4, 0, 5, 7]) == True
assert spy_game([1, 7, 2, 0, 4, 5, 0]) == False


def count_primes(num):
    """
    COUNT PRIMES: Write a function that
    returns the number of prime numbers that exist up to and including a given number
    count_primes(100) --> 25

    By convention, 0 and 1 are not prime.
    :param num: numb to count to
    :return: total number of primes that exists from 0 till and upto 100
    """
    counter = 0
    for n in range(2, num + 1):
        if is_prime(n):
            counter += 1
    return counter


def is_prime(n):
    """
    returns if the number given prime
    :param n: number given
    :return:
    """
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    return False


assert count_primes(100) == 25

big_letters = {'a': ['  *  ', ' * * ', '*****', '*   *', '*   *'],
               'b': ['***', '*  *', '***', '*  *', '***'],
               'c': ['  ***', ' *', '*', ' *', '  ***'],
               'd': ['**', '*  *', '*   *', '*  *', '**'],
               'e': ['*****', '*', '*****', '*', '*****']}


def print_big(letter):
    """
    PRINT BIG: Write a function that takes in a single letter, and
    returns a 5x5 representation of that letter in upper case
    print_big('a')

    out:   *
          * *
         *****
         *   *
         *   *
    HINT: Consider making a dictionary of possible patterns, and
    mapping the alphabet to specific 5-line combinations of patterns.
    For purposes of this exercise, it's ok if your dictionary stops at "E".
    :param letter: str
    """
    for char in big_letters[letter]:
        print(char)
    pass

# print_big('a')
# print_big('b')
# print_big('c')
# print_big('d')
# print_big('e')
