class Turtle:
    def __init__(self, name, speed, x = 0):
        self.name  = name
        self.speed = speed
        self.x = x

    def say_name(self):
        print(f"My name is {self.name} and my speed is {self.speed}")

    def move(self, distance):
        self.x = self.x + distance

    def get_position(self):
        return self.x

zulf = Turtle("Rzułf", 10)

zulf.say_name()
zulf.move(10)
print(zulf.get_position())