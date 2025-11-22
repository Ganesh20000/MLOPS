class EMPLOYEE:

    def __init__(self):
        self.id=200
        self.name='suresh'
        self.salary=20000
        self.designation='AIML'
        print("first one")

    def travel(self,designation):
        print("second one")
        print(f" sam is goint to , {designation}")


    


emp=EMPLOYEE()
# print(emp.id)
# print(emp.name)
# print(emp.designation)


emp.travel("goa")