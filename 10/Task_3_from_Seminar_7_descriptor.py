""" Реализовать базовый класс Worker (работник), в котором определить атрибуты:
 name, surname, position (должность), income (доход). Последний атрибут должен
 быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
 например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность)
  на базе класса Worker. В классе Position реализовать методы получения полного
имени сотрудника (get_full_name) и дохода с учетом премии
(get_total_income). Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения
 атрибутов, вызвать методы экземпляров)."""


class Not_Negativ:
    def __init__(self, attrib):
        self.attr = attrib

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('!Значение оклада не может быть отрицательным!')
        instance.__dict__[self.attr] = value


class Worker():
    income = Not_Negativ('income')
    _income = {}

    def __init__(self, name, surname, position, wage=50000, bonus=0):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = wage
        self._income["wage"] = self.income
        self._income["bonus"] = bonus


class Position(Worker):
    def get_full_name(self):
        print(f'{self.name}  {self.surname}')

    def get_total_income(self):
        print(f"Доход :{self._income['wage'] + self._income['bonus']}")


"""Для проверки задаем отрицательное значение: - 40 000 """

d = Position('Александр', 'Кияткин', 'Водитель', -40000, 5000)
d.get_full_name()
d.get_total_income()

d1 = Position('Виктор', 'Иванов', 'Бухгалтер', 30000, 5000)
d1.get_full_name()
d1.get_total_income()

d3 = Position('Петр', 'Сидоров', 'Рабочий')
d3.get_full_name()
d3.get_total_income()
print(d.__dict__)
print(d1.__dict__)
