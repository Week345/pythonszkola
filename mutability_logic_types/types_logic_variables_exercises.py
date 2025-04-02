# # Ćwiczenie 1.
# # Stwórz krotkę z trzema liczbami i spróbuj zmienić jej pierwszy element.

# test_krotka = (1,2,3,4)
# test_krotka[0] = 10
# print(test_krotka)

# # Ćwiczenie 2.
# # Stwórz listę liczb i dodaj nową liczbę na jej końcu.

lista = [1, 2, 3 ,4]
lista.append(5)
print(lista)

# # Ćwiczenie 3.
# # Stwórz zbiór z powtarzającymi się wartościami i sprawdź, ile ma unikalnych elementów.

zbior = {1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5}
zbiorset = set(zbior)
print(zbiorset)

# # Ćwiczenie 4.
# # Masz listę/krotkę liczb – znajdź największą liczbę
# # Czego należy użyć, jeśli zbiór danych może się zmieniać?

lista = [1, 2, 12, 88, 192]
max_lista = max(lista)
print(max_lista)

# W przypadku zmian zbioru danych
# def append_list(num):
#     lista.append(num)
#     max_lista = max(lista)
#     print(max_lista)

# append_list(99)

# # Ćwiczenie 5. 
# # Stwórz odpowiedni obiekt, w którym przechowasz dane o użytkowniku i jego wieku.
# # Do wartości obiektu odwołuj się po odpowiednim kluczu.

user_data = {"name": "Jacek Soplica", "age": 35}
print(user_data["name"], user_data["age"])

# # Ćwiczenie 6. 
# # Utwórz tablicę przechowującą kilka cyfr, które są zduplikowane. 
# # Skorzystaj z set() i wyświetl zawartość unikalnych wartości. 

numbers = {1, 3, 54, 12, 32, 66, 66, 32, 1, 3, 54, 3, 3, 7}
unique_numbers = set(numbers)
print(unique_numbers)

# # Ćwiczenie 7.
# # t = (4, 1, 3, 2)
# # Masz krotkę liczb. Stwórz jej posortowaną listę i wypisz ją w terminalu.

t = (4, 1, 3, 2)
sorted_list = sorted(t)
print(sorted_list)

# # Ćwiczenie 8.
# # Napisz funkcję, która będzie zwiększać wartość globalnej zmiennej counter o 1
# # za każdym razem, gdy zostanie wywołana. 

counter = 0

def increase():
    global counter
    counter += 1 
    return counter

print(increase()*6)

# # Ćwiczenie 9. 
# # Stwórz funkcję, która wyczyści globalną listę data = [1, 2, 3]

data = [1, 2, 3]

def clear():
    global data
    i = 0
    for i in range(0, 3):
        i += 1
        data.remove(i)
    return data

print(clear())

# # Ćwiczenie 10. 
# # Napisz funkcję, która usunie podaną wartość z globalnej listy (pod warunkiem, że w niej istnieje)

data = [1, 2, 3]

def remove_if_exists(num):
    global data
    if num in data:
        data.remove(num)
        print(data)

remove_if_exists(2)

# # Ćwiczenie 11.
# # Co zwróci poniższy kod? 
# # x = 10  
# # y = 0  
# # print(y or x)

# Zwroci 10 poniewaz w tym przypadku print wypisze nam pierwsza wartość która jest prawdziwa(czyli x = 10) poniewaz
# liczba 0 w pythonie traktowana jest jako wartosc false

# # Ćwiczenie 12. 

# Przeanalizuj poniższy kod: 

# # # x = 10
# # # print(id(x))  # ID obiektu w pamięci
# # # x += 1
# # # print(id(x)) 

# Dlaczego id obiektu się zmieniło?
# Poniewaz dzialamy na typie int ktory jest niemutowalny wiec kazda operacja zostanie wykonana na nowym obiekcie stworzonym w pamieci a wartosc oryginalu sie nie zmieni
# dlatego tez przy dzialaniach na typach niemutowalnych dzialamy na nowym ID


# # # lst = [1, 2, 3]
# # # print(id(lst))   ID listy w pamięci
# # # lst.append(4)
# # # print(id(lst))  

