'''def cut_cake(parts):
    try:
        return 1 / int(parts)
    except (ZeroDivisionError, TypeError, ValueError):
        print("Не надо так")

def do_someyhing(x):
    try:
        print(x)
    except:
        print('Пока!')
x = 0
while x < 10:
    do_someyhing(x)
x += 1
#cake = cut_cake([1,2,3,4])
#print(cake)'''
answers = {
        "привет": "И тебе привет!",
        "как дела": "Лучше всех",
        "что нового": "Ничего"
    }

def get_answer(question, answers=answers):
    question = question.lower()
    return answers.get(question)

def ask_user():
    while True:
        try:
            answer = input('Как дела?  ')
            if answer == 'Хорошо':
                break
            elif answer == 'Пока':
                break
            result = get_answer(answer, answers)
            print(result)
        except(KeyboardInterrupt):
            print("\nЗачем остановил?")
            break

ask_user()


