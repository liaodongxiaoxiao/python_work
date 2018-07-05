class Dog():
    """docstring for ClassName"""
    def __init__(self, name,age):
        self.name = name
        self.age = age
		
    def sit(self):
        """pass"""
        print(self.name.title()+" is now sitting.")

    def roll_over(self):
        """"""
        print(self.name.title()+" is rolled over!")

my_dog = Dog('dahuang',3)
print("My dog's name is "+ my_dog.name.title())
print("My dog is "+str(my_dog.age)+" years old.")
my_dog.sit()
my_dog.roll_over()