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


def recur_babylonian_sqrt_two(p_0,n):
    """
    recursive implementation of babylonain algorithm
    to find sqrt(2))
    """
    p_n = (p_0+(2/p_0))/2
    if (abs(p_n-p_0) < 0.001):
        return p_0
    else:
        return recur_babylonian_sqrt_two(p_n,n)

def babylonian_sqrt_two(n):
    """
    iterative implementation of babylonian algorithm
    converging on sqrt(2)) and associated relative errors
    """
    p_0 = float(input("We're inspired to guess: "))
    print("Guess ", p_0, " Relative Error: ", rel_error(p_0,math.sqrt(2)))
    p_n = (p_0+(2/p_0))/2
    while(abs(p_n-p_0) > 0.001 and n>0):
        print("Guess: ", p_n, " Relative Error: ", rel_error(p_n,math.sqrt(2)))
        p_0 = p_n
        p_n = (p_0+(2/p_0))/2
        n=n-1
    return p_n
def babylonian_sqrt(a):
    """
    Generalized babylonian sqrt function
    """
    if(a==0):
        return 0
    elif (a<0):
        raise Exception("Sqrt argument expected to be positive and real-valued.")
    else:
        p_0 = float(input("We're inspired to guess: "))
        iter_limit = 100
        while(abs(p_0*p_0 - a) > 0.001 and iter_limit>0):
            print("Guess ", p_0, " Relative Error: ", rel_error(p_0,math.sqrt(a)))
            p_0 = (p_0 + (a/p_0))/2
            iter_limit = iter_limit-1
        return p_0

def poly_root():
    """
    given polynomial f and f_deriv
    p_n = (p_0 - f(p_0)/f_deriv(p_0))
    """
    p_0 = float(input("Initial guess: "))
    f = p_0*p_0*p_0 - p_0
    f_deriv = 3*p_0*p_0 - 1
    p_n = (p_0 - (f/f_deriv))
    while(abs(p_0 - p_n) > 0.00001):
        p_0 = p_n
        f = p_0*p_0*p_0 - p_0
        f_deriv = 3*p_0*p_0 - 1
        p_n = (p_0 - (f/f_deriv))
        print(p_n)
    return p_n
