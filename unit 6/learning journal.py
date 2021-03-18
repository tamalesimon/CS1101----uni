def messing_with_words():
    my_set_of_words = "I want to travel the world writing code"
    x = my_set_of_words.split()
    print (x)
    print ('\n')

    """ removing items """

    x.pop(2) # removing items with pop
    print(x)
    
    print ('\n')
    x.remove('travel') # removing items with remove
    print (x)

    print ('\n')
    del x[3] # Removing items with del
    print (x)

    """ sorting iteems """
    print('\n')
    x.sort() # sorting
    print (x)

    """ Adding items """
    print('\n')
    x[3:1] = ["goal"] # adding items with slices
    print (x)

    print('\n')
    x.insert(4, "to") # adding items with insert
    print(x)

    print('\n')
    x.insert(5, "be")
    print(x)

    print('\n')
    x.append("and traveling") # adding items with append
    print (x)

    print('\n')
    space = ' '
    print (space.join(x))  # joining and printing the joined strings

messing_with_words()

