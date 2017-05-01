from container import *
# raise a ContainerFullException error


class ContainerFullException(Exception):
    ''' raises container Full error if the container is full'''
# raise a ContainerEmptyException error


class ContainerEmptyException(Exception):
    ''' raises container Empty error if the container is empty'''


def banana_verify(source, goal, cont, moves):
    '''(str,str,container,list of str) -> bool
    check whether we can get the goal word with the source word using the given
    methods.
    '''

    try:
        result = ""
        source = []
        # loop through the moves to determine whether it is Put, Get or Move.
        for element in moves:
            # if the move is Put,
            if element == 'P':
                # add the letter to the result
                cont.put(source.pop(0))
            # if the move is get
            elif element == 'G':
                # use the get method
                result += cont.get()
            # if the move is Move
            elif element == "M":
                result += source.pop(0)
        # if the result str is the goal word;
        if result == goal:
            # set it as True
            banana = True
        else:
            # set it as False
            banana = False
    # if the container is empty, raise a ContainerEmptyException and set
    # it as False
    except ContainerEmptyException:
        banana = False
    # if the container is full, raise a ContainerEmptyException and set it
    # as False
    except ContainerFullException:
        banana = False
    # return the result
    return banana

