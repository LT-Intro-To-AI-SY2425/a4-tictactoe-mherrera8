# object oriented programming

# (define-struct dog [fur_color name age favorite_food])

class Dog:
    species = "canis familiaris"
    def __init__(self, name = "no name", age = 0):
        self.name = name
        self.age = age 
        self.fetch_count = 0 
    def __str__(self):
        s = f"{self.name} is {self.age} years old"
        return s  
    def play_fetch(self, num_fetch):
        self.fetch_count += num_fetch

logan = Dog("logan", 8)
becker = Dog("becker", 4)
kepa = Dog("kepa", 4)