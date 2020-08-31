class father():#base class
    F_name="vijaya kumar"
    Age=48
class son(father):
    Son_name="vignesh"
    Age=24
obj=son()
print("FATHER NAME IS:",obj.F_name)
print("FATHER AGE IS:",obj.Age)
print("SON NAME IS:",obj.Son_name)
print("FATHER AGE IS:",obj.Age)
