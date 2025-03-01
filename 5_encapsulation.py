# !pip install --upgrade pip
# !pip install accessify

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

pt.__check_value(5)
# Получаем ошибку `accessify.errors.InaccessibleDueToItsProtectionLevelException:
# Point.check_value() is inaccessible due to its protection level`