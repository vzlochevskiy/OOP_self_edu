# Магические методы класса
## Инициализатор и финализатор

[py-file](3_dunder_methods.py)

Магические методы - `__имя__` (double underscore methods - dunder-methods)

1. `__init__(self)` - инициализатор объекта класса - вызывается сразу после создания объекта класса
1. `__del__(self)`  - деструктор класса - выполняется перед удалением объекта сборщиком мусора

### Но зачем?
Можно же так:
```python
class Point:
    color='red'
    circle=2

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_coordinates(self):
        return self.x, self.y

pt = Point()
pt.set_coordinates(1, 2)
print(pt.__dict__)

```

Можно, но неудобно. В данном случае нам нужно совершить 2 действия.
При использовании `__init__(self)` можно совершить всего 1 действие

```python
class Point:
    color = 'red'
    circle = 2

    def __init__(self, x=0, y=0):
        """Инициализатор объекта класса - выполняется в момент создания объекта"""
        print('call __init__ method')
        self.x = x
        self.y = y

    def __del__(self):
        """Финализатор класса - выполняется перед удалением объекта сборщиком мусора.
        Удаление объектов осуществляется в момент, когда на объект не ведет больше ни одной ссылки"""
        print('call __del__ method: ' + str(self))

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_coordinates(self):
        return self.x, self.y


pt = Point(1, 2)
print(pt.__dict__)

```

## Метод создания типа класса`__new__()` - вызывается перед созданием объекта класса

### Реализация паттерна Singleton
```python
class DataBase:
    """Реализация паттерна Singleton
    Идея заключается в ограничении возможности создания более одного экземпляра класса"""
    __instance = None

    def __new__(cls, *args, **kwargs):  # cls - ссылка на класс
        """Ссылается на текущий класс
            *args - позиционные аргументы,
            **kwargs - именованные аргументы"""
        print("Call __new__ for: " + str(cls))
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        """Финализатор класса, позволяет очистить адрес созданного объекта после его удаления"""
        DataBase.__instance = None

    def __init__(self, url, user, password, port):
        """Инициализатор объекта класса - выполняется в момент создания объекта"""
        print("call __init__ method")
        self.url = url
        self.user = user
        self.password = password
        self.port = port

    def connect(self):
        print(
            f"Success connect to DataBase: {self.url}:{self.port}@{self.user}#{'*' * len(self.password)}"
        )

    def close(self):
        print(f"Disconnect from: {self.url}:{self.port}")

    def read(self):
        print(f"Data from:: {self.url}:{self.port}")

    def write(self, data):
        print(f"Success write to: {self.url}:{self.port}", "\n", f"{data}")


db = DataBase('1.1.1.1', 'root', 'qwerty', 80)
db2 = DataBase('9.9.9.9', 'user', '123456', 70)

print(id(db) == id(db2))            # ссылаемся на один и тот же объект

# есть и недостаток - значения атрибутов, 
# передаваемых при попытке создания нового объекта переписали собой атрибуты обоих объектов класса

db.connect()

db2.connect()
```

## Доступ к атрибутам объекта: `__setattr__`, `__getattribute__`, `__getattr__` и `__delattr__`

### Изменение атрибутов класса при помощи методов класса
```python
class Point:
    MIN = 0
    MAX = 100
    def __init__(self, x=0, y=0):
        """Инициализатор объекта класса - выполняется в момент создания объекта"""
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y

    @classmethod
    def __check_value(cls, x):
        """Метод для проверки передаваемых к класс значений.
        В данный момент реализована проверка на принадлежность к классам int | float
        
        Возвращает: True or False. 
        True - значение соответствует условиям проверки, False - не соответствует. 
        """
        return isinstance(x, (int, float))

    @classmethod
    def set_bound(cls, left = cls.MIN, right = cls.MAX):
        """Метод для установки верхней и нижней границ координат создаваемых точек, экземпляров класса"""
        if cls.MIN != left or cls.MAX != right:
            cls.MIN = left
            cls.MAX = right
            print('Bounds was edited, new bounds: \n', f'left = {left}, right = {right}')

    def set_coordinates(self, x, y):
        # check values before update attributes values
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Координаты должны быть числами int or float")

    def get_coordinates(self):
        return self.__x, self.__y

pt = Point(1, 2)
print(pt.__dict__)                      # все свойства объекта
```

