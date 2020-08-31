class gfather():#base class
    gf_name="Subramaniyam"
    Age=88
class father(gfather):# child class &base class of son
     F_name="vijaya kumar"
     Age=48
class son(father):#child class
    Son_name="vignesh"
    Age=24
obj=son()
print("GRAND FATHER NAME IS:",obj.gf_name)
print("GRAND FATHER AGE IS:",obj.Age)
print("FATHER NAME IS:",obj.F_name)
print("FATHER AGE IS:",obj.Age)
print("SON NAME IS:",obj.Son_name)
print("SON AGE IS:",obj.Age)
