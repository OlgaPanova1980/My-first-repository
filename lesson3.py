string = "нь, сын трёхголового дракона!"
if len(string) < 42:
        print("length error: длина строки составляет", len(string), "символов")
else:
        print(string[7:42:3])
text = "12435514234 ERROR index: big_terrible_mistake message: Ай, случилася беда!"

template = 'message: '
index = text.index(template)
print(text[index + len(template):])
text = "5423534 lajksdfij;jhh абракадабра dfasdfs9d6f7686"
template = 'message: '
index = text.find(template)
if index != -1:
    print(text[index + len(template):])
    text = "12435514234 ERROR index: big_terrible_mistake message: Ай, случилася беда!"

text = "12435514234 ERROR index: big_terrible_mistake message: Ай, случилася беда!"

template = 'message: '
if template in text:
    index = text.index(template)
    print(text[index + len(template):])
a = "Ольга"
print("Самая красивая женщина на свете это", a)
string = "dd"
if len(string) == 0:
    print(False)
else:
    print(string.isascii())

string = "aaa"
print(string.endswith("_"))
if len(string) == 0:
    print(False)
data = input()
print(data * 5)
import sys

data = sys.stdin.readline()
print(data * 5)

n = 100
if n % 2 == 0:
    print(True)











