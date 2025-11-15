# class Student:
#     course = "Data Science"
#
# s1 = Student()
# setattr(s1, 'name', 'Иван')
# setattr(s1, 'surname', 'Иванов')
# setattr(s1, 'semester', 1)
# result = (s1.__dict__)
#
# print(result)
#
# class Group:
#     members = []
#
# class Student:
#     pass
#
# s1 = Student()
# setattr(s1, 'name', 'Иван')
# setattr(s1, 'surname', 'Иванов')
# setattr(s1, 'semester', 1)
#
# s2 = Student()
# setattr(s2, 'name', 'Лев')
# setattr(s2, 'surname', 'Сергеев')
# setattr(s2, 'semester', 1)
#
# setattr(Group, 'members', s1)
# setattr(Group, 'members', s2)
#
# result = (Group.members)
#
# # # result = (s1.__dict__)
# class PasswordChecker:
#     def set_password_range(self, min_len, max_len):
#         self.min_len = min_len
#         self.max_len = max_len
#
#     def check_passwords(self, passwords):
#         for p in passwords:
#             if [self.min_len <= len(p) <= self.max_len]:
#                 return True
#             else:
#                 return False
#
#         # return [self.min_len <= len(p) <= self.max_len for p in passwords]
#
#
# checker1 = PasswordChecker()
# checker1.set_password_range(5, 10)
# print(checker1.min_len, checker1.max_len)
# print(checker1.check_passwords(['qwer', 'fool67', 'ghjo478hl404']))


# class Team():
#     def __init__(self, name, team_size, capital):
#         self.name = name
#         self.team_size = team_size
#         self.capital = capital
#
#     def show_info(self):
#         print(f"Team name: {self.name}, team size: {self.team_size}, capital: {self.capital}")
#
#
# team1 = Team('OpenAI', 100, 1000000)
# Team.show_info(team1)
# class User:
#    login = 'user_login'
#    role = 'Python Developer'
#
#    def demo_method_print(self):
#        print(f'Method call by {self}')
#
#    def show_attrs(self):
#        print(f'Login: {self.login}, role: {self.role}')
#
# u1 = User()
# u1.login  = 'Gridin'
# u1.role = 'TechLead'
# u1.show_attrs()



class Triangle():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def is_triangle(self):
        if self.a < self.b + self.c and self.b < self.a + self.c and self.c < self.b + self.a:
            return True
        else:
            return False
    def get_triangle_area(self):
        p = (self.a + self.b + self.c) / 2
        S = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

            return S

    def get_triangle_area(self):
        if self.is_triangle():
            s = (self.a + self.b + self.c) / 2
            return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
        else:
            return 0

print(Triangle(a = 3, b = 4, c = 5).is_triangle())