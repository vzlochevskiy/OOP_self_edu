Конспекты уроков по курсу [Сергея Балакирева](www.youtube.com/@selfedu_rus) 

[youtube playlist](https://www.youtube.com/playlist?list=PLA0M1Bcd0w8zPwP7t-FgwONhZOHt9rz9E)

[курс по ООП на stepik](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbEpZdWwwTzVVc3JFcm1TblRwV2k0Y1YyVTF0QXxBQ3Jtc0tuR2FtUWNPRXQzaUhkYzl0dFpmR0xobWhtZzBNcnM2WkpWVmJGRlJmWVh1Y1NYX2MtYmM1REp0eVZtaXMyaTV4LUtua3pFQU9BRFBwT2xNV0JkM0RsRHZBb3FUdXZQVk03TXAtQURHT0N0di1VeDJrUQ&q=https%3A%2F%2Fstepik.org%2Fa%2F116336&v=Z7AY41tE-3U)

# Концепция ООП

> ООП - объектно-ориентированное программирование

## Классы и объекты классов
Класс - инструкция к объекту (шаблон) - Коты как вид\
Объект класса - экземпляр 

## Атрибуты и методы
Атрибут - свойство объекта, данные об объекте\
Метод - функция, определенная для объекта класса, выполнение действия с объектом

[**Определение класса, создание объектов, добавление и удаление атрибутов**](1_attributes.md#классы-и-объекты-классов-атрибуты-и-методы)

- `getattr(obj, name[, default])` - возвращает значение атрибута объекта;
- `hasattr(obj, name)` - проверяет наличие атрибута
- `setattr(obj, name, value)` - задает значение атрибута (если атрибут не существует - он создается)
- `delattr(obj, name)` - удаляет атрибут с именем name

- `__doc__` - содержит строку с описанием класса;
- `__dict__` - содержит набор атрибутов экземпляра класса

[**Методы классов, параметр `self`, манипуляции с атрибутами**](2_methods.md#создание-простого-метода)

**Магические методы - double-underscored (dunder-methods)**\
- [`__init__, _del__`](3_dunder_methods.md#инициализатор-и-финализатор)
- [`__new__`](3_dunder_methods.md#реализация-паттерна-singleton)

### Области видимости методов классов. Декораторы `@classmethod` и `@staticmethod`
[py-file](4_classmethod_staticmethod.py)

- `not_decorated`  - могут использовать атрибуты объекта, класса и принимать внешние атрибуты
    ```python
      def __init__(self, x, y): ...
    ```
    ```python
      def get_coord(self): ...
    ```
    [Подробнее](4_classmethod_staticmethod.md#общая-без-декораторов)

- `@classmethod`  - могут использовать атрибуты класса и принимать внешние атрибуты
    ```python
        @classmethod
        def validate(cls, arg):
    ```
    [Подробнее](4_classmethod_staticmethod.md#метод-класса---classmethod)


- `@staticmethod` - могут использовать только внешние атрибуты
    ```python
    @staticmethod
    def norm2(x, y): ... 
    ```
    [Подробнее](4_classmethod_staticmethod.md#статичный-метод---staticmethod)

## Инкапсуляция
> Инкапсуляция - сокрытие деталей реализации класса, абстракция. Определение разрешенных методов и свойств

### Механизмы инкапсуляции
[py-file](5_encapsulation.py)
- `attribute` (без подчеркиваний в начале названия) - публичное свойство `public`
- `_attribute` (одно подчеркивание в начала названия) \
режим доступа `protected` (служит для обращения внутри класса и во всех его дочерних классах)
- `__attribute` (два подчеркивания) \
режим доступа `private` (служит для обращения только внутри класса)
- модуль `accessify` для защиты чувствительных данных

[Подробнее](5_encapsulation.md)

## Наследование
> Определение свойств, единых для дочерних классов, в родительском классе во избежание дублирования кода



## Полиморфизм
> Возможность через единый интерфейс работать с объектами разных классов


