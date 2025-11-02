coworkers = ['Боженова', 'Укина', 'Горжий', 'Замирайло', 'Панова']
print(coworkers[0])
print(coworkers[4])
print(coworkers[::2])
print(coworkers[1::2])
print(len(coworkers))
new_coworkers = input('Введите имя коллеги: ')
coworkers.append(new_coworkers)
print(len(coworkers))
coworkers_name = input('Введите имя коллеги: ')
if coworkers_name in coworkers:
    print('Имя есть в списке')
else:
    print('Имени в списке нет')


