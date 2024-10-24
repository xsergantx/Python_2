class Animal:# животное (класс)
    alive = True # Живой (атрибут)
    fed = False # Накормленный (атрибут)
    def __init__ (self, name):
        self.name = name #имя

class Plant:# растение  (класс)
    edible = False
    def __init__ (self, name):
        self.name = name #имя


class Mammal(Animal): #Млекопитающее  (класс)
    def eat (self, food):
        if food.edible: #если  сьел съедобное
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Predator(Animal):#Хищник  (класс)
    def eat (self, food):
        if food.edible: #если  сьел съедобное
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Flower(Plant):#Цветок (класс)
    pass

class Fruit(Plant):#Фрукт (класс)
    edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')
#
print(a1.name)
print(p1.name)
#
print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.


# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.