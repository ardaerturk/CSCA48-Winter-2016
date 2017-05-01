"""
# Copyright Nick Cheng, Arda Erturk 2016
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 1, CSCA48, Winter 2017
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

from salboard import SALboard
from salbnode import SALBnode


def salb2salbLL(salb):
    ''' (SALboard) -> LinkedList
    Given a dictionary representation of a snakes and ladders board, return
    the linked list representation of the same board. Make the linked list
    circular.

    REQ and additional notes;
    - The last square cannot be the source or the destination of a snadder
    under "linked list representation":
    - The last node represents the last square. It is linked to the first
    node, which represents square 1.
    - No square can be the destination of more than one snadder.
    - The last square cannot be the source or the destination of a snadder.
    - NumSquares must be equal or greater than 1.
    '''
    # find the total squares on the board
    total_squares = salb.numSquares
    # find the dictionary representation of the snadders board
    snadders_dict = salb.snadders
    # set the head of the linked list using the given node
    head = SALBnode()
    # set the tail as head
    tail = head
    # loop through the squares
    for i in range(1, total_squares):
        # set a node
        LL = SALBnode()
        # the previous node has to be linked to the new created node
        tail.next = LL
        tail = LL

    # loop through the dictionary representaion of the snadders board to
    # implement the moves between the square if the square is the source of
    # a snadder of a snake
    for element in snadders_dict.items():
        # set the source of the snadder. We will move the player to the
        # destination of the snadder which is the key in the dictionary.
        source = element[0]
        # set the destination which is the tail of the snadder. It is the
        # value in the dictionary representation of the snadders board.
        destination = element[1]
        # set the node of the source as the head of the linked list.
        source_LL = head
        # loop through the linked list.
        for item in range(source-1):
            source_LL = source_LL.next
        # set the node of the destination as the head of the linked list.
        finish_LL = head
        # loop through the linked list
        for item in range(destination-1):
            finish_LL = finish_LL.next
        # the source must be linked to the destination of the source
        source_LL.snadder = finish_LL
    # create a circular linked list. The tail links to the head of the linked
    # list
    tail.next = head
    # return the linked list
    return head


def willfinish(first, stepsize):
    '''(SALBnode, int) -> bool
    Given a linked list representaion of a snakes and ladders board and a
    stepsize, returns whether a player playing on the board with the given
    step size will ever land on the last square.

    REQ and additional notes;
    - The last square cannot be the source or the destination of a snadder
    under "linked list representation":
    - The last node represents the last square. It is linked to the first
    node, which represents square 1.
    - No square can be the destination of more than one snadder.
    - The last square cannot be the source or the destination of a snadder.
    - NumSquares must be equal or greater than 1.
    - stepsize must be equal or greater than 1.

    >>> board = SALboard(14, {2:5, 3:6})
    >>> test = salb2salbLL(board)
    >>> willfinish(test, 7)
    True
    >>> board = SALboard(16,{})
    >>> test = salb2salbLL(board)
    >>> willfinish(test, 3)
    True
    >>> board = SALboard(4, {3:1})
    >>> test = salb2salbLL(board)
    >>> willfinish(test, 3)
    False
    '''
    board = 1
    # set the last node
    if first.next == first:
        tail = first
    # set the board size
    else:
        curr = first.next
        while curr != first:
            if curr.next == first:
                tail = curr
            curr = curr.next
            board += 1
    # Set the new head with the given stepsize
    curr = first
    for i in range(stepsize-1):
        curr = curr.next
    # loop through if the board has a snadders in the given board
    while curr.snadder is not None:
        curr = curr.snadder
    # set the step as 0
    step_1 = 0
    # loop through the linked list. If the current node is None(last node);
    while curr != tail and step_1 < board * 3:
        for i in range(stepsize):
            curr = curr.next
        while curr.snadder is not None:
            curr = curr.snadder
        step_1 += 1
    # if the current node reaches the last node, then it is possible to finish
    # the game with the given stepsize. Set the result as True
    if curr == tail:
        result = True
    # else the user can not finish with the given stepsize. Set the result as
    # False
    else:
        result = False
    # return result
    return result


def whowins(first, step1, step2):
    ''' (SALBnode, int, int) -> int
    Given a linked list representation of snakes and ladders board and two
    step sizes for player 1 and player 2 respectively, return the number
    of the player that wins the game on the given board with players using
    their given step sizes.
    REQ and additional notes;
    - The last square cannot be the source or the destination of a snadder
    under "linked list representation":
    - The last node represents the last square. It is linked to the first
    node, which represents square 1.
    - No square can be the destination of more than one snadder.
    - The last square cannot be the source or the destination of a snadder.
    - NumSquares must be equal or greater than 1.
    - step1 and step2 must be equal or greater than 1.

    >>> board = SALboard(14, {2:5, 3:6})
    >>> test = salb2salbLL(board)
    >>> whowins(test, 21, 1)
    2
    >>> board = SALboard(14, {2:5, 3:6})
    >>> test = salb2salbLL(board)
    >>> whowins(test, 30, 60)
    2
    >>> board = SALboard(100, {})
    >>> test = salb2salbLL(board)
    >>> whowins(test, 30, 60)
    2
    >>> board = SALboard(1, {})
    >>> test = salb2salbLL(board)
    >>> whowins(test, 21, 1)
    1
    '''
    # set the linked list
    player_1 = first
    current_node = first.next
    final_node = first
    # set the counter as 1
    N = 1
    # find the number of squares
    while(current_node != player_1):
        current_node = current_node.next
        N += 1
    # loop through the squares to set the last node.
    for i in range(N-1):
        final_node = final_node.next
    # set the player's location according to the given stepsize
    for i in range(step1-1):
        player_1 = player_1.next
    # if the player is on the final node, he/she is the winner!! return
    # his/her player number
    if (player_1 == final_node):
        result = 1
    else:
        # if the player is not on the final node, continue the process.
        while(player_1 != final_node):
            # set the player's locacation according to the given step size
            for i in range(step1):
                player_1 = player_1.next
            # if the current node is a source of a snadder, go to the
            # destination of the snadder
            if (player_1.snadder is not None):
                player_1 = player_1.snadder
            if (player_1 == final_node):
                result = 2
    return result


def dualboard(first):
    '''(SALBnode) -> SALBnode
    Given a linked list representation of a snakes and ladders board, return
    the linked list that represents its dual. we define its dual to be the
    snakes and ladders board with the same number of squares, and the same
    number of snadders, except the source and destination of each snadder are
    interchanged.

    REQ and additional notes;
    - The last square cannot be the source or the destination of a snadder
    under "linked list representation":
    - The last node represents the last square. It is linked to the first
    node, which represents square 1.
    - No square can be the destination of more than one snadder.
    - The last square cannot be the source or the destination of a snadder.
    - NumSquares must be equal or greater than 1.

    >>> head = salb2salbLL(SALboard(9, {3: 1, 2: 5}))
    >>> other = salb2salbLL(SALboard(9, {1: 3, 5: 2}))
    >>> dual = dualboard(head)
    >>> dual == other
    True
    >>> head = salb2salbLL(SALboard(10, {}))
    >>> other = salb2salbLL(SALboard(10, {}))
    >>> dual = dualboard(head)
    >>> dual == other
    True
    >>> head = salb2salbLL(SALboard(9, {3: 1, 2: 5}))
    >>> other = salb2salbLL(SALboard(9, {2: 7, 4: 8}))
    >>> dual = dualboard(head)
    >>> dual == other
    False
    >>> head = salb2salbLL(SALboard(10, {3: 1, 2: 5}))
    >>> other = salb2salbLL(SALboard(15, {1: 3, 5: 2}))
    >>> dual = dualboard(head)
    >>> dual == other
    False
    '''
    # set the current node
    current = first

    # set the head as a node
    head = SALBnode()
    final = head
    # set a count variable that is equal to 0
    count = 0
    # loop through the number of squares to find the total number of squares
    # on the given board

    total_squares = first.next
    while(total_squares != current):
        total_squares = total_squares.next
        count += 1
    # we need to make a new board and the number of squares must be equal
    # to our main board

    for element in range(count):
        LL = SALBnode()
        final.next = LL
        final = LL

    # the last square(the last node) must be linked to the first node.
    # when we do that, the linked list becomes circular.
    final.next = head

    # use elemental for loop to implement the snadder board to our new board.
    for element in range(count):

        # set the current node
        curr = head
        # if the current node is a source of a snadder( on the given board),
        # then go to the destination of that snadder.
        find = first
        if current.snadder is not None:
            N = 0
            while (current.snadder != find):
                N += 1
                find = find.next
            # we have to change the destination point and the source point of
            # the snadder on the cloned board
            if (current.snadder == find):
                dest = head
                # set the source on the new board
                for node_2 in range(N):
                    # This will be the new source
                    dest = dest.next
                    N = 0

                # set the destination on the new board
                for find in range(element):
                    curr = curr.next

                # on the cloned board, change the source of the snadder and
                # the destination of the board. For example, if the snadder
                # {3: 8} on the original board, it will become {8: 3} on
                # the new board
                dest.snadder = curr

                # if the current node is a source of a snadder, do the same
                # process for them as well
                current = current.next
        # if the current node is not a source of a snadder, then continue
        # with the next node
        else:
            current = current.next

    # return the cloned board
    return head
