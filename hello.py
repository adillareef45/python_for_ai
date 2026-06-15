class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating!"
    
    def run(self):
        return f"{self.name} is running!"
    
    def jump(self):
        return f"{self.name} is jumping!"

class Dog(Animal):
    def bark(self):
        return f"{self.name} is barking!"
    
class Wolf(Dog):
    def howl(self):
        return f"{self.name} is howling!"
    

jerry = Dog(name="Jerry")
jerry.bark()
jerry.run()

diasy = Wolf(name="Diasy")
diasy.bark()
diasy.howl()