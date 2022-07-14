# Зформуйте строку, яка містить певну інформацію про символ в відомому слові.
# Наприклад "The [номер символу] symbol in [тут слово] is '[символ з відповідним порядковим номером]'".
# Слово та номер отримайте за допомогою input() або скористайтеся константою.
# Наприклад (слово - "Python" а номер символу 3) - "The 3 symbol in "Python" is 't' ".


while True:

    word = input("Введіть одне слово: ")
    count = 1

    if not word:
        print("Ви не вказали слово!")

    else:
        for symbol in word:
            if symbol == " ":
                count += 1
        if 2 <= count <= 4:
            print(f"Ви ввели {count} слова!")
        elif count > 4:
            print(f"Ви ввели {count} слів!")
        else:
            if not word.isalpha():
                print("Ви не можете використовувати числа та знаки!")
            else:
                break

while True:

    symbol = input("Введіть номер символу, який ви шукаєте: ")

    if not symbol:
        print("Ви не вказали номер!")

    else:
        if not symbol.isdigit():
            print("Ви можете використовувати лише числа")
        elif int(symbol) <= 0:
            print("Ви не можете вказувати число \"0\" та від'ємні числа!")
        else:
           break

try:
    found_symbol = word[(int(symbol) - 1)]
    print(f"{symbol} літера в слові \"{word}\" - це \"{found_symbol.upper()}\"")
except IndexError:
    print(f"{symbol} літери в слові \"{word}\" не існує")