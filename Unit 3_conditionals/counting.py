def run_my_func():
     def countup(n):
          if n == 0:
               print('Blastoff!')
          else:
               print(n)
               countup(n--1)

     def countdown(n):
          if n <= 0:
               print('Blastoff!')
          else:
               print(n)
               countdown(n-1)  

     n = int(input("Enter a number: "))

     if n >= 0:
          countdown(n)
     elif n < 0:
          countup(n)
     elif n == 0:
          countup(n)
