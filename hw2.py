################
# HW2 Modules
################

def unzip_trajectory(trajectory):
    """
    Method to separate trajectory from errors as generated in logistic_map below
    """
    return list(zip(*trajectory))

def logistic_attractor(c):
    """
    Simple calculation of logistic attractor, analytically derived for c=/=0.
    """
    return 1.-(1./float(c))

def logistic_map(c, x_0, n=1000):
    """
    Logistic map of the form F(x)=cx(1-x). 
    Specify constant c and intial point x_0 to converge to the attractor at 10E-5 level.
    Optionally specify iteration parameter.
    """
    attractor = logistic_attractor(c)
    x = []
    abs_error = []
    x_1 = c*x_0*(1-x_0)
    i=1
    while(abs(x_0-x_1)>0.00001 and i<=n):
        x.append(x_0)
        abs_error.append(abs(attractor-x_0))
        x_0 = x_1
        x_1 = c*x_0*(1-x_0)
        i = i+1
    x.append(x_0)
    abs_error.append(abs(attractor-x_0))
    return x, abs_error

def modulo_map(x_0, n=1000):
    """
    Map defined by x_n+1= 2*x_n mod 1.
    """
    x = [0] * n
    x[0] = x_0
    for i in range(1,n-1):
        x_0 = 2.*x_0 % 1
        x[i] = x_0
    return x