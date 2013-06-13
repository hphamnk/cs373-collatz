#!/usr/bin/env python

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2013
# Glenn P. Downing
# ---------------------------

# ------------
# Global
# ------------

#cycle_cache = [0] * 1000001

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
    """
    assert i > 0
    assert j > 0
    # <your code>

    if i > j:
        temp = i
        i = j
        j = temp
    
    max_cycle_num = 0
    global cycle_cache 


    for x in range (i, j+1):

        # value is in cache, use cache to find cycle length
        current_cycle_num = cycle_cache.get(x,-1)

        # value is not in cache, find cycle length and add it to cache
        if current_cycle_num == -1:
            cycle_cache[x] = cycle_length(x)
            current_cycle_num = cycle_cache[x]

        # check if current_cycle_num > max_cycle_num
        if current_cycle_num > max_cycle_num:
            max_cycle_num = current_cycle_num

    assert max_cycle_num > 0
    return max_cycle_num

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

# -------------
# cycle_length
# -------------

def cycle_length (n) :

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
            return previous_cycle + 1

    # odd: n * 3 + 1 , check if value is in cache, else call recursively
    if ( n % 2 ) != 0:
        x = (3 * n + 1) / 2
        previous_cycle = cycle_cache.get(x,-1)
        if previous_cycle == -1:
            return cycle_length(x) + 2
        else:
            return previous_cycle + 2
