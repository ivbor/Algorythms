def real_bin_search(func, func_value, left_edge,
                    right_edge, eps=1e-6, check=False):
    '''
        basic binary search among real
        numbers for x where func(x) = y
        works only for monotonic functions
        in O(log2(n)) time where n is how
        many eps will fit in abs(r-l)
        r - right edge of search interval
        l - left one accordingly

        by default assumes required x
        to be between left and right edges
        but can check that
        if check is set to True
    '''

    # this algo requires O(log2(n))
    # operations where n is the amount of
    # the smallest cuts we consider (epsilons)
    # that can fit in abs(r-l)

    if check:
        result = real_bin_search(
            func,
            func_value,
            left_edge - 1,
            right_edge + 1)
        if (result < left_edge or right_edge < result):
            raise KeyError('func_value is unreachable within given edges')

    # determine whether function is
    # ascending or descending

    # l+eps and r-eps we use
    # so that search can work
    # even if function does not
    # exist in l or r
    is_ascending = (func(left_edge + eps) < func(right_edge - eps))

    # we can use while to ensure accuracy
    # is no less than eps
    while (abs(right_edge - left_edge) >= eps):

        # find the middle of the cut
        middle = (left_edge + right_edge)/2

        if is_ascending:

            # if function is ascending
            # and function is less than y
            # this means y is somewhere
            # in bigger x's (righer)
            # so move left border of the
            # current cut to the middle
            if func(middle) < func_value:
                left_edge = middle

            # if ascending and function
            # is more than y - this means
            # y is lesser x's (lefter)
            # so move right border of the
            # current cut to the middle
            else:
                right_edge = middle

        # for descending - everything
        # works accordingly with the
        # change of sign in if clause
        else:
            if func(middle) > func_value:
                left_edge = middle
            else:
                right_edge = middle

    # for even more accuracy
    # as an answer give the middle
    # of the accurate enough cut
    return (left_edge + right_edge)/2
