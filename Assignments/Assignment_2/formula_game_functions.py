"""
# Copyright Arda Erturk 2017 and Nick Cheng 2016
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 2, CSCA48, Winter 2017
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
"""

# Do not change this import statement, or add any of your own!
from formula_tree import FormulaTree, Leaf, NotTree, AndTree, OrTree

# Do not change any of the class declarations above this comment

# Add your functions here.


def build_tree(formula):
    '''(str) -> FormulaTree
    given a string formula, return the FormulaTree representation of the
    formula if it is a valid formula. Otherwise return None. *, +, - represent
    AND OR NOT respectively. A node that represents * or + has 2 child nodes,
    which in turn represent the two subformulas that are ANDed or ORed to
    form the larger formula. A node that represents - has one child node,
    which in turn represents the formula that is NOTed.
    REQ:
    - formula is not empty
    - the variables in the formula must be lower case
    - the representation of the formula must contain enough paranthesis(except
    for '-'
    >>> build_tree('X')
    None
    >>> build_tree('x*y')
    None
    >>> build_tree('-(x)')
    None
    >>> build_tree('(x+(y)*z)')
    None
    >>> build_tree('((-x+y)*-(-y+x))')
    AndTree(OrTree(NotTree(Leaf('x')), Leaf('y')),
                             NotTree(OrTree(NotTree(Leaf('y')), Leaf('x'))))
    >>> build_tree('(x*y)')
    AndTree(Leaf('x'), Leaf('y'))
    >>> build_tree('-y')
    Leaf('y')
    >>> build_tree('x')
    Leaf('x')
    >>> build_tree('v')
    Leaf('v')
    >>>build_tree('((x+y)*(z+-k))')
    AndTree(OrTree(Leaf('x'), Leaf('y')), OrTree(Leaf('z'),
                                                        NotTree(Leaf('k'))))
    '''
    try:
        # set the upper case checker as False
        upper = False
        # create lists
        tokenlist = []
        var = []

        # loop through the formula do determine the symbols
        for element in formula:
            # if the formula does not contain a paranthesis:
            if '(' not in formula:
                return None
            # if the element is '-'
            elif element == "-":
                # append the character to the list
                tokenlist.append(element)
            # if the element is '+'
            elif element == "+":
                # append the character to the list
                tokenlist.append(element)
            # if the element is '('
            elif element == "(":
                # append the character to the list
                tokenlist.append(element)
            # if the element is '*'
            elif element == "*":
                # append the character to the list
                tokenlist.append(element)
            # if the element is ')'
            elif element == ")":
                # remove and return the last object from the list and set it
                # as a new variable
                token = tokenlist.pop()
                # loop through that variable
                while token != '(':
                    # if the object is -
                    if token == "-":
                        # set the object as a variable, return the last object
                        # from the list to determine the character
                        var_formula = var.pop()
                        # append it to the list by using NotTree since the
                        # object has '-'
                        var.append(NotTree(var_formula))
                        token = tokenlist.pop()
                    # if the object is *
                    elif token == "*":
                        # set the left side of the *
                        var_formula = var.pop()
                        # now set the right side of the *
                        var_2 = var.pop()
                        # append it to the list by using And Tree class, since
                        # the symbol is '*'
                        var.append(AndTree(var_2, var_formula))
                        # remove and return the last item from the list
                        token = tokenlist.pop()
                    # if the object is '+'
                    elif token == "+":
                        # if the last item is '-'
                        if tokenlist[-1] == "-" and tokenlist[-1] is not None:
                            # set the left side of the '+'
                            var_formula = var.pop()
                            # set the right side of the '+'
                            var_2 = var.pop()
                            # since the object is '-', set it as NotTree
                            var_2 = NotTree(var_2)
                            # append it to the list by using OrTree class
                            var.append(OrTree(var_2, var_formula))
                            # pop the object twice/ remove and return the last
                            # item do it twice because of the '-' symbol
                            token = tokenlist.pop()
                            token = tokenlist.pop()
                        # otherwise
                        else:
                            # set the left side
                            var_formula = var.pop()
                            # set the right side
                            var_2 = var.pop()
                            # append it to the list by using OrTree class
                            var.append(OrTree(var_2, var_formula))
                            # remove and return the last object in the list
                            token = tokenlist.pop()

            # if the element is a alphabetical character,
            elif element.isalpha() is True:
                # if the character is lower,
                if element.islower() is True:
                    # then append to the list as 'Leaf'
                    var.append(Leaf(element))
                # otherwise return None
                else:
                    upper = True
                    return None
            # if the character is ')'
            elif element == ")":
                # remove and return the last object from token list and set it
                # as a variable
                token = tokenlist.pop()
                # loop through the list
                while token != '(':
                    # if the object is '-'
                    if token == "-":
                        # remove and return the last object, that is next to
                        # the '-' sign.
                        var_formula = var.pop()
                        # append the charachter as a NotTree because of the
                        # '-' sign
                        var.append(NotTree(var_formula))
                        #  set a new variable that is the last object
                        # from the list
                        token = tokenlist.pop()
                    # if the object is '*'
                    elif token == "*":
                        # remove and return the last object, the right side of
                        # the '*'
                        var_formula = var.pop()
                        # now the left side of the '*' sign.
                        var_2 = var.pop()
                        # append the left side and right side by using AndTree
                        # class
                        var.append(AndTree(var_2, var_formula))
                        token = tokenlist.pop()

                    # if the object is '+'
                    elif token == "+":
                        # if the last item is not none and '-' in the list,
                        if tokenlist[-1] is not None and tokenlist[-1] == "-":
                            # remove and return the last object, the right side
                            # of the '+'
                            var_formula = var.pop()
                            # now do the same process for the left side
                            var_2 = var.pop()
                            # since the item is '-', we need to assign it as
                            # NotTree
                            var_2 = NotTree(var_2)
                            # append the left side and right side by using
                            # OrTree class
                            var.append(OrTree(var_2, var_formula))
                            # pop the item twice/ remove and return the last
                            # item do it twice because of the '-' symbol
                            token = tokenlist.pop()
                            token = tokenlist.pop()
                        # otherwise
                        else:
                            # set the right side of the Or Tree
                            var_formula = var.pop()
                            # set the left side of the Or Tree
                            var_2 = var.pop()
                            # append the left side and right side by using
                            # OrTree
                            var.append(OrTree(var_2, var_formula))
                            # remove and return the last item in the list
                            token = tokenlist.pop()

        # return the first item in the list
        return var[0]
    except IndexError:
        return None