# Dlaczego id obiektu się nie zmieniło?
# Poniewaz dzialamy na liscie ktora jest mutowalna wiec kazda operacja zostanie wykonana na oryginalnym obiekcie wiec nie bedzie potrzeby stworzenia nowego w pamieci
# programu, a wiec nie zmieni sie ID obiektu bo bedziemy dzialac caly czas na tym samym obiekcie

# Ćwiczenie 13.

# Zainstaluj w Visual Studio Code wtyczki:
# Black Formatter (Microsoft)
# Flake8 (Microsoft)
# Mypy Type Checker (Microsoft)

# Przeanalizuj wszystkie błędy zgłoszone w swoich programach. 
# Dla ułatwienia - przenieś na początek 5 programów do osobnych
# plików i popraw wszystkie zgłoszone błędy.

# Ćwiczenie 14. 

# Do 5 pierwszych zadań ćwiczeniowych z funkcji (przerobienie programów z operatorami na funkcje)
# dodaj typowanie. 

def add(num1: int = 10, num2: int = 12):
    result = num1 + num2
    print(result)

add()

def sub(num1: int = 20, num2: int = 15):
    result = num1 - num2
    print(result)

sub()

def div(num1: int = 30, num2: int = 5):
    result = num1 / num2
    print(result)

div()

def mul(num1: int = 17, num2: int = 15):
    result = num1 * num2
    print(result)

mul()

def full_div(num1: int = 30, num2: int = 4):
    result = num1 // num2
    print(result)

full_div()

# Przykład funkcji z typowaniem:

# def add_numbers(number_1:int = 12, number_2: int = 8) -> int:
#     return number_1 + number_2


# result = add_numbers(20 + 10)
# print(result)

# Sprawdź, czy mimo wskazania typów kod się uruchamia. 
# Jeśli tak, to dlaczego?
# Porównaj tą samą funkcję, w której nie ma wskazania typowania
# z funkcją, do której udało Ci się dodać typowanie. 

# Czy edytor kodu reaguje inaczej na te podejścia?


# Ćwiczenie 15.

# Stwórz program ze zmienną globalną counter.
# Licznik globalny powinien być zmieniany za pomocą
# funkcji. 
# Funkcje increase oraz decrease powinny mieć zabezpieczenie przed możliwością
# podania im wartości ujemnej. 
# Dodatkowo licznik powinien być zmieniany tylko i wyłącznie przez liczby całkowite
# Użyj do tego odpowiedniej funkcji, która zaokrągla do najbliższej liczby całkowitej.

counter = 0

def increase():
    global counter
    user_input = round(float(input("Podaj liczbę do dodania: ")))
    if user_input >= 0:
        counter += user_input
    else:
        print("Podana wartość nie może być wartością ujemną")
    return counter
    
def decrease():
    global counter
    user_input = round(float(input("Podaj liczbę do odjęcia: ")))
    if user_input >= 0:
        counter -= user_input
    else:
        print("Podana wartość nie może być wartością ujemną")
    return counter

def main_counter():
    global counter
    increase()
    decrease()
    print(counter)

main_counter()

# Ćwiczenie 16. 

# Stwórz program ze zmienną globalną users_list.
# Tablica użytkowników powinna być modyfikowana z poziomu funkcji.
# Oczekiwane funkcje:
# add_user(user_name)
# remove_user(user_index)

# Dodaj pięciu użytkowników w pętli.
# Wyświetl tablicę.

# Usuń użytkownika z indeksem 3.
# Wyświetl tablicę.


# Ćwiczenie 17. 

# Stwórz zmienną a z wartością 5.
# Do zmiennej b przypisz a. 
# Wyświetl wartość zmiennej a oraz zmiennej b.

# Zmień wartość zmiennej a, nadpisując ją. (Ponownie należy zrobić np. a = 10)
# Wyprintuj wartości obu zmiennych. 

# Odpowiedz na pytanie - co tu się wydarzyło? 
# print(id(a)) oraz print(id(b)) mogą Ci się przydać w udzieleniu odpowiedzi :) 


# Ćwiczenie 18. 

# Stwórz zmienną a przechowującą listę z wartościami 'janek', 'zenek', 'franek'
# Do zmiennej b przypisz zmienną a.
# Zmień wartość indeksu 1 zmiennej a na 'kasia'
# Wykonaj:
# print(a)
# print(b)

# Co tu się wydarzyło i dlaczego?



