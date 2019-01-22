requested_toppings = 'mushrooms'

if requested_toppings != 'anchovies':
    print("Hold the Anchovies")

requested_toppings = ['mushroom', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms")
if  'pepperoni' in requested_toppings:
    print("Adding pepperoni")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese")

requested_toppings.append('green peppers')
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.") 
    else:
         print("Adding " + requested_topping + ".")
empty_list = []

if empty_list:
    print("not empty")
else:
    print("Empty")