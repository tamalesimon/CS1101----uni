def new_line(): #defining the "dot" to represent the lines
    print('.')

def three_lines(): #defining 3lines function here 
    new_line()
    new_line()
    new_line()


def nine_lines(): #defining 9lines function here
    three_lines()
    three_lines()
    three_lines()


def clear_screen(): #defining 25line function here
    nine_lines()
    new_line()
    three_lines()
    three_lines()    
    nine_lines()

nine_lines() #calling nine_lines function here
print("here above, 9 lines") 
print("\n")
print("here below, 25 lines ")
clear_screen() #calling clear_screen function here
