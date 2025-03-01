from time import sleep

# Механизм инкапсуляции

> Метод ограничения доступа к атрибутам экземпляра класса

## Виды атрибутов по режиму доступа
- `attribute` (без подчеркиваний в начале названия) - публичное свойство `public`
    ```python
    class Point:
        def __init__(self, x=0, y=0):
            """Инициализатор объекта класса - выполняется в момент создания объекта"""
            self.x = x
            self.y = y
    
    
    pt = Point(1, 2)
    pt.x = 200                      # присваиваем новые значения атрибутам
    pt.y = 'y'
    print(pt.x, pt.y)               # это работает, а мы, вероятно так не хотели
    ```

- `_attribute` (одно подчеркивание в начала названия) \
режим доступа `protected` (служит для обращения внутри класса и во всех его дочерних классах)
    ```python
    class Point:
        def __init__(self, x=0, y=0):
            """Инициализатор объекта класса - выполняется в момент создания объекта"""
            self._x = x
            self._y = y
    
    
    pt = Point(1, 2)
    print(pt._x, pt._y)               # ничего не поменялось
    ```
    > Все дело в том, что данный режим доступа призван только предупредить разработчика о том, что его использование 
не рекомендуется и может привести к ошибкам 

- `__attribute` (два подчеркивания) \
режим доступа `private` (служит для обращения только внутри класса)
    ```python
    class Point:
        def __init__(self, x=0, y=0):
            """Инициализатор объекта класса - выполняется в момент создания объекта"""
            self.__x = x
            self.__y = y
  
        def set_coordinates(self, x, y):
            # check values before update attributes values
            if isinstance(x, ('int', 'float')):
                self.__x = x
                self.__y = y
            else:
                raise ValueError("Координаты должны быть числами")
  
        def get_coordinates(self):
            return self.__x, self.__y

    pt = Point(1, 2)
    print(pt.__x, pt.__y)               # получаем ошибку `AttributeError: 'Point' object has no attribute '__x'`
    
    pt.set_coordinates(10, 20)          # не получаем ошибки

    print(pt.get_coordinates())         # выводим актуальные координаты

    ```
    > Таким образом, данный режим доступа позволяет запретить прямое обращение к защищенным атрибутам

    > В свою очередь, использование методов `set_coordinates` и `get_coordinates`, позволяет без ошибок получить
    или изменить значения защищенных атрибутов 

## Cеттеры и Геттеры (`setter`, `getter`) или `Интерфейсные методы`
> Возникает вопрос: а зачем создавать какие-то дополнительные интерфейсы?
> 
> Класс в ООП следует воспринимать как единое целое и, чтобы 
> **случайно или намеренно не нарушить целостность работы алгоритма**,
> следует взаимодействовать с ним только через публичные свойства и методы.

В этом суть принципа инкапсуляции.

> *Пример про автомобиль, его органы управления и вмешательство в конструкцию двигателя*

```python
class Point:
    def __init__(self, x=0, y=0):
        """Инициализатор объекта класса - выполняется в момент создания объекта"""
        self.__x = x
        self.__y = y

    def set_coordinates(self, x, y):
        # check values before update attributes values
        if isinstance(x, (int, float)):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Координаты должны быть числами int or float")

    def get_coordinates(self):
        return self.__x, self.__y

pt = Point(1, 2)
pt.set_coordinates(10, 20)          # не получаем ошибки
print(pt.get_coordinates())         # выводим актуальные координаты

pt2 = Point()
pt2.set_coordinates('1', '2')        # получаем ошибку `ValueError: Координаты должны быть числами`
```

### Добавим приватный метод для проверки корректности координат
```python
class Point:
    def __init__(self, x=0, y=0):
        """Инициализатор объекта класса - выполняется в момент создания объекта"""
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y

    @classmethod
    def __check_value(cls, x):
        return isinstance(x, (int, float))

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
pt.set_coordinates(10, 20)          # не получаем ошибки
print(pt.get_coordinates())         # выводим актуальные координаты

pt2 = Point()
pt2.set_coordinates('1', '2')        # получаем ошибку `ValueError: Координаты должны быть числами`

```

### Какие еще свойства содержит экземпляр класса `Point`
```python
class Point:
    def __init__(self, x=0, y=0):
        """Инициализатор объекта класса - выполняется в момент создания объекта"""
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y

    @classmethod
    def __check_value(cls, x):
        return isinstance(x, (int, float))

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
print(dir(pt))                      # все свойства внутри объекта
```
> Можем заметить атрибуты `'_Point__x'` и `'_Point__y'` - они и содержат значения приватных атрибутов
> Таким образом, мы можем обратиться к `private-атрибутам` объекта следующим образом:
```python
print(pt._Point__x)
print(pt._Point__y)
```

#### **Однако не надо так делать. Сохраним это втайне.**

### Метод защиты атрибутов, который не получится обойти даже с названиями системных атрибутов
**Модуль `accessify`**

```zsh
pip install --upgrade pip
pip install accessify
```

После установки данной библиотеки необходимо ее импортировать

```python
from accessify import private, protected


class Point:
  def __init__(self, x=0, y=0):
    """Инициализатор объекта класса - выполняется в момент создания объекта"""
    self.__x = self.__y = 0
    if self.__check_value(x) and self.__check_value(y):
      self.__x = x
      self.__y = y

  @private
  @classmethod
  def __check_value(cls, x):
    return isinstance(x, (int, float))

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
print(dir(pt))  # все свойства внутри объекта

pt.__check_value(5)  # Получаем ошибку `accessify.errors.InaccessibleDueToItsProtectionLevelException: Point.check_value() is inaccessible due to its protection level`

```

##### Использование `accessify` оправдано только в случаях, когда требуется по-настоящему защитить чувствительные данные, повсеместное применение - оверинжиниринг. 

## Итоги по механизмам инкапсуляции
- `attribute` (без подчеркиваний в начале названия) - публичное свойство `public`
- `_attribute` (одно подчеркивание в начала названия) \
режим доступа `protected` (служит для обращения внутри класса и во всех его дочерних классах)
- `__attribute` (два подчеркивания) \
режим доступа `private` (служит для обращения только внутри класса)
- модуль `accessify` для защиты чувствительных данных