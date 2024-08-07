# Цель: освоить навык создания пользовательских исключений и использовать его в решении задачи.
# Повторить тему ООП и принцип инкапсуляции.

class Car:
  def __init__(self, model, vin, numbers):
    self.model = model
# При инициализации объекта вызываются методы __is_valid_vin и __is_valid_numbers для проверки корректности данных
    self.__vin = self.__is_valid_vin(vin)
    self.__numbers = self.__is_valid_numbers(numbers)


  def __is_valid_vin(self, vin_number):
    if not isinstance(vin_number, int): # Проверка на целочисленность
      raise IncorrectVinNumber('Некорректный тип vin номер')
    if not  1000000 <= vin_number <= 9999999: # Проверка на вхождение в диапазон
      raise IncorrectVinNumber('Неверный диапазон для vin номера')
    return True


  def __is_valid_numbers(self, numbers):
    if not isinstance(numbers, str): # Номер должен быть в строковом виде
      raise IncorrectCarNumbers('Некорректный тип данных для номеров')
    if len(numbers) != 6: # Номер должен иметь длину 6 знаков
      raise IncorrectCarNumbers('Неверная длина номера')
    return True



class IncorrectVinNumber(Exception):
  def __init__(self, message):
    self.message = message


class IncorrectCarNumbers(Exception):
  def __init__(self, message):
    self.message = message


try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')