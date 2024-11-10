class Vehicle:
    __COLOR_VARIANTS = ['Аустер', 'Гейзер', 'Индиго', '	Лагуна', 'Лазурь']

    def __init__(self, owner: str, __model: str, __engine_power: int, __color: str):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self):
        return f'{self.__model}'

    def get_horsepower(self):
        return f'{self.__engine_power}'

    def get_color(self):
        return f'{self.__color}'

    def print_info(self):
        print(f'Модель: {self.get_model()}')
        print(f'Мощность двигателя: {self.get_horsepower()}')
        print(f'Цвет: {self.get_color()}')
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color: str):
        new_color = new_color
        if new_color in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')
# Изначальные свойства
vehicle1.print_info()
# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('Индиго')
vehicle1.owner = 'Vasyok'
# Проверяем что поменялось
vehicle1.print_info()
