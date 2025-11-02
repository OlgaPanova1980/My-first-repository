# shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
# list_id_before = id(shopping_center[-1])
# print(shopping_center)
# print(list_id_before)
#
# shopping_center[-1].append("Uniqlo")
# print(shopping_center)
# list_id_after = id(shopping_center[-1])
# print(list_id_after)
# print(list_id_before == list_id_after)
# L = [1, 1, 2, 3, 2]
## b = set(L)
# print(b)
# # {1,2,3}
# text = "The Zen of Python"
#
# unique = set(text)
#
# print("Количество уникальных символов: ", len(unique))
# a = input("Введите первую строку: ")
# b = input("Введите вторую строку: ")
#
# a_set, b_set = set(a), set(b) # используем множественное присваивание
#
# a_and_b = a_set.intersection(b_set)
# print(a_and_b)
# some_var = (2,)
# if some_var is None:
#     print("NoneType")
# else:
#     print(type(some_var))
# if type(a) == int and 100 <= a <= 999 and a % 2 == 0 and a % 3 == 0:
#     if 100 <= a <= 999:
#         if a % 2 == 0:
#             if a % 3 == 0:
#                 print("Число удовлетворяет условиям")5
# M = [[i*j for j in range(1, 11)] for i in range(1, 11)]
# print(M)
# T = [[i*j for j in range(1,11)] for i in range(1,11)]
# # print(T)
# L = list(map(int, input().split()))
# print(not any(L))
# def linear_solve(a, b):
#     if a: # помним, что 0 интерпретируется как False, иначе True
#         return b / a
#     else:
#         return "Нет корней"
# def quadratic_solve(a, b, c):
#     d = b ** 2 - 4 * a * c
#     if d < 0:
#         return "Нет вещественных корней"
# def quadratic_solve(a, b, c):
#     if D(a, b, c) < 0:
#         return "Нет вещественных корней"
# iter_obj = iter("Hello!")
#
# print(next(iter_obj))

# print(list(map(pow_, a_list)))  # [1, 4, 9]
#
# for i in map(pow_, a_list):
#    pass

L = ['THIS', 'IS', 'LOWER', 'STRING']
L1 = L.lower[]
print(L1)