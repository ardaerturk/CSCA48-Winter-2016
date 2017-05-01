class BTNode(object):
    """A node in a binary tree."""

    def __init__(self, value, left=None, right=None):
        """(BTNode, int, BTNode, BTNode) -> NoneType
        Initialize this node to store value and have children left and right,
        as well as depth 0.
        """
        self.value = value
        self.left = left
        self.right = right
        self.d = 0

    def __str__(self):
        return self._str_helper("")

    def _str_helper(self, indentation=""):
        """(BTNode, str) -> str
        Return a "sideways" representation of the subtree rooted at this node,
        with right subtrees above parents above left subtrees and each node on
        its own line, preceded by as many TAB characters as the node's depth.
        """
        ret = ""

        if(self.right is not None):
            ret += self.right._str_helper(indentation + "\t") + "\n"
        ret += indentation + str(self.value) + "\n"
        if(self.left is not None):
            ret += self.left._str_helper(indentation + "\t") + "\n"
        return ret

    def set_depth(self, depth):
        '''(BTNode, int) -> NoneType'''
        self.d = depth
        for element in (self.left, self.right):
            if (element is not None):
                element.set_depth(depth + 1)
        return
    # #######################????

    def leaves_and_internals(self):
        '''(BTNode, int) -> (set,set)'''

        (leaves, internals) = self.leaves_and_internals_helper()
        try:
            internals.remove(self.value)
        except KeyError:
            pass
        return (leaves, internals)

    def leaves_and_internals_helper(self):
        leaves = set()
        internals = set()

        if (self.left is None) and (self.right is None):
            leaves.add(self.value)
            return (leaves, internals)
        else:
            for element in (self.left, self.right):
                if (element is not None):
                    (templeaves, tempinternals) = \
                        element.leaves_and_internals_helper()
                    leaves.update(templeaves)
                    internals.update(tempinternals)
            internals.add(self.value)
            return (leaves, internals)

    def sum_to_deepest_helper(self):
            if (self.left is None) and (self.right is None):
                return (self.d, self.value)
            else:
                depth_sum = []
                for element in (self.left, self.right):
                    if (element is not None):
                        depth_sum.append(element.sum_to_deepest_helper())
                (max_d, sum_d) = max(depth_sum)
                return (max_d, sum_d + self.value)

    def sum_to_deepest(self):
        self.set_depth(0)
        (depth, sum_d) = self.sum_to_deepest_helper()
        return sum_d

if(__name__ == "__main__"):
    # just a simple tree to practice on
    my_tree = BTNode(10, BTNode(3, BTNode(5), BTNode(2)),
                     BTNode(7, BTNode(4, BTNode(9)), BTNode(6)))
    print(my_tree)
