# Области видимости функций, пространства имен класса
 
### Общая (без декораторов)

> Методы, способные использовать атрибуты класса, атрибуты экземпляра класса и внешние переменные

Своеобразная "настройка по-умолчанию", с ней мы имеем дело всегда, когда не указываем каких-либо декораторов

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def get_coordinates(self):
        return self.x, self.y

v =  Vector(1, 2)
# можем получить координаты при помощи метода, унаследованного от класса
result = v.get_coordinates()
# или обратиться к созданному классу и в качестве аргумента `self` передать созданный экземпляр класса Vector
result1 = Vector.get_coordinates(v)

print(result, result1, sep='\n') # Видим, что результат идентичен
```

### Метод класса - `@classmethod`

> Методы, способные использовать только атрибуты класса и внешние переменные

Методы для использования внутри класса, доступ из объектов класса не подразумевается.

```python
class Vector:
    MIN = 0
    MAX = 100

    @classmethod
    def validate(cls, arg):
        return cls.MIN <= arg <= cls.MAX

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y
        else:
            print(f"Incorrect input. Created object has coordinates ({self.x}, {self.y})")

    def get_coordinates(self):
        return self.x, self.y


v = Vector(1, 2)

result = v.get_coordinates()            # можем получить координаты при помощи метода, унаследованного от класса
result1 = Vector.get_coordinates(v)     # или обратиться к созданному классу и в качестве аргумента `self` передать 
                                        # созданный экземпляр класса Vector
print("result", result, 
      "result1", result1, sep="\n")     # Видим, что результат идентичен

v_wrong = Vector(1, 200)                # для тестирования метода класса validate создадим еще экземпляр Vector
print("v_wrong", 
      v_wrong.get_coordinates(), 
      sep="\n")                         # в результате были установлены значения по умолчанию (0, 0)

```

### Статичный метод - `@staticmethod`

> Методы, не имеющие доступа ни к чему, кроме явно переданных им аргументов.

Могут быть полезны для сохранения каких-либо сервисных методов, связанных с классом скорее логически, 
чем хранимыми атрибутами 

```python
class Vector:
    MIN = 0
    MAX = 100
    
    @staticmethod
    def norm2(x, y):
        return x**2 + y**2
    
    @classmethod
    def validate(cls, arg):
        return cls.MIN <= arg <= cls.MAX

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y
        else:
            print(f"Incorrect input. Created object has coordinates ({self.x}, {self.y})")

    def get_coordinates(self):
        return self.x, self.y


v = Vector(1, 2)

result = v.get_coordinates()            # можем получить координаты при помощи метода, унаследованного от класса
result1 = Vector.get_coordinates(v)     # или обратиться к созданному классу и в качестве аргумента `self` передать 
                                        # созданный экземпляр класса Vector
print("result", result, 
      "result1", result1, sep="\n")     # Видим, что результат идентичен

v_wrong = Vector(1, 200)                # для тестирования метода класса validate создадим еще экземпляр Vector
print("v_wrong", 
      v_wrong.get_coordinates(), 
      sep="\n")                         # в результате были установлены значения по умолчанию (0, 0)

print("Vector.norm2 to (5, 6) is ", 
      Vector.norm2(5, 6))               # вызов статичного метода для расчета требуемого показателя 
```

##### Можно ли передать методам недоступные им атрибуты?
> Да, но это плохо. Не делайте так. Серьезно.

## Итоги по декораторам `@staticmethod` и `@classmethod`

- `without @...`  - могут использовать атрибуты объекта, класса и принимать внешние атрибуты
```python
def __init__(self, x, y): ...
```
```python
def get_coord(self): ...
```
- `@classmethod`  - могут использовать атрибуты класса и принимать внешние атрибуты
```python
@classmethod
def validate(cls, arg):
```
- `@staticmethod` - могут использовать только внешние атрибуты
```python
@staticmethod
def norm2(x, y): ... 
```