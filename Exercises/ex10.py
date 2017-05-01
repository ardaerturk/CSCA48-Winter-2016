from container import *


def rec_helper(s1, s2, c):
    if c.is_empty() is False and c.peek() == s2[0]:
        c.get()
        result = rec_helper(s1, s2[1:], c)
    elif len(s1) == 0:
        if c.is_empty() is False and c.peek() != s2[0]:
            result = False
        else:
            result = True
    elif s1[0] == s2[0]:
        result = rec_helper(s1[1:], s2[1:], c)
    elif len(s1) > 0:
        c.put(s1[0])
        result = rec_helper(s1[1:], s2, c)
    return result


def banana_game(s1, s2, c):
    length = len(s1)
    index = 0
    while s1[index] != s2[0]:
        c.put(s1[index])
        index = index + 1
    if length == len(s2):
        result = rec_helper(s1[index:], s2, c)
    else:
        result = False
    return result
