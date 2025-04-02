# Zad. 1
# Napisz funkcję, która przyjmuje dwie liczby (a i b) i zwraca ich sumę - do wykonania zadania wykorzystaj funkcję sum().

def sum_num(a, b):
    num = (a, b)
    return sum(num)

print(sum_num(13,33))


# Zad. 2
# Stwórz funkcję, z dwoma parametrami - name, surname. Wewnątrz ciała funkcji wykorzystaj
# odpowiednią wbudowaną funkcję zliczająca znaki przekazane w formie argumentów. 
# Przypisz  wynik do zmiennej letter_result i wyświetl go w terminalu.

def count_letters(name, surname):
    letter_result = len(name) + len(surname)
    return letter_result

print(count_letters("Wiktor", "Kulikowski"))

# Zad. 3
# Napisz funkcję, która przyjmuje dwa napisy (text1, text2) i zwraca ich konkatenację.

def con_texts(text1, text2):
    texts = text1 + text2
    return texts

print(con_texts("Wik","tor"))

# Zad. 4
# Napisz program, który poprosi użytkownika o wprowadzenie liczby całkowitej, a następnie wypisze jej wartość bezwzględną 
# korzystając z abs().

def num_abs():
    user_num = int(input("Podaj liczbę: "))
    abs_val = abs(user_num)
    return abs_val

print(num_abs())


# Zad. 5 
# Napisz program, który wyświetii w terminalu ile lat będzie miał Andrzej. Przy definiowaniu funkcji użyj wartości domyślnej
# dla parametru age. Wartość domyślna powinna mieć 10. 

def show_age(age = 10):
    return age

print("Andrzej ma",show_age(),"lat.")
    

# zad. 6 
# Napisz program, który oblicza pole powierzchni prostokąta. Program
# # powinien prosić użytkownika o wprowadzenie długości i szerokości prostokąta (uwzględnij wartości zmiennoprzecinkowe),
# # a następnie obliczyć jego pole powierzchni. 

def count_area():
    width = float(input("Podaj szerokość: "))
    height = float(input("Podaj wysokość: "))
    area = width * height
    return area
print(count_area())


# Zad. 7 
# Stwórz program, który będzie potęgował liczbę a do potęgi b. Wykorzystaj odpowiednią funkcję i wyświetl wynik w terminalu.

def num_power(a, b):
    result = pow(a, b)
    return result
print(num_power(3, 4))

# numbers = [3, 12, 7, -1, 9, 0]

# Zad. 8 
# Stwórz program, który wyświetli wartości tablicy numbers rosnąco.

def sort_asc():
    numbers = [3, 12, 7, -1, 9, 0]
    numbers.sort()
    return numbers
print(sort_asc())


# zad. 9 
# Stwórz program, który wyświetli maksymalną wartość tablicy numbers.

def max_value():
    numbers = [3, 12, 7, -1, 9, 0]
    max_num = max(numbers)
    return max_num
print(max_value())

# zad. 10
# Stwórz program, który wyświetli minimalną wartość tablicy numbers.

def min_value():
    numbers = [3, 12, 7, -1, 9, 0]
    min_num = min(numbers)
    return min_num
print(min_value())
