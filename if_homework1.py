age = int(input("Введите свой возраст: "))

def study(age):
    if 0 <= age <= 5:
        return "детский сад"
    elif 6 <= age <= 17:
        return "школа"
    elif 18 <= age <= 23:
        return "ВУЗ"
    else:
        return "рабочее учреждение"

x = study(age)

print(f"Больше всего вам подойдет: {x}")