# Возможно 3 варианта входных данных (домен не имеет значения):
# 'https://www.example.com'
# 'www.example.com'
# 'example.com'
#
# переменная url (переименовать нельзя)
# Для проверки случаев меняйте значения в
#
url = 'example.com'
if 'www' not in url:
    url = 'https://www.' + url
elif 'https://' not in url:
    url = 'https://' + url
#
# Переменная должна содержать нормальный url  'https://www.example.com':
print(url)


