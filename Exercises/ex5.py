def rsum(user_input):
    '''(list of int) -> int
    Returns the sum of all elements in a given list.
    REQ:
    len(user_input) >= 1
    '''
    length = len(user_input)
    if length == 0:
        result = 0
    elif length == 1:
        result = user_input[0]
    else:
        result = rsum(user_input[1:]) + user_input[0]
    return result


def rmax(user_input):
    '''(list of int) -> int
    return the maximum number in a given list
    REQ:
    len(user_input) >= 1
    '''
    if len user_input == 1:
        result = user_input[0]
    else:
        number = rmax(user_input[1:])
        if number > user_input[0]:
            result = number
        else:
            result = user_input[0]
    return result


def second_smallest(user_input):
    '''(list of int) -> int
    return the second smallest number in a given list.
    REQ:
    len(user_input) >= 1
    '''
    if (len(user_input)) == 2 and user_input[0] <= user_input[1]:
        result = user_input[1]
    elif user_input[-1] >= user_input[0] and user_input[-1] >= user_input[1]:
        result = second_smallest(user_input[:-1])
    else:
        result = second_smallest([user_input[-1]] + user_input[:-1])
    return result


def minimum(user_input):
    '''(list of int) -> int
    return the minimum number in a given list.
    REQ:
    len(user_input) >= 1
    '''
    if len(user_input) == 1:
            result = user_input[0]
    else:
        number = minimum(user_input[1:])
        if number < user_input[0]:
            result = number
        else:
            result = user_input[0]
    return result


def sum_max_min(user_input):
    '''(list of int) -> int
    Return the sum of the maximum and minimum elements in a given list
    REQ:
    len(user_input) >= 1
    '''
    result = rmax(user_input) + minimum(user_input)
    return result
