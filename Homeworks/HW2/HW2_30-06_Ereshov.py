# Напишіть программу "Касир в кінотеатрі", яка буде виконувати наступне:
# Попросіть користувача ввести свій вік (можно використати константу або функцію input()).

while True:
    age = input("Вкажіть ваш вік: ")
    if not age:
        print("Ви не вказали свій вік")
    else:
        try:
            age = int(age)
        except ValueError:
            print("Ви можете вказати свій вік лише числами")
        if isinstance(age, int) and age <= 0:
            print("Невірно вказан вік")
        if isinstance(age, int) and age > 111:
            print("Невірно вказан вік")
        if age in range(1, 111, 1):
            break

# - якщо вік користувача складається з однакових цифр (11, 22, 44 і тд років, всі можливі варіанти!) - вивести "Який цікавий вік!"
if age in range(11, 111, 11): # Я вважаю, що вік 101 та 111 - це теж "цікавий вік"
    print("Який цікавий вік!")

# - якщо користувачу менше 7 - вивести "Де твої батьки?"
if age < 7:
    print("Де твої батьки?")

# - якщо користувачу менше 16 - вивести "Це фільм для дорослих!"
elif age < 16:
    print("Це фільм для дорослих!")

# - якщо користувачу більше 65 - вивести "Покажіть пенсійне посвідчення!"
elif age >= 65:
    print("Покажіть пенсійне посвідчення!")
# - у будь-якому іншому випадку - вивести "А білетів вже немає!"

else:
    print("А білетів вже немає!")