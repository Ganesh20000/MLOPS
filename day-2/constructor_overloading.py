# class  Animal:

#     def __init__(self,name):
#         self.name=name

#     def speak(self):
#         print(f" {self.name} makes a sound")


# class DOG(Animal):

#     def speak(self):
#         print(f"{self.name} is very good pet")





# an =Animal("dog")

# an.speak()


# d=DOG("jemmie")
# d.speak()


print("_"*100)


#! constructor overloading example


class  Animal:

    def __init__(self,name):
        self.name=name

    def speak(self):
        print(f" {self.name} makes a sound")


class DOG(Animal):


    def __init__(self):
        self.behaviour="friendly "

    def speak(self):
        print(f" rocky is very {self.behaviour}")





# an =Animal("dog")

# an.speak()


d=DOG()
d.speak()
