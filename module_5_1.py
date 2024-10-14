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

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)

#print(h1.name, h1.number_of_floors)
#print(h2.name, h2.number_of_floors)