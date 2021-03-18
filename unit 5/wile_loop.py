""" str = "Simon" # initial string
reversedString=[]
index = len(str) # calculate length of string and save in index
while index > 0: 
    reversedString += str[ index - 1 ] # save the value of str[index-1] in reverseString
    index = index - 1 # decrement index
print(reversedString) """

""" prefixes = 'JKLMNOPQU'
suffix = 'ack'
for letter in prefixes:
    print(letter + suffix) """

fruit = 'banana'
fruit[:]