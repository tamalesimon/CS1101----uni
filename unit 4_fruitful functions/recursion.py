def is_divisible(x, y): #defining is_divisible func
    return x % y == 0 

def is_power(x, y):
    if x == y:          #x is power of Y if both numbers are equal BASE 1
        return True
    if y == 1:          #the only positive int that is power of 1 is itself  BASE 2
        return False
    if not is_divisible(x, y): #is_power calling is_divisible
        return False
    return is_power(int(x/y), y) #is_power calling is_itself recursively



n = int(10.)

print(isinstance(n, float), isinstance(n * 1.0, float))

def area(l, w):
    temp = l * w;
    return temp

l = 4.0
w = 3.25
x = area(l, w)
if ( x ):
  print (x)

    