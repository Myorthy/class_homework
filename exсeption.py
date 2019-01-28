# Задача 1

def polska_nota():
    operation, num_1, num_2 = input('Введите операцию для двух положительных чисел(польская нотация): ')
    num_1 = int(num_1)
    num_2 = int(num_2)
    operations = ['+', '-', '*', '/']
    assert operation in operations, 'Используйте только доступные операции! (+, -, *, /)'
    if operation == '+':
        result = num_1 + num_2
    elif operation == '-':
        result = num_1 - num_2
    elif operation == '*':
        result = num_1 * num_2
    elif operation == '/':
        result = num_1 / num_2

    return result
# print(polska_nota())



# Задача 2

# try:
#      # print(polska_nota())
#
# except ValueError:
#      print('Используемые значения противоречат заданным условиям')
# except UnboundLocalError:
#      print('Используется не корректная команда')
# except ZeroDivisionError:
#      print('На ноль делить нельзя!')
# else:
#     print('При выполнении кода исключений не обнаружено')


# Задача 3
documents = [
{"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
{"type": "invoice", "number": "11-2"},
{"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}]

def names():
  """
  функция, которая выводит список владельцев документов
  """
  num = input('Введите номер документа, для поиска его владельца: ')
  for person in documents:
    if person["number"] == num:
      try:
        return person["name"]
      except KeyError:
        return 'Владелец данного документа не обнаружен!'
    else:
        return 'Данный документ не обнаружен!'

while True:
  user_command = input("""Введите вашу команду("n" - для поика владельца документа,
  "end" - для выхода из программы) : """)

  if  user_command == 'n':
    print(names())
  elif  user_command == 'end':
    break
