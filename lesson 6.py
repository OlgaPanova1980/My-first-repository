number = (int(1 % 2))
if number == 0:
    print("Число чётное")
else:
    print("Число нечётное")

number = 1
if number >= 0 and number == 0:
    print("число положительное, четное", "число равно нулю" )
else:
    print("число отрицательное, нечетное", "число равно нулю")
number = -1
if number >= 0:
    print("число положительное, четное")
elif number == 0:
    print("число равно нулю")
else:
    print("число отрицательное, нечетное")

for i in range(5): # i: [0, 1, 2, 3, 4] 5 итераций
    for j in range(3): # j: [0, 1, 2] 3 итерации
         for k in range(2): # k: [0, 1]
            print(i,j,k)
number = 1
for i in range(1,11): # i: [0, 1, 2] 3 итерации
    for j in range(2):  # j: [0, 1, 2] 3 итерации
         print(f'{number} * {i} = {number * i}')
         print()

n = 1
while n < 6:
    print(n)
    n += 1

n = 0
# пока n меньше 10
while n < 10:
    n += 1
    if n % 2 != 0:
        continue
    print(n)

sum = 0
i = 1
while i <= 10:
    sum += i
    i += 1
print(sum)

summ = 0
for i in range(1, 11):
    if i % 2 == 0:
        continue
    summ += i
print(summ)

multipl = 1
for i in range(1, 11):
    if i % 2 == 0:
        continue
    multipl *= i
print(multipl)
a = 10
b = 1
if a < b:
    for i in range(a, b+1):
        print(i)
else:
    print(a*b)
