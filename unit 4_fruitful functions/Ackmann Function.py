"""
A(m, n) =
n + 1                   if m = 0
A(m − 1, 1)             if m > 0 and n = 0
A(m − 1, A(m, n − 1))   if m > 0 and n > 0 
"""


def Ack_func(m, n):  #defining the AckerMann_function

    if m == 0:
        return n + 1  #going to test this out
    """ testing out the first block and it works
        >>> def Ack_func(m,n): #defining the AckerMann_function
        ...     if m == 0:
        ...         return n+1
        ...
        >>> Ack_func(0,1)
    """

    if n == 0:
        return Ack_func(m - 1,
                        1)  #evaluating the second condition AckerMann_function


#tested it out and i didnt understand the out it produced nothing

    else:
        return Ack_func(m - 1, Ack_func(m, n - 1))

print(Ack_func(3, 4))  #evaluted A(3, 4) result was 125
""" If higher values of A(m, n) are evaluated, brings 

RecursionError: maximum recursion depth exceeded in comparison
>>> """