def draw_formula_tree_helper_function(root, draw_tree_str, height):
    '''(FormulaTree, str, int) -> str
    Helper function for build_tree returns a string that is the drawing
    representation of the tree.
    REQ:
    - formula is not empty
    - formula must be valid
    >>> draw_formula_tree(build_tree('((a+b)*c)'))
    '* c\n  + b\n    a'
    >>> draw_formula_tree(build_tree('x'))
    'x'
    >>> draw_formula_tree(build_tree('((x+y)*(z+-k))'))
    '* + - k\n    z\n  + y\n    x'
    >>> draw_formula_tree(build_tree('((-x+y)*-(-y+x))'))
    '* - + x\n      - y\n  + y\n    - x'
    '''

    # indent if the object in the new line
    if draw_tree_str[len(draw_tree_str)-1:] == '\n':

        # loop through the height
        for element in range(height):
            # now indent spaces
            draw_tree_str += '  '

    # now add the symbol of the object to the string
    draw_tree_str += root.symbol

    # we need to indent after symbols. Check whether the object is as symbol
    if root.symbol == '-' or root.symbol == '*' or root.symbol == '+':
        # indent space
        draw_tree_str += ' '

    # otherwise
    else:
        # add newline for the other objects
        draw_tree_str += '\n'

    # if there are still childs remaining
    if root.children != []:
        # loop through the childs
        for elements in root.children[::-1]:
            # recursive call. increase the height by one at each recursive call
            draw_tree_str = draw_formula_tree_helper_function(elements,
                                                              draw_tree_str,
                                                              height+1)
    # return result
    return draw_tree_str


