from datetime import datetime

class Employee:
    def __init__(self, id, name, surname, date_of_birth, salary, position):
        self.id = id
        self.name = name
        self.surname = surname
        self.date_of_birth = datetime.strptime(date_of_birth, "%d-%m-%Y")
        self.salary = salary
        self.position = position

    def introduce_employee(self):
        print(f"Hi, I am {self.name} {self.surname}")

    def get_age(self):
        today = datetime.today()
        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age

    def get_hourly_rate(self):
        mph = self.salary/160
        return  str(mph) + " zł"


employee = Employee(1, "Jan", "Kowalski", "01-01-1990", 10000, "Engineer")
# employee.introduce_employee()
# print(employee.get_age())
# print(employee.get_hourly_rate())


class Enemy:
    def __init__(self, name, health_points, atack_damage, atack_speed):
        self.name = name
        self.health_points = health_points
        self.atack_damage = atack_damage
        self.atack_speed = atack_speed

    def atack(self, opponent_hp):
        opponent_hp -= self.atack_damage
        return opponent_hp

    def defence(self, opponent_ad):
        self.health_points -= opponent_ad
        return self.health_points

    def demage_per_time(self, time):
        return  self.atack_speed * time * self.atack_damage

enemy = Enemy("Enemy1", 100, 5, 1.23)
# print(enemy.atack(50))
# print(enemy.defence(15))
# print(enemy.demage_per_time(10))

class Fridge: #aggregation
    def __init__(self, brand, model, temperature, total_products):
        self.brand = brand
        self.model = model
        self.temperature = temperature
        self.products= []
        self.total_products = total_products

    def set_temperature(self, new_temperature):
        self.temperature = new_temperature
        print(f"Temperature set on {self.temperature} degrees")

    def add_product(self, product):
        self.products.append(product)
        print(f"Product {product} added!")

    def delete_product(self, product):
        if product in self.products:
            self.products.remove(product)
            print(f"Product delated: {product}")
        else:
            print("Product not found in fridge")


# my_fridge.set_temperature(6)
# my_fridge.add_product("Milk")
# my_fridge.delete_product("Milk")
# my_fridge.delete_product("Meat")

class Products:
    def __init__(self, products, quantity):
        self.products = products
        self.quantity = quantity

prod = Products(4, 20)
my_fridge = Fridge("Samsung", "ABC123", 4, prod)

print("Products:", my_fridge.total_products.products)



