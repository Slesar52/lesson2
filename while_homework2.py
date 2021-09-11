answer_questions = [
    {"Как дела": "Хорошо!"}, 
    {"Что делаешь?": "Программирую"}
    ]

question = input("Какой у тебя вопрос?")

def ask_user(answer_questions):
    while True:
        question = input("Какой у тебя вопрос?")
        if question == answer_questions[0]:
            print(answer_questions[1])
