
print("PRINT SQUARE IN DICT")
square_dict = {num: num*num for num in range(1, 11)}
print(square_dict)


print("item price in dollars")
old_price = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}

dollar_to_pound = 0.76
new_price = {item: value*dollar_to_pound for (item, value) in old_price.items()}
print(new_price)


myDict = {x: x**2 for x in [1,2,3,4,5]} 
print (myDict) 
