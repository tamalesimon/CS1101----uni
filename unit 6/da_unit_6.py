import math



def my_sqrt(a):
   

 x = 1
    

while True:
        

    y = (x + a / x) / 2.0
       

    if y == x:
           

        break
       

    x = y
    

        return x

    def test_sqrt():
   

        a = 1
    

        while a < 26:
        

            print('a =', a, '| my_sqrt(a) =', my_sqrt(a), '| math.sqrt(a) =', math.sqrt(a), '|

 diff =', abs(my_sqrt(a) - math.sqrt(a)))
       

 a = a + 1



test_sqrt()