def draw_formula_tree(root):
    '''(FormulaTree) -> str
    Returns the tree representation. Rotate the tree 90 degrees clockwise to
    see it with its root at the top.(without lines or arrows between parent
    and child nodes). Children of the root are indented 2 spaces.
    Children of a child of the root are indented 4 spaces.
    REQ:
    - formula is not empty
    - formula must be valid
    >>> draw_formula_tree(build_tree('((a+b)*c)'))
    '* c\n  + b\n    a'
    >>> draw_formula_tree(build_tree('x'))
    'x'
    >>> draw_formula_tree(build_tree('((x+y)*(z+-k))'))
    '* + - k\n    z\n  + y\n    x'
    >>> draw_formula_tree(build_tree('((-x+y)*-(-y+x))'))
    '* - + x\n      - y\n  + y\n    - x'
    '''
    # start the height with 0
    height = 0

    # create an empty string
    draw_tree_str = ""

    # now recursive call. Use the helper function to draw the tree
    final_draw_tree = draw_formula_tree_helper_function(root, draw_tree_str,
                                                        height)
    # we need to delete the /n at the end of the final string.
    return final_draw_tree[:-1]


def evaluate(root, variables, values):
    '''(FormulaTree, str, str) -> bool
    Returns whether the formula is true(1) or not(0). For a formula consisting
    of just one variable, the truth value of the formula is the truth value of
    the variable. (F1 * F2) is the minimum of the truth values of F1 and F2.
    Truth value of (F1 + F2) is the maximum of the truth values of F1 and F2.
    Truth value of -F1 is one minus the truth value of F1.
    REQ:
    - formula must be valid
    - formula is not empty
    - values must be either 1 or 0
    >>> evaluate(build_tree('(-a+b)*-(c+d)'), 'abcd', '1010')
    0
    >>> evaluate(build_tree('(-a+b)*-(c+d)'), 'abcd', '1111')
    1
    >>> evaluate(build_tree('((x+y)*((y+z)*(-y+-z)))'), 'xyz', '1100')
    1
    >>> evaluate(build_tree('((x+y)*((y+z)*(-y+-z)))'), 'xyz', '1000')
    0
    '''
    # create a new dictionary
    truth_dict = {}

    # loop through in range of variables that is given.
    for element in range(0, len(variables)):
        truth_dict[variables[element]] = values[element]

    # if the charachter is an alphabetical character, then
    if root.symbol.isalpha() is True:
        # take the integer value, 1 for true, 0 for false.
        result = int(truth_dict[root.symbol])

    # if the symbol is *
    elif root.symbol == '*':
        # the truth value is the minimum of the truth value of the first one
        # and the second one
        result = min(evaluate(root.children[0], variables, values),
                     evaluate(root.children[1], variables, values))

    # if  the symbol is -
    elif root.symbol == '-':
        # truth value is one minus the truth value of itself
        result = 1 - evaluate(root.children[0], variables, values)

    # if the symbol is +
    elif root.symbol == '+':
        # the truth value is the minimum of the truth value of the first one
        # and the second one
        result = max(evaluate(root.children[0], variables, values),
                     evaluate(root.children[1], variables, values))

    # return the result
    return result


