####
# HW1
####
def recur_babylonian(p_0,n):
    """recursive implementation of babylonain algorithm
    to find sqrt(2))"""
    p_n = (p_0+(2/p_0))/2
    if (abs(p_n-p_0) < 0.001):
        return p_0
    else:
        return recur_babylonian(p_n,n)

def babylonian(p_0,n):
    """iterative implementation of babylonian algorithm
    to find sqr(2))"""
    p_n = (p_0+(2/p_0))/2
    while(abs(p_n-p_0) > 0.001 and n>0):
        p_0 = p_n
        p_n = (p_0+(2/p_0))/2
        n=n-1
        print(p_n)
    return p_n
print(babylonian(99.0,16))
