# Методы классов

Как было сказано ранее, класс имеет:
- свойства (данные)
- методы (действия)

В данном уроке мы говорим о простых методах классов, их создании, назначении аргумента `self` 
и манипуляциях с атрибутами и их значениями

### Создание простого метода
> Рекомендуется называть методы с глаголом в начале (set_..., get_...)
```python
class Point:
    color = 'red'
    circle = 2
    
    def set_coordinates():
        print('Call set_coordinates method')
    
print(Point.set_coordinates)                     # обращение к методу без его вызова 

Point.set_coordinates()


# создадим экземпляр класса Point
pt = Point()

print(pt.set_coordinates)

pt.set_coordinates()                             # вызовет ошибку - не передан параметр self
```

### Причина ошибки - в отсутствии параметра `self`, являющегося ссылкой на экземпляр класса `Point`
Так никакой ошибки не возникает
```python
class Point:
    color = 'red'
    circle = 2
    
    def set_coordinates(self):
        print('Call set_coordinates method known as: \n \t' + str(self))

# создадим экземпляр класса Point
pt = Point()
pt.set_coordinates()

Point.set_coordinates()                     # вызовет ошибку - т.к. нет экземпляра класса

Point.set_coordinates(pt)                   # ошибки не возникло, т.к. был явно передан экземпляр класса
```

### Зачем вообще все это нужно?
Для передачи аттрибутов экземплярам класса - без него не указано какому экземпляру нужно присвоить значения атрибутов
```python
class Point:
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
f = getattr(pt, 'get_coordinates')                  # создали объект, хранящий функцию 
print(f())                                          # вызвали эту функцию
```
Таким образом, мы получили возможность присвоить какие-либо атрибуты экземплярам класса

Кроме того, важно отметить, что фактически, методы класса являются такими же атрибутами, но ведут они не к данным, а к функциям