def play2win_helper_function_3(root, variables, values, truth):
    '''(FormulaTree, str, str, int) -> (int, int)
    Helper function for play2win. If the main function has 2 or more remaining
    values, this function adds 0 and 1 to the value.
    REQ:
    - formula must be valid
    - formula is not empty
    - values must be consist of 1 and 0
    >>> play2win(build_tree('((-a+b)*-(c+d))'), 'EEEE', 'abcd', '00')
    0
    >>> formula = '((-a+b)*-(c+d))'
    >>> root = build_tree(formula)
    >>> first = play2win(root, 'EEEE', 'abcd', '')
    >>> second = play2win(root, 'EEEE', 'abcd', str(first))
    >>> third = play2win(root, 'EEEE', 'abcd', str(first)+str(second))
    >>> forth = play2win(root, 'EEEE', 'abcd', str(first)+str(second)+
                                                                    str(third))
    >>> result = str(first)+str(second)+str(third)+str(forth)
    >>> result == 1100
    True
    >>> a=build_tree('((x+y)*((y+z)*(-y+-z)))')
    >>> play2win(a, 'EEA', 'xyz','')
    1
    >>> play2win(a, 'EEA', 'xyz','1')
    1
    >>> play2win(a, 'EEA', 'xyz','11')
    1
    >>> a = build_tree('((x+y)*((y+z)*(-y+-z)))')
    >>> play2win(a, 'EEA', 'xyz','')
    1
    >>> play2win(a, 'EEA', 'xyz','1')
    0
    >>> play2win(a, 'EEA', 'xyz','10')
    0
    '''
    # by adding 0 to values
    (add_0_result, add_0_truth) = play2win_helper_function_1(root, variables,
                                                             values+'0', truth)
    # by adding 1 to values
    (add_1_result, add_1_truth) = play2win_helper_function_1(root, variables,
                                                             values+'1', truth)
    truth = add_1_truth or add_0_truth
    # if 0 and 1, then -> 0
    if add_1_truth == 0 and add_0_truth == 1:
        # set the result as 0
        result = int(False)
    #
    elif add_0_truth == 0 and add_1_truth == 1:
        # set the result as 1
        result = int(True)
    # otherwise . 2 possibilities. Either 0 or 1 -> 1 or both 1 and O -> 0
    else:
        result = truth
    return (result, truth)


def play2win_helper_function_2(root, variables, values, truth):
    '''(FormulaTree, str, str, int) -> (int, int)
    Helper function for play2win. If the main function has 1 remaining value
    this function evaluates case by case by adding 1 and 0.
    REQ:
    - formula must be valid
    - formula is not empty
    - values must be consist of 1 and 0
    >>> play2win(build_tree('((-a+b)*-(c+d))'), 'EEEE', 'abcd', '00')
    0
    >>> formula = '((-a+b)*-(c+d))'
    >>> root = build_tree(formula)
    >>> first = play2win(root, 'EEEE', 'abcd', '')
    >>> second = play2win(root, 'EEEE', 'abcd', str(first))
    >>> third = play2win(root, 'EEEE', 'abcd', str(first)+str(second))
    >>> forth = play2win(root, 'EEEE', 'abcd', str(first)+str(second)+
                                                                    str(third))
    >>> result = str(first)+str(second)+str(third)+str(forth)
    >>> result == 1100
    True
    >>> a=build_tree('((x+y)*((y+z)*(-y+-z)))')
    >>> play2win(a, 'EEA', 'xyz','')
    1
    >>> play2win(a, 'EEA', 'xyz','1')
    1
    >>> play2win(a, 'EEA', 'xyz','11')
    1
    >>> a = build_tree('((x+y)*((y+z)*(-y+-z)))')
    >>> play2win(a, 'EEA', 'xyz','')
    1
    >>> play2win(a, 'EEA', 'xyz','1')
    0
    >>> play2win(a, 'EEA', 'xyz','10')
    0
    '''

    # evaluate the truth values for both 1 and 0.
    truth_for_1 = evaluate(root, variables, values+'1')
    truth_for_0 = evaluate(root, variables, values+'0')
    # set the winning possibility as True/1
    possibility = int(True)
    # determine which one is True or False.
    # if the first one is the same with truth value,
    if truth_for_0 == truth:
        # then set the result as 0
        result = 0
    # if the second one is the same with the truth value,
    elif truth_for_1 == truth:
        # then set the result as 1
        result = 1
    # then there are 2 possibilities. Either both of them are wrong or they
    # both work
    else:
        result = truth
        # set the possibility as False/0
        possibility = int(False)
    return (result, possibility)


