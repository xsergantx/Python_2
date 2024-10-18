class House:
    def __init__ (self, name, number_of_floors):
        self.name = name # имя
        self.number_of_floors = number_of_floors # кол-во этажей

    def go_to(self, new_floor):
        if 0 < new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
            else:
             print("Такого этажа не существует")

    def __len__ (self):
        return self.number_of_floors

    def __str__(self):
        print(f'Название:{self.name}, кол-во этажей: {self.number_of_floors}')



h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
