class Demo:
    print("class method")
    d=50
    def add(self,a,b):
        c=a+b+self.d
        print (c)
obj1=Demo()
obj1.add(10,20)
