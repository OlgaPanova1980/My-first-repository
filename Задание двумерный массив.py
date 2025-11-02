rows = 3
column = 3
todo_list = []
for i in range(rows):
    todo_list.append(['']*column)
print(todo_list)

print('Заполняем ежедневник: ')
for i in range(rows):  # цикл по строкам
    for j in range(column):  # цикл по столбцам
        print()
        print(f'rows:{i} column:{j}')
        todo_list[i][j] = input(f'todo_list[{i}][{j}] = ')
    # выводим заполненный массив
print()
print(f'Заполненный массив: {todo_list}')

num_delete = int(input('Введите номер записи, которую нужно удалить 0-2: '))
for array in todo_list:
 # удаляем элемент массива по индексу
 array.pop(num_delete)
# выводим заполненный массив
print(f'Полученный массив: {todo_list}')
for i in range(len(todo_list)):
#Считайте с консоли номер дня недели и новую запись и добавьте эту запись в соответствующий элемент списка.
    new_delo = input(f'Введите новое значение для {i} строки: ')

 # добавляем полученный элемент по индексу column
    todo_list[i].insert(num_delete, new_delo)
print()
print(f'Итоговый список дел: {todo_list}')
for i in range(3):
    print(todo_list[i])
    print()

