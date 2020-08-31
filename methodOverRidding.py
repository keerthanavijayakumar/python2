class Employee1():
    def epersonal_detais(self):
        empId=1143
        empName="ravi"
        empAge=48
        empaddress=chennai
    def eofficial_details(self):
        AddharNo=65326611018
        panNo=Hc233J2
        voterID=232424235
class employeeoverRiding(Employee1):
    def epersonal_detais(self):
        print("empId:1143")
        print("empName:ravi")
        print("empAge:52")
        print("empaddress:selam")
    def eofficial_details(self):
        print("AddharNo=65326611018")
        print("panNo=Hc233J2")
        print("voterID=232424235")

obj=employeeoverRiding()
obj.epersonal_detais()
obj.eofficial_details()
