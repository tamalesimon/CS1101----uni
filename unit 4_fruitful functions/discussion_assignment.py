def check_even_odd(n): #without the argument precondition
    r = n % 2
    print((r)," is the remainder")
    if r == 0:         #postcondition
        e = "is an even number"
        return n, e     #return statement for return value
    else:
        o = "is an odd number"
        return n, o     #return statement for return value
        
