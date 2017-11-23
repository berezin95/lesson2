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
        answer = input('Скажи что-то:  ')
        if answer == 'Хорошо':
            break
        elif answer == 'Пока':
            break
        result = get_answer(answer, answers)
        print(result)

if __name__ == "__main__":
    ask_user()