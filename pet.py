#git clone
"""
Introduction to Classes and Object-Oriented Programming (OOP) in Python
"""

# ------------------------------------------------------------
# Define a class
# ------------------------------------------------------------

class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am a {self.species}.")


# ------------------------------------------------------------
# Create instances of the class
# ------------------------------------------------------------

dog = Pet("Buddy", "Dog")
cat = Pet("Whiskers", "Cat")


# ------------------------------------------------------------
# Access attributes of the instances
# ------------------------------------------------------------

print(dog.name)      # Output: Buddy
print(dog.species)   # Output: Dog

# Call methods
dog.introduce()
cat.introduce()
