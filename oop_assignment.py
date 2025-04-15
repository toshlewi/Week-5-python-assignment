class Animal:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")


class Bird(Animal):
    def move(self):
        print(f"{self.name} is flying! 🕊️")


class Fish(Animal):
    def move(self):
        print(f"{self.name} is swimming! 🐟")


class Snake(Animal):
    def move(self):
        print(f"{self.name} is slithering! 🐍")


class Dog(Animal):
    def move(self):
        print(f"{self.name} is running! 🐕")


class Kangaroo(Animal):
    def move(self):
        print(f"{self.name} is hopping! 🦘")


# Create a list of animals
animals = [
    Bird("Pigeon"),
    Fish("Goldie"),
    Snake("Viper"),
    Dog("Rex"),
    Kangaroo("Joey")
]

# Demonstrate polymorphism
print("\n--- Animal Movement Demonstration ---")
for animal in animals:
    animal.move()

# Extended example with more complex behavior
print("\n--- Extended Animal Behavior ---")

class Cheetah(Dog):  # Inherits from Dog but overrides move
    def move(self):
        print(f"{self.name} is sprinting at 70 mph! 🐆")
    
    def hunt(self, prey):
        print(f"{self.name} chases {prey.name}!")
        self.move()
        prey.move()


class Rabbit(Kangaroo):  # Inherits from Kangaroo
    def move(self):
        print(f"{self.name} is darting quickly! 🐇")
    
    def evade(self, predator):
        print(f"{self.name} tries to escape from {predator.name}!")
        self.move()
        predator.move()


# Create predator and prey
cheetah = Cheetah("Chester")
rabbit = Rabbit("Bugs")

# Demonstrate interaction
cheetah.hunt(rabbit)
print("---")
rabbit.evade(cheetah)