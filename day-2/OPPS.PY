






class Emp:

    #! apply static method

    __user_id=0

    def __init__(self):
        #? encapsulation
        self.__name = "default user"

        # self.id=Emp.__user_id
        # Emp.__user_id +=1


    

# 
        # self.user=0
        # self.user+=1
        self.idd=200
        self.names='suresh'
        self.salary=20000
        self.designation='AIML'
        # print("first one")
    
    @staticmethod

    def get_method():
        return Emp.__user_id


    @staticmethod
    def set_method(value):
        Emp.__user_id=value

    def travel(self,designation):
        # print("second one")
        print(f" sam is goint to , {designation}")


    

emp=Emp()
# print(emp.id)
# print(emp.name)
# print(emp.designation)


emp.travel("goa")