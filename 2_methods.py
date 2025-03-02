class Point:
    """Класс для представления координат точек на плоскости"""
    color = 'red'
    circle = 2

    def set_coordinates(self, x, y):
        """Задать координаты точки"""
        self.x = x
        self.y = y

    def get_coordinates(self):
        """Получить координаты точки"""
        return self.x, self.y

# создадим экземпляр класса Point
pt = Point()
pt.set_coordinates(1, 2)
print(pt.__dict__)

pt2 = Point()
pt2.set_coordinates(10, 20)
print(pt2.__dict__)

print('pt coordinates', pt.get_coordinates())
print('pt2 coordinates', pt2.get_coordinates())

# использование getattr и setattr
f = getattr(pt, 'get_coordinates')       # создали объект, хранящий функцию
print(f())                               # вызвали эту функцию

