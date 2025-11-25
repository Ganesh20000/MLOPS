class Emp:

    __user_id = 0   # static variable

    def __init__(self):
        self.__name = "default user"

        # static counter
        self.id = Emp.__user_id
        Emp.__user_id += 1

        # non-static → resets every object
        self.user = 1

        self.salary = 20000
        self.designation = "AIML"

    def travel(self, designation):
        print(f"sam is going to {designation}")


# testing
E = Emp()
G = Emp()
O = Emp()

print(E.id)  # 0
print(G.id)  # 1
print(O.id)  # 2
