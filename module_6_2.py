class Vehicle:          #любой транспорт
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def __init__(self, owner: str, model: str, color='white', engine_power=1000):#в скобках атрибуты
        self.owner = owner#владелец
        self.__model = model#модель
        self.__engine_power = engine_power #мощность двигателя
        self.__color = color#цвет

    def get_model (self): #метод
        return f'Модель: {self.__model}'

    def get_horsepower (self):#метод
        return f'Мощность: {self.__engine_power}'

    def get_color (self,):#метод
        return  f'Цвет: {self.__color}'

    def print_info (self):#метод
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color (self, new_color: str):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'\033[91mНельзя сменить цвет на {new_color}\033[0m')



class Sedan(Vehicle):  #седан
    __PASSENGERS_LIMIT = 5 #в седан может поместиться только 5 пассажиров

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
