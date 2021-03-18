def run_my_func(): #defined a function that i can to run the whole
     def countup(n): #count up function defined here
          if n == 0:
               print('Blastoff!')
          else:
               print(n)
               countup(n--1)

     def countdown(n): #count down function defined here
          if n <= 0:
               print('Blastoff!')
          else:
               print(n)
               countdown(n-1)  

     n = int(input("Enter a number: ")) #here the input keyword to prompt user to enter a number

     if n >= 0:     #if statement to switch between countup and countdown
          countdown(n)
     elif n < 0:
          countup(n)
     elif n == 0:
          countup(n)


# runime error program


""" def get_mytransaction (Transaction):
     Transaction = 1000
     mytransaction = Transaction
     if Transaction >= 0 and mytransaction == 500:
          print("Acount balance:"+" "+int(Transaction))
     else:
          print(mytransaction)
          get_mytransaction(500--200) """


     
