import os
from temperature import Temperature

class Calorie:
    """
    Represents optimal calorie amount 
    per person needs to take today.
    """
    
    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature
    
    def calculate(self):
        result = 10 * self.weight + 6.5 * self.height - self.temperature * 10
        return result

if __name__ == '__main__':
    temperature = Temperature(country="croatia", city="zagreb").get()
    calorie = Calorie(weight=100, height=192, age=41, temperature=temperature)
    os.system("cls")
    print(calorie.calculate())