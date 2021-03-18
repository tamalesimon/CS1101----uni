""" nested list """
student_informations = ["simon peter tamale", "myemail@gmail.com", ["UNIV 1001", "CS 1101"], "+2568979834987"]

""" the operator * """
my_sorry = ['I am sorry'] * 5

""" slices """
my_list = ["simon", "peter"]
my_list[2:1] = ["tamale"] 

""" += operator """
my_number  = [1,2,3,4,5,6]
my_other_number = [7,8,9]
my_number += my_other_number

print (my_number)

""" filter """
random_words = ["she", "sells", "sea", "shells", "at", "the", "sea", "shore"]

def my_word_filter(word):

    if (word in random_words):
        print(random_words)
        return True
    else: 
        return False
    
my_filtered_words = filter(my_word_filter, random_words)

""" doesnt do what the programmer wanted """

def add_my_items ():
    x = [1,2,3,4,5,6]
    x = x.append(7)

    print (x)







