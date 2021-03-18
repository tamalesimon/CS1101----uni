import math  #importing all the math modules including sqrt

def my_sqrt(a): # this is for my_sqrt function definition
        x = 1
        while True:
            y = (x + a/x) / 2.0
            if y == x:
                break
            x = y 
            return y

def test_sqrt(): # this is the function to call the printing table
    a = 1.0 # struggled here abit the interpreter wanted a float and i was giving it an int
    while a < 25:
        a += 1 
        print('a =',a,"|" ' ' 'my_sqrt(a) =', my_sqrt(a), "|" ' ' 'math.sqrt(a) = ', math.sqrt(a), "|", 'Diff =', my_sqrt(a)-math.sqrt(a))
        # my print statement as you can see for the diff(abs value) which is my_sqrt(a)-math.sqrt(a)
        
