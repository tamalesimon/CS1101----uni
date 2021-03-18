alphabet = "abcdefghijklmnopqrstuvwxyz"   

test_dups = ["zzz","dog","bookkeeper","subdermatoglyphic","subdermatoglyphics"] 

test_miss = ["zzz","subdermatoglyphic","the quick brown fox jumps over the lazy dog"] 

def histogram(s):
     d = dict()
     for c in s:
          if c not in d:
               d[c] = 1
          else:
               d[c] += 1
     return d 

     """ Part 1 """

def has_duplicates(s): #has_duplicates function definition
     my_dict = histogram(s)
     for v  in my_dict.values():
          if v > 1:
               return True
          return False

def test_dups_func(): #testing the duplicates
   for s in test_dups:
                    duplicates = has_duplicates(s)
                    if duplicates:
                         print (s+ ' ', 'has duplicates', '\n')
                    else:
                         print (s+ ' ', 'has no dupicates', '\n')

def missing_letters(s):
    r = list(alphabet)
    s = s.lower()
    for c in s.lower():
        if c in r:
            r.remove(c)  # removes the instance where there is no missing_letters
    return ''.join(r)


""" Part 2 """
def test_miss_func():
     
    for s in test_miss:
               missing = missing_letters(s)
               if missing:
                    print(s +' ' + 'is missing leters', missing_letters(s), '\n')
               else: 
                    print(s+ ' '+ 'uses all the letters',)
     
          
               
        
     

             
        




