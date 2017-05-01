def greeting(name):
    ''' (str) -> str
    Returns a greeting message with the given name
    '''
    # create a message
    return 'Hello' + " " + name + " " + 'how are you today?'


def mutate_list(my_list):
    ''' (list) -> list
    If the element is an integer, multiply by 2. If the element is a bool,
    get the opposite. If the element is a string, remove the first and last
    letters. Set the 0th element as 'Hello'. The function shouldn't return
    anyting.
    Req: my_list must have at least 1 element
    Req: All strings will have at least 2 characters in them.
    '''
    my_list[0] = "Hello"
    # if the element is an integer
    for element in range(1, len(my_list)):
        # if the element is a string
        if isinstance(my_list[element], str):
            # remove the first and the last letters
            my_list[element] = my_list[element][1:-1]
        elif isinstance(my_list[element], int):
            # multiply by 2
            my_list[element] = my_list[element] * 2
        # if the element is a bool
        elif isinstance(my_list[element], bool):
            # return the opposite
            my_list[element] = not element


def merge_dicts(dict1, dict2):
    ''' ({str: list of ints}, {str: list of ints}) -> {str: list of ints}
    Returns a new dictionary with all key:value pairs from both dictionaries.
    '''
    # create an empty dict
    dict3 = dict()
    # loop through the dict1
    for key in dict1:
        # append the values if the keys are the same
        if key in dict2:
            dict3[key] = dict1[key] + dict2[key]
        else:
            dict3[key] = dict1[key]
    # loop through dict 2
    for i in dict2:
        if i not in dict1:
            dict3[i] = dict2[i]
    return dict3
