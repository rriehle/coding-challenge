#!/usr/bin/env python3

#  Write a scipt that takes each column of an array/list/tuple and
#  adds it to the corresponding column of another array/list/tuple
#  and returns the result as an array/list/tuple. See the asserts
#  toward the bottom of the module for perhaps a better
#  explination of the goal.


### Ugly, brute force approach ###

def sum_as_tuple(a, b, c):
    """ Add three single-digit numbers, return the tens and singles digits seperately  """
    d = a + b + c
    return (
        d // 10,  # integer division provides the ten's or 'carry' digit
        d % 10,  # mod ten provides the single's digit
    )

def brute_force(a, b):
    maxlen = max(len(a), len(b))

    # Reverse the arguments so that the math can be done
    # iteratively from from lower-order to higher-order digits
    # that is, from right to left.

    areversed = a[::-1]  # reevrse a
    areversed += [0] * (maxlen - len(areversed))  # pad to the minimum common lengeth between a and b

    breversed = b[::-1]  # reverse b
    breversed += [0] * (maxlen - len(breversed))

    creversed = []  # accumulator for the results
    carry = 0

    for i in range(maxlen):
        carry, single = sum_as_tuple(areversed[i], breversed[i], carry)
        creversed.append(single)

    if carry:
        creversed.append(carry)  # pick up the final carry

    return creversed[::-1]  # reverse of creversed


### Elegant approach ###

#  Convert the array to a char/string,
#  convert the string to an int,
#  do the integer math,
#  convert the result back in the other direction,
#  to a str, and finally to an array/list.

def str_int_str(a, b):
    astr=""
    bstr=""

    for foo in a:
        astr += str(foo)

    for foo in b:
        bstr += str(foo)

    c = int(astr) + int(bstr)

    return [int(foo) for foo in str(c)]


### Tests ###

def test_sum_as_tuple():
    assert (0, 3) == sum_as_tuple(1, 2, 0)
    assert (1, 2) == sum_as_tuple(7, 5, 0)
    assert (1, 8) == sum_as_tuple(9, 9, 0)
    assert (2, 7) == sum_as_tuple(9, 9, 9)

def test_solutions():

    strategies = (
        brute_force,
        str_int_str,
    )

    for strategy in strategies:
        assert [6, 5, 2] == strategy([2, 5, 7], [3, 9, 5])
        assert [1, 9, 9, 8] == strategy([9, 9, 9], [9, 9, 9])
        assert [8, 5, 1, 2, 1] == strategy([8, 4, 7, 9, 2], [3, 2, 9])


### CLI ###

if __name__ == '__main__':
    print(sum_as_tuple(1, 2, 0))
    print(sum_as_tuple(7, 5, 0))
    print(sum_as_tuple(9, 9, 9))
    print(str_int_str([2, 5, 7], [3, 9, 5]))
    print(brute_force([2, 5, 7], [3, 9, 5]))
    print(str_int_str([8, 4, 7, 9, 2], [3, 2, 9]))
