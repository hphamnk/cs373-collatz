#!/usr/bin/env python

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2013
# Glenn P. Downing
# ---------------------------

# ------------
# Global
# ------------
"""
used lazy cache instead of list to eleminate the problem out of bounds
"""
cycle_cache = {1:1}

# ------------
# collatz_read
# ------------

def collatz_read (r, a) :
    """
    reads two ints into a[0] and a[1]
    r is a  reader
    a is an array of int
    return true if that succeeds, false otherwise
    """
    s = r.readline()
    if s == "" :
        return False
    l = s.split()
    a[0] = int(l[0])
    a[1] = int(l[1])
    assert a[0] > 0
    assert a[1] > 0
    return True

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    return the max cycle length in the range [i, j]
    check if i is greater than j, if yes, swap them
    use for loop to go through i to j
        check if value is in cache, use cache to find cycle length
        if value is not in cache, find cycle length function and add it to cache
    """
    assert i > 0
    assert j > 0
    # <your code>

    if i > j:
        temp = i
        i = j
        j = temp

    assert i <= j    
    
    max_cycle_num = 0
    global cycle_cache 

    for x in range (i, j+1):
        # value is in cache, use cache to find cycle length
        current_cycle_num = cycle_cache.get(x,-1)

        # value is not in cache, find cycle length and add it to cache
        if current_cycle_num == -1:
            cycle_cache[x] = cycle_length(x)
            current_cycle_num = cycle_cache[x]
        assert current_cycle_num > 0

        # check if current_cycle_num > max_cycle_num
        if current_cycle_num > max_cycle_num:
            max_cycle_num = current_cycle_num
        assert max_cycle_num >= current_cycle_num

    assert max_cycle_num > 0
    return max_cycle_num

# -------------
# cycle_length
# -------------

def cycle_length (n) :
    """
    find cycle_length(n) recursively
    base case: n = 1
    even: check if value is in cache, if not in cache, call cycle_length(n/2) + 1
    odd: check if value is in cache, if not in cache, call cycle_length((3n + 1)/2) + 2
    """

    assert n > 0

    if n == 1:
        return 1

    # even: n / 2, check if value is in cache, else call recursively,
    if ( n % 2 ) == 0:
        x = n / 2
        previous_cycle = cycle_cache.get(x,-1)
        if previous_cycle == -1:
            return cycle_length(x) + 1
        else:
            assert previous_cycle > 0
            return previous_cycle + 1

    # odd: n * 3 + 1, since this will be even, skip another step by / 2
    # check if value is in cache, else call recursively
    if ( n % 2 ) != 0:
        x = (3 * n + 1) / 2
        previous_cycle = cycle_cache.get(x,-1)
        if previous_cycle == -1:
            return cycle_length(x) + 2
        else:
            assert previous_cycle > 0
            return previous_cycle + 2

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    prints the values of i, j, and v
    w is a writer
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    v is the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    """
    a = [0, 0]
    while collatz_read(r, a) :
        v = collatz_eval(a[0], a[1])
        collatz_print(w, a[0], a[1], v)

# -------
# imports
# -------

import sys


# ----
# main
# ----

collatz_solve(sys.stdin, sys.stdout)