def play2win_helper_function_1(root, variables, values, truth):
    '''(FormulaTree, str, str, int) -> (int, int)
    This is the main helper function for play2win. Uses both
    play2win_helper_function_2 and play2win_helper_function_3 functions.
    Evaluates both cases, one remaining or 2 or more values remaining.
    REQ:
    - formula must be valid
    - formula is not empty
    - values must be consist of 1 and 0
    >>> play2win(build_tree('((-a+b)*-(c+d))'), 'EEEE', 'abcd', '00')
    0
    >>> formula = '((-a+b)*-(c+d))'
    >>> root = build_tree(formula)
    >>> first = play2win(root, 'EEEE', 'abcd', '')
    >>> second = play2win(root, 'EEEE', 'abcd', str(first))
    >>> third = play2win(root, 'EEEE', 'abcd', str(first)+str(second))
    >>> forth = play2win(root, 'EEEE', 'abcd', str(first)+str(second)+
                                                                    str(third))
    >>> result = str(first)+str(second)+str(third)+str(forth)
    >>> result == 1100
    True
    >>> a = build_tree('((x+y)*((y+z)*(-y+-z)))')
    >>> play2win(a, 'EEA', 'xyz','')
    1
    >>> play2win(a, 'EEA', 'xyz','1')
    1
    >>> play2win(a, 'EEA', 'xyz','11')
    1
    >>> a = build_tree('((x+y)*((y+z)*(-y+-z)))')
    >>> play2win(a, 'EEA', 'xyz','')
    1
    >>> play2win(a, 'EEA', 'xyz','1')
    0
    >>> play2win(a, 'EEA', 'xyz','10')
    0
    '''

    # if there is only 1 value remaining,
    if len(variables) == len(values)+1:
        # use  helper function
        (result, possibility) = play2win_helper_function_2(root, variables,
                                                           values, truth)
    # if there are 2 or more values remaining,
    else:
        (result, possibility) = play2win_helper_function_3(root, variables,
                                                           values, truth)
    return (result, possibility)


def play2win(root, turns, variables, values):
    '''(FormulaTree, str, str, int) -> int
    Returns the best next move for the player whose turn is next. The game
    starts with a boolean formula. For each variable, player A and E choose
    their truth value. Player A wins if the truth value of F is 0, and player
    E wins if the truth value of F is 1.
    SPECIAL CASE: If there is no winning strategy, or if choosing either 1 or
    0 would lead to winning, then 1 is returned if it is player E’s turn, and
    0 is returned if it is player A’s turn.
    REQ:
    - formula must be valid
    - formula is not empty
    - values must be consist of 1 and 0
    - turns must be consist of E and A
    - len(turns) > len(values)
    >>> play2win(build_tree('((-a+b)*-(c+d))'), 'EEEE', 'abcd', '00')
    0
    >>> formula = '((-a+b)*-(c+d))'
    >>> root = build_tree(formula)
    >>> first = play2win(root, 'EEEE', 'abcd', '')
    >>> second = play2win(root, 'EEEE', 'abcd', str(first))
    >>> third = play2win(root, 'EEEE', 'abcd', str(first)+str(second))
    >>> forth = play2win(root, 'EEEE', 'abcd', str(first)+str(second)+
                                                                    str(third))
    >>> result = str(first)+str(second)+str(third)+str(forth)
    >>> result == 1100
    True
    >>> a = build_tree('((x+y)*((y+z)*(-y+-z)))')
    >>> play2win(a, 'EEA', 'xyz','')
    1
    >>> play2win(a, 'EEA', 'xyz','1')
    1
    >>> play2win(a, 'EEA', 'xyz','11')
    1
    >>> a = build_tree('((x+y)*((y+z)*(-y+-z)))')
    >>> play2win(a, 'EEA', 'xyz','')
    1
    >>> play2win(a, 'EEA', 'xyz','1')
    0
    >>> play2win(a, 'EEA', 'xyz','10')
    0
    '''

    # determine the current player
    try:
        player = turns[len(values)]
        # if the current player is A
        if player == 'A':
            # A wins if the truth value of the formula is 0, so player A is
            # trying to make it False, therefore set the truth as 0.
            truth = 0
        # if the current player is E
        elif player == 'E':
            # E wins if the truth value of the formula is 1,so he/she is trying
            # to make it True, therefore set the truth as 1.
            truth = 1
            (result, possibility) = play2win_helper_function_1(root, variables,
                                                               values, truth)
        return result
    except UnboundLocalError:
        return 0
