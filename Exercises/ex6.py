def rsum(user_input):
    '''(list of list of int) -> int
    Returns the sum of all elements in a given list or nested list.
    REQ:
    len(user_input) >= 1
    '''
    length = len(user_input)
    if length == 0:
        result = 0
    elif length == 1:
        if isinstance(user_input[0], list):
            result = rsum(user_input[0])
        else:
            result = user_input[0]
    else:
        if isinstance(user_input[0], list):
            result = rsum(user_input[0]) + rsum(user_input[1:])
        else:
            result = user_input[0] + rsum(user_input[1:])
    return result


def rmax(user_input):
    '''(list of int) -> int
    return the maximum number in a given list
    REQ:
    len(user_input) >= 1
    '''
    if (user_input == []):
        return float('-inf')
    else:
        first = user_input[0]
        others = user_input[1:]
        if isinstance(first, int):
            large = first
        else:
            large = rmax(first)
        large_2 = rmax(others)

        if (large > large_2):
            result = large
        else:
            result = large_2
        return result


def second_smallest(user_input):
    '''(list of int) -> int
    return the second smallest number in a given list.
    REQ:
    len(user_input) >= 1
    '''
    (number1, number2) = small_large(user_input)
    result = number2
    return result


def small_large(user_input):
    '''(list of list of int) -> tuple
    return a tuple which has the minimum and the maximum numbers)
    '''
    if (user_input == []):
        return (float('inf'), float('inf'))

    first = user_input[0]
    others = user_input[1:]

    if (isinstance(first, int)):
        small = (first, float('inf'))
    else:
        small = small_large(first)

    small2 = small_large(others)

    if (small[0] < small2[0]):
        minimum = small[0]
        i = small[1]
        k = small2
    else:
        minimum = small2[0]
        i = small2[1]
        k = small
    if (i < k[0]):
        minimum_other = i
    else:
        minimum_other = k[0]
    return (minimum, minimum_other)


def sum_max_min(user_input):
    '''(list of int) -> int
    Return the sum of the maximum and minimum elements in a given list
    REQ:
    len(user_input) >= 1
    '''
    (largest, smallest) = sum_max_min_helper(user_input)
    result = largest + smallest
    return result


def sum_max_min_helper(user_input):
    '''(list of  list ints) -> tuple
    Return the largest and the smallest numbers in a given list
    '''
    if user_input == []:
        return(float("-inf"), float("inf"))
    else:
        first = user_input[0]
        others = user_input[1:]

        if isinstance(first, int):
            first_large = first
            first_small = first

        else:
            (first_large, first_small) = sum_max_min_helper(first)

        (others_large, others_small) = sum_max_min_helper(others)

        if (first_large > others_large):
            largest = first_large
        else:
            largest = others_large
        if(first_small < others_small):
            smallest = first_small
        else:
            smallest = others_small

        return (largest, smallest)