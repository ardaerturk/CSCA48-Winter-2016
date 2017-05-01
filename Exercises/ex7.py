def edit_distance(s1, s2):
    if len(s1) == 0:
        result = 0
    else:
        result = edit_distance(s1[1:], s2[1:])
        if s1[0] != s2[0]:
            result += 1
    return result


def subsequence(s1, s2):
    if len(s1) != 0 and len(s2) == 0:
        return False
    elif len(s1) == 0 or (s2 == s1):
        return True
    else:
        if s1[-1] == s2[-1]:
            return subsequence(s1[:-1], s2[:-2])
        else:
            return subsequence(s1, s2[:-1])


def perms(s):
    if len(s) <= 1:
        result = set(s)
    elif len(s) == 0:
        result = 'None'
    else:
        result = set()
        for element in perms(s[1:]):
            for elements in range(len(s) + 1):
                i = element[:elements]
                k = s[0]
                l = element[elements:]
                result.add(i + k + l)
    return result
