"""
This module contains the function for recursive insertion sort
"""

def insertion_sort(ul):
    """ Insertion sort """
    for index in range(1, ul.size()):
        pos = index
        while pos > 0 and ul.get(pos) < ul.get(pos-1):
            first = ul.get(pos)
            second = ul.get(pos-1)
            ul.set(pos-1, first)
            ul.set(pos, second)
            pos -= 1
    return ul

def recursive_insertion(ul, itr=0):
    """ Insertion sort recursive """
    if itr > ul.size() - 1 or itr < 0:
        return ul
    key = ul.get(itr)
    pos = itr - 1
    while pos > -1 and ul.get(pos) > key:
        ul.set(pos + 1, ul.get(pos))
        pos = pos - 1
    ul.set(pos + 1, key)
    return recursive_insertion(ul, itr + 1)
