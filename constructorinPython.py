class constructor():
    print("WELCOME TO PASS VALUE CONSTRUCTOR")
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("I am :",self.name)
        print("My age is:",self.age)

obj=constructor("keerthana",22)
obj.display()



class constructor2():
    print("WELCOME TO CONSTRUCTOR")
    def __init__(self):
        self.name="MUTHU"
        self.age=21
    def display(self):
        print("I am :",self.name)
        print("My age is:",self.age)

obj=constructor2()
obj.display()
