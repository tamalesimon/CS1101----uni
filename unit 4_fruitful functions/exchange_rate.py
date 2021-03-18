def convert_money_exchange(rate, usd, euros):

    """ testing euros condition """
    if rate > 4000 or rate == 4580: #because the Euro 
        UGX = rate * euros
        return UGX
    """ 
    >>> convert_money_exchange(2000, 2, 2)
    # when we run it with that test case nothing happens which is correct
    
    >>> convert_money_exchange(4300, 6, 20)
    86000
    # when we run it with the above test case it returns 86,000 UGX, which is correct
    """

    """ testing the usd condition """
    if rate > 3000 or rate == 3850: #bacause the USD flactuates against the UGX Shilling
        UGX = rate * usd
        return UGX 
    
    """ 
    >>> convert_money_exchange(2000, 2, 2)
    # when we run it with that test case nothing happens which is correct
    
    >>> convert_money_exchange(3300, 2, 20)
    6600
    # when we run it with the above test case it returns 86,000 UGX, which is correct
    """


    
