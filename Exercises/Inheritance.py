class Bird:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        print(f"This is {self.name}, it is {self.age} years old")

class PredatorBird(Bird):
    def __init__(self, name, age, beak_len, wingspan):
        super().__init__(name, age)
        self.beak_len = beak_len
        self.wingspan = wingspan

    def hunting(self):
        return f"{self.name} soars high into the air, searching for prey."


class Eagle(PredatorBird):
    def __init__(self, name, age, beak_len, wingspan, nest_size):
        super().__init__(name, age, beak_len, wingspan)
        self.nest_size = nest_size

    def represent(self):
        return f"The eagle is a symbol of power and strength. Its nest is {self.nest_size} cm."

# eagle = Eagle("Bald Eagle", 8, 15, 200, 100)
# eagle.describe()
# print(eagle.hunting())
# print(eagle.represent())


class Character:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.health = 100

    def introduce(self):
        print(f"I am {self.name}, level {self.level}, and I have {self.health} health points.")

class Warrior(Character):
    def __init__(self, name, level, strength, agility):
        super().__init__(name, level)
        self.strength = strength
        self.agility = agility

    def attack(self):
        return f"{self.name} performs a strong attack!"

    def defense(self):
        return f"{self.name} prepares for defense!"

class Knight(Warrior):
    def __init__(self, name, level, strength, agility, armor):
        super().__init__(name, level, strength, agility)
        self.armor = armor

    def present(self):
        print(f"I am {self.name}, a knight at level {self.level}. I have {self.armor} armor points.")


knight = Knight("Arthur", 10, 90, 70, 100)
knight.introduce()
knight.present()
