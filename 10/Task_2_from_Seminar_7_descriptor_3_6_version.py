class Not_Negativ:

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('!Значение не может быть отрицательным!')
        instance.__dict__[self.attr] = value
    def __set_name__(self, owner, attr):
        self.attr = attr

class Road:
    _length = Not_Negativ()
    _width = Not_Negativ()

    def __init__(self, a=1, b=1):
        self._length = a
        self._width = b

    def mass_ashpalt(self, thickness=1):
        print(f'Масса асфальта при толщине {thickness} см : '
              f'{self._length * self._width * thickness * 25} кг')


"""Для проверки можно задать отрицательное значение"""
d = Road(100, 10)

d.mass_ashpalt(5)
d.mass_ashpalt()