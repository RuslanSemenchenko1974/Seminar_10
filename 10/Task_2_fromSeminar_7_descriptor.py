"""Реализовать класс Road (дорога), в котором определить атрибуты: length
(длина), width (ширина). Значения данных атрибутов должны передаваться при
создании экземпляра класса. Атрибуты сделать защищенными. Определить метод
 расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
  Использовать формулу: длинаширинамасса асфальта для покрытия одного кв метра
   дороги асфальтом, толщиной в 1 см*число см толщины полотна. Проверить
   работу метода."""


class Not_Negativ:
    def __init__(self, attrib):
        self.attr = attrib

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('!Значение не может быть отрицательным!')
        instance.__dict__[self.attr] = value


class Road:
    _length = Not_Negativ('_length')
    _width = Not_Negativ('_width')

    def __init__(self, a=1, b=1):
        self._length = a
        self._width = b

    def mass_ashpalt(self, thickness=1):
        print(f'Масса асфальта при толщине {thickness} см : '
              f'{self._length * self._width * thickness * 25} кг')


"""Для проверки задаем отрицательное значение: - 100 """
d = Road(-100, 10)

d.mass_ashpalt(5)
d.mass_ashpalt()
