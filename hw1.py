####
# HW1
####
import math

def rel_error(measured, expected):
    return (measured-expected)/expected

def recur_rel_error(e_r):
    """
    recursive implementation of relative error of babylonian
    algorithm
    """
    pass


def recur_babylonian(p_0,n):
    """
    recursive implementation of babylonain algorithm
    to find sqrt(2))
    """
    p_n = (p_0+(2/p_0))/2
    if (abs(p_n-p_0) < 0.001):
        return p_0
    else:
        return recur_babylonian(p_n,n)

def babylonian(p_0,n):
    """
    iterative implementation of babylonian algorithm
    converging on sqrt(2)) and associated relative errors
    """
    print("Guess ", p_0, " Relative Error: ", rel_error(p_0,math.sqrt(2)))
    p_n = (p_0+(2/p_0))/2
    while(abs(p_n-p_0) > 0.001 and n>0):
        print("Guess ", p_n, " Relative Error: ", rel_error(p_n,math.sqrt(2)))
        p_0 = p_n
        p_n = (p_0+(2/p_0))/2
        n=n-1
