# 1. Створіть дві змінні first=10, second=30.
# Виведіть на екран результат математичної взаємодії (+, -, *, / и тд.) для цих чисел
first = 10
second = 30

print(first, " + ", second, " = ", first + second)

print(second, " - ", first, " = ", second - first)

print(first, " * ", second, " = ", first * second)

print(second, " / ", first, " = ", int(second / first))

print(second, " // ", first, " = ", second // first)

print(second, " ** ", first, " = ", second ** first)

print(second, " % ", first, " = ", second % first)


# 2. Створіть змінну і запишіть в неї результат порівняння (<, > , ==, !=) чисел з завдання 1.
# Виведіть на екран результат кожного порівняння.

result = first < second
print(first, " < ", second, " - is ", result)

result = first > second
print(first, " > ", second, " - is ", result)

result = first == second
print(first, " == ", second, " - is ", result)

result = first != second
print(first, " != ", second, " - is ", result)

# Створіть змінну - результат конкатенації (складання) строк str1="Hello " и str2="world".
# Виведіть на екран.

str1 = "Hello "
str2 = "world!"
result = str1 + str2
print(result)