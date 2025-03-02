class Point:
    """Класс для представления координат точек на плоскости"""
    color = 'red'
    circle = 2

print(Point.__doc__)

# Создание экземпляров класса
a = Point()
b = Point()

# все экземпляры класса наследуют instance (тип):
print(type(a))
print(type(b) == Point)
print(isinstance(a, Point), end='\n\n')

# Объект может не содержать в себе локальных атрибутов
print(a.__dict__)
# но иметь возможность обращаться к атрибутам класса
print(a.color, end='\n\n')

# При этом нам доступно создание локальных атрибутов с такими же названиями
a.color = "green"
print(a.color, end='\n\n')

# В то же время прочие экземпляры того же класса продолжают ссылаться на атрибут родительского класса
print(b.color)
print(Point.color)

# Также мы можем создавать новые атрибуты (свойства)
Point.type_pt = 'disc'
print(a.__dict__)
print(a.type_pt)
print(Point.__dict__)

# Другой способ взаимодействия с атрибутами класса и объектов класса
setattr(Point, 'prop', 1)                   # `setattr` устанавливает значение атрибута `prop` равным 1, если такого атрибута не существовало - создает и устанавливает
setattr(Point, 'type_pt', 'square')
print(Point.prop)
print(Point.type_pt)

# При обращении к несуществующему атрибуту - получаем ошибку
print(Point.a)

print(getattr(Point, 'a', False))
print(getattr(Point, 'color', False))

# Удаление атрибутов
del Point.prop
# del Point.prop                # здесь происходит ошибка, т.к. уже не существует такого атрибута
del a.color                   # удаление локального атрибута

print(a.color)
print(a.__dict__)

delattr(Point, 'type_pt')     # удалить можно только существующий атрибут

# Проверка наличия атрибута
hasattr(Point, 'prop')

hasattr(a, 'circle')          # вовсе не значит что именно у этого экземпляра есть такой атрибут
print(a.__dict__)


# заново создадим объекты класса Point
a = Point()
b = Point()

# создание локальных атрибутов
a.x = 1
a.y = 2
b.x = 10
b.y = 20