##

#^ inheritance python code 

class Animal:

    def __init__(self,name):
        self.name=name

    def speak(self):
        print(f"{self.name} make sound")




class Dog(Animal):


    def speak(self):
        print(f"{self.name} bark")




g=Animal("animal")

g.speak()

d=Dog("charle")




d.speak()