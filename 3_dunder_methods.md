# Инициализатор и финализатор

[py-file](3_dunder_methods.py)

Магические методы - `__имя__` (double underscore methods - dunder-methods)

1. `__new__()` - вызывается перед созданием объекта класса
1. `__init__(self)` - инициализатор объекта класса - вызывается сразу после создания объекта класса
1. `__del__(self)` - финализатор класса - выполняется перед удалением объекта сборщиком мусора

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