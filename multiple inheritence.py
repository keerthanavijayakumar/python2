class father():#base class
    F_name="vijaya kumar"
    Age=48
class mother():# base class 
     M_name="rani"
     Age=48
class son(father,mother):#child class
    Son_name="vignesh"
    Age=24
obj=son()
print(" FATHER NAME IS:",obj.F_name)
print(" FATHER AGE IS:",obj.Age)
print("MOTHER NAME IS:",obj.M_name)
print("MOTHER AGE IS:",obj.Age)
print("SON NAME IS:",obj.Son_name)
print("SON AGE IS:",obj.Age)
