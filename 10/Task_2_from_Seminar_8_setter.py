class Cell():
    def __init__(self, quantity):
        if quantity < 0:
            raise ValueError('количество не может быть отрицательным!')
        self._quantity = quantity

    def __add__(self, other):
        return Cell(self._quantity + other._quantity)

    def __sub__(self, other):
        if self._quantity < other._quantity:
            print("Разность отрицательна, поэтому операция не выполняется")
            pass
        else:
            return Cell(self._quantity - other._quantity)

    def __mul__(self, other):
        return Cell(self._quantity * other._quantity)

    def __truediv__(self, other):
        return Cell(int(self._quantity / other._quantity))

    def __str__(self):
        return f"{self._quantity}"

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError("! < 0, не может быть отрицательным")
        self._quantity = value


d1 = Cell(20)
d2 = Cell(10)
d3 = Cell(30)
d4 = Cell(60)

"""Для проверки можно задать отрицательное значение"""

d1.quantity = 30
print(f"Создаем объекты клеток {d1.quantity}, {d2.quantity}, {d3.quantity}, "
      f" {d4.quantity}")
result = d1 + d2
print(f"Складываем {d1} и {d2} :{result.quantity}")
print(f"Вычитаем {d1} и {d3} : {d1 - d3}")
print(f"Вычитаем {d3} и {d1} : {d3 - d1}")
print(f"Умножаем {d1} и {d3} :{d3 * d1}")
print(f"Делим {d4} и {d3} :{d4 / d3}")
print(f"Делим {d3} и {d1} :{d3 / d1}")
