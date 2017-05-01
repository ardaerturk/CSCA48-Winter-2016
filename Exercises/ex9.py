def radix_sort(L):
    '''(list of ints) -> list
    returns a list with the same integers sorted in non-decreasing order by
    radix sort algorithm
    '''
    max_item = max(L)

    def radix_sort_helper(L, curr):
        if (curr > max_item):
            return L
        else:
            one = [element for element in L if (element & curr != 0)]
            zeros = [element for element in L if (element & curr == 0)]
            return radix_sort_helper(zeros + one, curr << 1)
    return radix_sort_helper(L, 1)
