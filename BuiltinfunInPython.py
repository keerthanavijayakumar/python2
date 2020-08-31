print("ABS FUNCTION5")
print(abs(7))
print(abs(-8))
print(abs(7.44))
print(abs(-1.7))
my_list=[1,2,-3,6,-4]
print(my_list)
new_list=[abs(i)for i in my_list]
print(new_list)


print("ALL FUNCTION")
print(all("Hai"))
print(all(""))
##print(all(1))
print (all([False,0]))
print (all([10,13]))



print("ALL FUNCTIONS IN LIST")
listsame=[1,1,1]
listdiff=[1,2,3]
print (all([x == 1 for x in listsame]))
print (all([x == 2 for x in listsame]))
print (all([x == 1 for x in listdiff]))
print (any([x == 1 for x in listdiff]))


print("ANY FUNCTIONS ")
names=["keerthana","priya","muthu","sowmi"]
print(any([x == "muthu" for x in names]))

print(any([x == "keerthi" for x in names]))

print(any(""))
print(any({}))
print(any([]))
print(all(""))
print(all(""))
print(all(""))


print("b00l FUNCTIONS ")
number = 5
print('The binary equivalent of 5 is:', bin(number))

test = []
print(test,'is',bool(test))

test = [0]
print(test,'is',bool(test))

test = 0.0
print(test,'is',bool(test))

test = None
print(test,'is',bool(test))

test = True
print(test,'is',bool(test))

test = 'Easy string'
print(test,'is',bool(test))
