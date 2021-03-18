country = 'Uganda', 'Kenya', 'Norway', 'South Africa', #defining a tuple
capital = ['Kampala', 'Nairobi', 'Oslo', 'Joburg'] #defining a list 

#using zip
country_capital = list(zip(country, capital))

print(country_capital) #printing out a list of tuples

for index in enumerate(country_capital):
    print(index)

my_capital_country = {'Uganda':'Kampala', 'Kenya':'Nairobi', 'Norway':'Oslo', 'South Africa':'Joburg'}
print(my_capital_country.items()) #printing