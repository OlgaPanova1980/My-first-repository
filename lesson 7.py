coworkers = ['Irina_Ivanova', 'Anna_Rykova', 'Olga_Fatova', 'Liza_Chex', 'Yana_Vidova']
print(coworkers[0], coworkers[4])
print(coworkers[:])
print(len(coworkers))
client_name = input('Введите имя клиента: ')
coworkers.append(client_name)
print(len(coworkers))
client_name = input('Введите имя клиента: ')
if client_name in coworkers:
    print('имя есть в списке')
else:
    print('имени в списке нет')

coworkers = ['Мария', 'Ангелила', 'Антонина', 'Дарья', 'Екатерина']

# вывести первый и последний элемент списка
print(f'''Первый элемент списка {coworkers[0]}
            Последний элемент списка {coworkers[-1]}''')

# вывести каждый первый элемент списка
print(coworkers[::2])

# вывести каждый второй элемент списка
print(coworkers[1::2])
numbers = set([1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9, 9])
print(numbers)

# вывести длину списка
print(f'Длина списка: {len(coworkers)}')

# добавить новый элемент в список
name = input('Введите имя нового коллеги: ')
coworkers.append(name)
# вывести длину списка
print(f'Длина списка: {len(coworkers)}')

# проверить наличие элемента в списке
name = input('Введите имя коллеги: ')
if name in coworkers:
    print('Этот коллега есть в списке')
else:
    print('Такого имени в списке нет')