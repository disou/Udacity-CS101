__author__ = 'dis'

# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.
def symmetric(symm_table):
    """ Check if the provided table is symmetric or not.

    :param symm_table: list of lists
    """
    try:
        for indx in range(0, len(symm_table)):
            for sec_indx in range(0, len(symm_table[indx])):
                if symm_table[indx][sec_indx] != symm_table[sec_indx][indx]:
                    return False
    except IndexError:
        return False
    return True


# def symmetric_fast(symm_table):
#     check_list = [(symm_table[row][col] == symm_table[col][row])
#                   for row in range(0, len(symm_table))
#                   for col in range(0, len(symm_table[row]))
#                   ]
#     # print check_list
#     return True if False not in check_list else False


# print symmetric([[1, 2, 3],
#                [2, 3, 4],
#                [3, 4, 1]])
#>>> True

#print symmetric([["cat", "dog", "fish"],
#                ["dog", "dog", "fish"],
#                ["fish", "fish", "cat"]])
#>>> True

#print symmetric([["cat", "dog", "fish"],
#                ["dog", "dog", "dog"],
#                ["fish","fish","cat"]])
#>>> False

#print symmetric([[1, 2],
#                [2, 1]])
#>>> True

#print symmetric([[1, 2, 3, 4],
#                [2, 3, 4, 5],
#                [3, 4, 5, 6]])
#>>> False

#print symmetric([[1,2,3],
#                 [2,3,1]])
#>>> False
