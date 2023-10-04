from Algorithms.python_solutions.array_count_sort import array_count_sort


def two_dim_array_count_sort(a, keys='all'):
    """
    Sorts a 2-dimensional array consisting of whole numbers.

    This function sorts the 1-dimensional arrays inside a 2-dimensional array
    in ascending order by all indexes (by default) or by exact indexes
    in the order they are presented.

    Parameters
    ----------
    a : list[list[int]]
        The 2-dimensional array to be sorted.

    keys : 'all', list of int, or int, optional
        Specifies the indexes to sort by. If 'all', it sorts by all indexes
        (default). If a list of integers is provided, it sorts by the exact
        indexes in the specified order. If an integer is provided,
        it sorts by a single index.

    Returns
    -------
    list[list[int]]
        The sorted 2-dimensional array.

    Raises
    ------
    TypeError
        Raised if the 'keys' argument is of an unsupported type.

    """

    if keys == 'all' or isinstance(keys, list):

        # divide cases with keys=all and keys in list

        # for 'all' option need to know how many
        # columns are available exactly
        m = max([len(i) for i in a])

        # then translate option 'all' to list
        keys = [i for i in range(m)] if keys == 'all' else keys

        # use helper to ease complexity of code
        two_dim_array_count_sort_list(a, keys)

    elif isinstance(keys, int):
        a = array_count_sort(a, key=keys)
    else:
        raise TypeError('Cannot parse keys')
    return a


def two_dim_array_count_sort_list(a, keys):
    """
    Helper function for sorting a 2-dimensional array by specific keys.

    This function is used internally by `two_dim_array_count_sort`
    to perform the sorting of a 2-dimensional array based on specific keys.

    Parameters
    ----------
    a : list[list[int]]
        The 2-dimensional array to be sorted.

    keys : list of int
        Specifies the indexes to sort by.

    Returns
    -------
    None

    """
    # list of rows with the same key symbol (to be sorted further)
    p_set = [0, len(a)-1]

    # list of p_sets
    p_set_list = [p_set]

    for i in keys:

        # after first launch update list of p_sets
        new_p_set_list = list()

        # need to sort only entries with the same key digits
        # (or all entries only on the first launch)
        for k in p_set_list:

            # if there comes only one entry with the same digit -
            # doesn't need to be sorted further
            if len(k) >= 2:

                # sort entries with the same key digits,
                # take position of their new rows
                # entries with the same key values are
                # packed in lists (they are to be sorted)
                a[k[0]:(k[-1] + 1)], p = \
                    array_count_sort(a[k[0]:(k[-1] + 1)],
                                     key=i, position=True)

                # based on new entries' places (p array)
                # make a list where lists in p array
                # are unpacked and indexes of unpacked
                # elements are marked by the same values
                ind_uniq_rows = list()
                for o in range(len(p)):
                    if isinstance(p[o], list):
                        for _ in range(len(p[o])):
                            ind_uniq_rows.append(o + k[0])
                    else:
                        ind_uniq_rows.append(o + k[0])

                # using list with unpacked lists and
                # elements from them marked
                # make sets of indexes of rows
                # with the same elements to sort
                # them further or at least distinguish
                p = ind_uniq_rows
                p_set = list()
                for o in range(1, len(p)):
                    if p[o-1] == p[o]:
                        if (o-1) not in p_set:
                            p_set.append(k[0] + o - 1)
                        if o not in p_set:
                            p_set.append(k[0] + o)

                    # once the set is compiled -
                    # all consequently equal
                    # elements included - collect it
                    # and clear the list for the next set
                    if (p[o-1] != p[o] or o == len(p) - 1) and \
                       (p_set not in new_p_set_list):
                        new_p_set_list.append(p_set)
                        p_set = list()

        # put new p_sets list with collected p_sets
        # to the place of old p_set list
        # to be sorted by the next index
        p_set_list = new_p_set_list