### При получении свойства `item` `__getattribute__(self, item)`
Пример с запретом чтения какого-либо аргумента
```python
class Point:
    MIN = 0
    MAX = 100
    def __init__(self, x=0, y=0):
        """Инициализатор объекта класса - выполняется в момент создания объекта"""
        self.x = x
        self.y = y

    def __getattribute__(self, item):
        """Метод, автоматически вызываемый в момент получения свойства класса\n
        -----------\n
        Принимает:
        `item` - название атрибута, значение которого мы хотели бы получить\n\n
        -----------\n
        Возвращает:
        Значение атрибута `item`\n\n
        """
        if item == 'x':
            raise ValueError('доступ запрещен')
        else:
            return object.__getattribute__(self, item)

pt = Point(1, 2)
pt2 = Point(10, 20)

a = pt.y
print(a)
``` 

### При создании и/или изменении свойства key класса 
`__setattr__(self, key, value)`
Пример с запретом создания или изменения какого-либо аргумента
```python
class Point:
    MIN = 0
    MAX = 100
    def __init__(self, x=0, y=0):
        """Инициализатор объекта класса - выполняется в момент создания объекта"""
        self.x = x
        self.y = y

    def __getattribute__(self, item):
        """Метод, автоматически вызываемый в момент получения свойства класса\n
        -----------\n
        Принимает:
        `item` - название атрибута, значение которого мы хотели бы получить\n\n
        -----------\n
        Возвращает:
        Значение атрибута `item`\n\n
        """
        if item == 'x':
            raise ValueError('доступ запрещен')
        else:
            return object.__getattribute__(self, item)
        
    def __setattr__(self, key, value):
        """Метод, автоматически вызываемый в момент создания и/или изменения атрибута key
        """
        if key == 'z':
            raise AttributeError('Недопустимое имя атрибута')
        else:
            object.__setattr__(self, key, value)

pt1 = Point(1, 2)
pt2 = Point(10, 20)

pt1.z = 5

```

### При получении несуществующего свойства `item`  
`__getattr__(self, item)`
```python
class Point:
    MIN = 0
    MAX = 100
    def __init__(self, x=0, y=0):
        """Инициализатор объекта класса - выполняется в момент создания объекта"""
        self.x = x
        self.y = y

    def __getattribute__(self, item):
        """Метод, автоматически вызываемый в момент получения свойства класса\n
        -----------\n
        Принимает:
        `item` - название атрибута, значение которого мы хотели бы получить\n\n
        -----------\n
        Возвращает:
        Значение атрибута `item`\n\n
        """
        if item == 'x':
            raise ValueError('доступ запрещен')
        else:
            return object.__getattribute__(self, item)
        
    def __setattr__(self, key, value):
        """Метод, автоматически вызываемый в момент создания и/или изменения атрибута key
        """
        if key == 'z':
            raise AttributeError('Недопустимое имя атрибута')
        else:
            object.__setattr__(self, key, value)
        
    def __getattr__(self, item):
        """Метод, автоматически вызываемый при получении несуществующего свойства
        """
        print('__getattr__: ' + item)

pt1 = Point(1, 2)
pt2 = Point(10, 20)

print(pt1.MAX)

```

### При удалении свойства `item` (при этом не важно, существует оно или нет)
`__delattr__(self, item)`
```python
class Point:
    MIN = 0
    MAX = 100
    def __init__(self, x=0, y=0):
        """Инициализатор объекта класса - выполняется в момент создания объекта"""
        self.x = x
        self.y = y

    def __getattribute__(self, item):
        """Метод, автоматически вызываемый в момент получения свойства класса\n
        -----------\n
        Принимает:
        `item` - название атрибута, значение которого мы хотели бы получить\n\n
        -----------\n
        Возвращает:
        Значение атрибута `item`\n\n
        """
        if item == 'x':
            raise ValueError('доступ запрещен')
        else:
            return object.__getattribute__(self, item)
        
    def __setattr__(self, key, value):
        """Метод, автоматически вызываемый в момент создания и/или изменения атрибута key
        """
        if key == 'z':
            raise AttributeError('Недопустимое имя атрибута')
        else:
            object.__setattr__(self, key, value)
        
    def __delattr__(self, item):
        """Метод, автоматически вызываемый при получении несуществующего свойства
        """
        print('__delattr__: ' + item)
        object.__delattr__(self, item)

pt1 = Point(1, 2)
pt2 = Point(10, 20)

del pt1.x
print(pt1.__dict__)

```
