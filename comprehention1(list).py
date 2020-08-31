print("PRINT THE ITERATION ")
print([x for x in range(1,11)])


print("PRINT SQUARE VALUES ")
print ([x**2 for x in range(1,11)])


print("PRINT THE EVEN NUMBERS")
print([x for x in range(1,11)if x%2==0])


print("PRINT THE ODD NUMBERS")
print([x for x in range(1,11)if x%2==1])

print("PRINT THE if and else BLOCK")
print([x if x>2 else x+1 for x in range(1,11)])


print("PRINT THE EVEN NUMBERS SQUARE AND ODD NO CUBE")
print([x**2 if x%2==0 else x**3 for x in range(1,11)])

