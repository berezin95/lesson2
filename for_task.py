#string = input('Строка: ')

#for letter in string:
#    print(letter)

def average(scores):
    return sum(scores) / len(scores)

classes = [
    {'school_class': '4a', 'scores': [3,4,4,5,2]},
    {'school_class': '7б', 'scores': [5,4,5,5,3,2,2]},
    {'school_class': '10а', 'scores': [5,5,5,5,5]},
    {'school_class': '9в', 'scores': [3,4,4]},
    {'school_class': '6б', 'scores': [3,4,4,5,2]}
]

all_marks = []
for index in classes:
    all_marks.extend(index['scores'])
    avg = average(index['scores'])
    print('Средний балл в ' + index['school_class'] + ' классе: ' + str(avg))

print('\nСредний балл в школе: ' + str(average(all_marks)))

#print(classes[0]['school_class'])
#print(average([2, 3, 4]))