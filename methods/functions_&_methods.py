import math
import string


def vol(radius):
    """
    Write a function that computes the volume of a sphere given its radius.
    :param radius: int
    :return: int
    """
    volume = (4/3) * math.pi * (radius ** 3)
    return volume


assert vol(2) == 33.510321638291124


def is_palindrome(s):
    """
    Write a Python function that checks whether a word or phrase is palindrome or not.

    Note: A palindrome is word, phrase, or sequence that reads the same backward as forward,
     e.g., madam,kayak,racecar, or a phrase "nurses run". Hint: You may want to check out
     the .replace() method in a string to help out with dealing with spaces.
     Also google search how to reverse a string in Python, there are some clever ways to do it with slicing notation.
    :param s:
    :return:
    """
    length = len(s)
    for i in range(length//2):
        if s[i] != s[length-i - 1]:
            return False
    return True


assert is_palindrome('catac') == True
assert is_palindrome('cat') == False
assert is_palindrome('racecar') == True
assert is_palindrome('madam') == True


def is_panagram(str, alphabet=string.ascii_lowercase):
    """
    # Assumption alphabet if passed then will have unique values
    Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)
    Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
    For example : "The quick brown fox jumps over the lazy dog"
    :param str:
    :param alphabet:
    :return:
    """
    str_set = set(x.lower() for x in str)
    alpha_list = list(x.lower() for x in alphabet)
    for c in str_set:
        for i in range(len(alpha_list)):
            if c == alpha_list[i]:
                alpha_list.pop(i)
                break

    return len(alpha_list) == 0


assert is_panagram("The quick brown fox jumps over the lazy dog") == True
assert is_panagram("The quick brown fox jumps over the dog") == False