def find_person(name, user_list):
    index = 0
    while index < len(user_list) :
        if user_list[index] == name:
            return '{} нашелся(ась)'.format(user_list.pop(index))
            break
        index = index + 1
    return 'Пользователя нет в списке'


users = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
user_name = input("Введи имя: ")
result = find_person(user_name, users)
print(result)

'''print(users)
for name in users:
    if name == "Валера":
        user_id = users.index(name)
        print('{} нашелся'.format(users.pop(user_id)))
print(users)'''

'''index = 0
while index < (len(users) - 1):
    if users[index] == 'Валера':
        break
    index = index + 1

print('{} нашелся'.format(users.pop(index)))
print(users)'''