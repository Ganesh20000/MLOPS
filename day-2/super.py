
#^ super key word is used to call the parent class methods and properties in a child class.


class  Animal:

    def __init__(self):
        self.name="buddy"

    def speak(self):
        print(f" {self.name} makes a sound")


class DOG(Animal):


    def __init__(self,breed):
        super().__init__()
        self.breed=breed

    def speak(self):
        super().speak()
        print(f" rocky is  {self.breed} breed")





# an =Animal("dog")

# an.speak()


d=DOG("german shepherd")
d.speak()


# super keyword is used to call the parent class methods and properties in a child class.