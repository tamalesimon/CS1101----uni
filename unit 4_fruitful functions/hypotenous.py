from math import sqrt
""" step 1 importing helper function from math Sqrt """

""" step 2 defining the hypotenuse() which takes 2 arguments (a,b) """
def hypotenuse(a, b):
    
    """ finding a_side length """
    a_side = a**2 #here finding a_side Squared
    

    """ finding b_side length """
    b_side = b**2 #here finding b_side Squared
    


    result = a_side+b_side #adding both sides together
    """ following the fomular we add the sides together """

    return sqrt(result) #returning the square root of result as the hypotenuse side

print(hypotenuse(3,4))




    