##################
# HW3 Modules
# Abhiram Kakuturu
###################

import random

def binary_noise(x):
    """
    Random noise modification of 50th+ binary digits of input.
    """
    ## Create a bit mask based on the
    ## position passed in
    ## produces '10000' if we pass in position=4
    ## our bit in the '4th' position is set to 1
    binary = bin(x)[2:]
    for position in range(50, len(binary)):
        bit_mask = random.randint(0, 1) << position
        x = bit_mask | x
    return int(binary, 2)

def modulo_map(x_n, noise=False):
    """
    Binary shift map.
    Optional parameter to include random noise in the 50th+ binary digits.
    """
    mapped = 2.*x_n % 1
    if noise:
        mapped = binary_noise(mapped)
    return mapped

def tent_map(x_n):
    """
    Tent map where F(x) = (x<0.5) ? x : 1-x
    """
    return x_n if x_n<0.5 else 1-x_n

def logistic_map(x_n, c=4):
    """
    Logistic map of the form F(x) = cx(1-x)
    """
    return c*x_n*(1-x_n)

def orbit_vector(f, x_0, n):
    """
    Applies given mapping 'f' on 'x_0' for 'n' iterations and returns vector of orbit taken.
    """
    orbit = [0]*n
    orbit[0] = x_0
    for i in range(1,n):
        orbit[i]= f(orbit[i-1])
    return orbit
