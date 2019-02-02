from abc import ABC, abstractmethod

class Animal(ABC):
    color = 'black'
    voice = 'Oyy'
    full_state = ''
  
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def get_voice(self):
        print(self.voice)
    
    @abstractmethod
    def feed(self):
        pass
    
    @abstractmethod
    def collect(self):
        pass

        
class Bird(Animal):
    eggs_count = 0 # шт.
    eggs_limit = 1 # шт.
    full_state = 'hungry'
    
#     def egg_collection(self, eggs):
#         if eggs > self.eggs_limit:
#             self.eggs_count = self.eggs_limit
#         else:
#             self.eggs_count = eggs
    
    def feed(self):
        print(f"{self.name} was fed with grain")
        self.state = 'full'
        
    def collect(self):
        print(f"Egg is collected from {self.name}")
            
            
class Goose(Bird):
    voice = 'Honk! Honk!'
    
    
class Chicken(Bird):
    eggs_limit = 2 # шт.
    voice = 'Cluck! Cluck! Cluck!'

    
class Duck(Bird):
    voice = 'Quack! Quack!'

    
class Cow(Animal):
    voice = 'Moooo!'
    milk_limit = 30 #л
    full_state = 'hungry'
    
#     def get_milk(self, milk):
#         if milk > self.milk_limit:
#             print(f'Было надоено {milk_limit} л. молока ')
#             self.milk_limit = 0
#         else:
#             self.milk_limit = self.milk_limit - milk
#             print(f'Было надоено {milk} л. молока ')
            
    def feed(self):
        print(f"{self.name} was fed with grass")
        self.state = 'full'
        
    def collect(self):
        print(f"Milk is collected from {self.name}")
    
class Goat(Cow):
    voice = 'Baaa!'
    milk_limit = 3 #л

    
class Sheep(Animal):
    voice = 'Beee!'
    wool_limit = 12 #kg
    full_state = 'hungry'
    
#     def get_wool(self, wool):
#         if wool > self.wool_limit:
#             print(f'Было сострижено {wool_limit} кг. шерсти ')
#             self.wool_limit = 0
#         else:
#             self.wool_limit = self.wool_limit - wool
#             print(f'Было сострижено {wool} кг. шерсти ')
    
    def feed(self):
        print(f"{self.name} was fed with forage")
        self.state = 'full'
        
    def collect(self):
        print(f"Wool is collected from {self.name}")
        
# Задача 2
goose_0 = Goose('Серый', 6)
goose_0.get_voice()
# print(goose_0.full_state)
# goose_0.feed()
# print(goose_0.full_state)
goose_1 = Goose('Белый', 7)
cow_0 = Cow('Манька', 500)
# print(cow_0.milk_limit)
# cow_0.get_milk(12)
# print(cow_0.milk_limit)
sheep_0 = Sheep('Барашек', 80)
sheep_1 = Sheep('Кудрявый', 100)
chicken_0 = Chicken('Ко-Ко', 2)
# print(f'В день курица несет {chicken_0.eggs_limit} яйца')
chicken_1 = Chicken('Кукареку', 1.5)
goat_0 = Goat('Рога', 60)
goat_1 = Goat('Копыта', 70)
# print(goat_1.milk_limit)
# goat_1.get_milk(1)
# goat_1.get_voice()
# print(goat_1.milk_limit)
duck_0 = Duck('Кряква', 4)

# Задача 3
list = [goose_0, goose_1, cow_0, sheep_0, sheep_1, chicken_0, chicken_1, goat_0, goat_1, duck_0]
max_weight = 0
bigger_animal = ''
weight_of_all = 0
for animal in list:
    weight_of_all += animal.weight
    if animal.weight > max_weight:
        max_weight = animal.weight
        bigger_animal = animal.name
print(f'Общий вес всех животных на ферме составил {weight_of_all} кг.')
print(f'Самое тяжелое животное : "{bigger_animal}" (вес {max_weight} кг.)')

# Накормим всех животных

for animal in list:
  animal.feed()
  animal.collect()
