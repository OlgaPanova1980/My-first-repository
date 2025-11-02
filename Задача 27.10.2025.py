# # Преобразовать ФИО в Фамилия И.О.
# fio = input('Введите ФИО: ')
# f, i, o = fio.split()
# # print(f + ' ' + i[0] + '.' + o[0] + '.')
# # print(answer)
# print(f"{f} {i[0]}.{o[0]}.")
#
# # Написать функцию для проверки соотв.строки формату YYYY-MM-DD
# def chek_date (str_date):
#     if len(str_date.split('-')) != 3:
#         return False
#     year, month, day = str_date.split('-')
#     if len(year) != 4 or len(month) != 2 or len(day) != 2:
#         return False
#     if not year.isdigit() and month.isdigit() and day.isdigit():
#         return False
#     year, month, day = int(year), int(month), int(day)
#     if 2000 <= year <= 3000 and 1 <= month <= 12 and 1 <= day <= 31:
#         return True
#     else:
#         return False
#
# print(chek_date ('2021-05-26'))
# print(chek_date ('20212-05-26'))
# print(chek_date ('2021205-26'))
# print(chek_date ('202F-05-26'))
# print(chek_date ('2025-13-26'))

import json
def save_info(info):
    with open("info.json", "w") as f:
        json.dump(info, f)

def load_info ():
    with open("info.json") as f:
        info = json.load(f)
        return info
info = load_info()
print(info)
# a = [
#     {1 : 2},
#     {"d" : "c"},
#     "123",
#     124587
# ]
#
# save_info(a)

