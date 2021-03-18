prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    if letter in ('O', 'Q'): # here is where i specified the condition to add 'u'
                            # struggled a bit added 'O' and 'Q' it didn't work why?
        print (letter + 'u' + suffix)
    else:
        print(letter + suffix)


# slices using a negative slice step to reverse list
my_fruit_basket = ["bananas", "carrots", "goose berries", "apples"]
print(my_fruit_basket[::-1]) # double colon with slice step reverses list

# selecting a specific item in a string
my_name = "Simon Peter Tamale"
my_name = my_name[12:] #select starting from index 12
print (my_name)

# change items in the object list
my_fruit_basket = ["bananas", "carrots", "goose berries", "apples"]
my_fruit_basket[:2] = ["tomatoes", "oranges",]
print (my_fruit_basket)

