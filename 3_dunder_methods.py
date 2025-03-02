class Point:
    color = 'red'
    circle = 2

    def __init__(self, x=0, y=0):
        """Инициализатор объекта класса - выполняется в момент создания объекта"""
        print('Call __init__ method' + str(self))
        self.x = x
        self.y = y

    def __del__(self):
        """Финализатор класса - выполняется перед удалением объекта сборщиком мусора.
        Удаление объектов осуществляется в момент, когда на объект не ведет больше ни одной ссылки"""
        print('Call __del__ method: ' + str(self))

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_coordinates(self):
        return self.x, self.y

print('check __init__')

pt = Point(1, 2)
print(pt.__dict__, end='\n' + '-' * 80 + '\n')


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

print(id(db) == id(db2))  # ссылаемся на один и тот же объект

# есть и недостаток - значения атрибутов,
# передаваемых при попытке создания нового объекта переписали собой атрибуты обоих объектов класса

db.connect()

db2.connect()
print('\n' + '-' * 80 + '\n')


class Point_new:
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
        """Метод, автоматически вызываемый в момент создания и/или изменения атрибута `key`
        """
        if key == 'z':
            raise AttributeError('Недопустимое имя атрибута')
        else:
            object.__setattr__(self, key, value)

    def __getattr__(self, item):
        """Метод, автоматически вызываемый при получении несуществующего свойства
        """
        print('__getattr__: ' + item)

    def __delattr__(self, item):
        """Метод, автоматически вызываемый при получении несуществующего свойства
        """
        print('__delattr__: ' + item)
        object.__delattr__(self, item)

# create Point_new objects
pt1 = Point_new(1, 2)
pt2 = Point_new(10, 20)

# check __getattribute__
# a = pt1.x
# b = pt1.y
# print(a, b, sep='\n')

# check __setattr__
# pt1.z = 5

# check __getattr__
print(pt1.yy)

# check __delattr__
del pt1.x
print(pt1.__dict__, end='\n' + '-' * 80 + '\n')