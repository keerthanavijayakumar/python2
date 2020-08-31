class overloading():
    def multiplyTwovalue(self):
        print("No values found in this class")
    def multiplyTwovalue(self,a,b):
        c=a*b
        print(c)   #It gives error  python consider the last def fun only so it will produces the error
obj=overloading()                              
#obj.multiplyTwovalue()                          
obj.multiplyTwovalue(10,20)
        


#second program for overloading

class divition():
    def divide(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            c=a+b+c
            print(c)
        elif a!=None and b!=None:
            c=a+b
            print(c)
        else:
            c=a
            print(c)
obj=divition()
obj.divide(12,12)
        
        
    
