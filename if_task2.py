def compare_strings(string1, string2):
    if string1 == string2:
        return 1
    elif len(string1) > len(string2):
        return 2
    elif string2 == 'learn':
        return 3

str1 = input('Первая строка: ')
str2 = input('Вторая строка: ')

result = compare_strings(str1, str2)
print(result)