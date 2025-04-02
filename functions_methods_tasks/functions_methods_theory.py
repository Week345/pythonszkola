# Funkcja w języku Python (i nie tylko) to wyodrębniony fragment kodu, który można wielokrotnie wywołać z różnymi danymi wejściowymi, 
# aby uzyskać określony wynik lub efekt. Poniżej znajdziesz szczegółowe omówienie najważniejszych aspektów funkcji w Pythonie:


# def nazwa_funkcji(parametry):
#     """
#     (Opcjonalny) Docstring - krótki opis funkcji
#     """
#     # ciało funkcji
#     # ...
#     return (wartość_zwrotna)


# def – słowo kluczowe sygnalizujące definicję funkcji.

# nazwa_funkcji – nazwa, którą posługujemy się przy wywoływaniu funkcji. 
# Tradycyjnie stosuje się notację snake_case, np. oblicz_sume, sprawdz_czy_pierwsza

# parametry (opcjonalne) – zmienne, które przyjmują dane wejściowe przekazywane do funkcji.

# : – dwukropek oznacza początek ciała funkcji.

# return (opcjonalne) – instrukcja zwracająca wartość lub kończąca działanie funkcji


# Przykład prostej funkcji:

# def say_something(text):
#     print(text)

# say_something('testowa wiadomość')


# Jaka jest różnica między parametrem, a argumentem?

# Parametry to zmienne zadeklarowane w definicji funkcji.
# Argumenty to konkretne wartości przekazywane funkcji podczas jej wywołania.

# Rodzaje parametrów w Pythonie
# Parametry pozycyjne (podstawowe): np. def funkcja(a, b): ...
# Parametry domyślne: np. def funkcja(a, b=10): ...
# Jeśli wywołasz funkcja(5), to b przyjmie wartość 10.
# Parametry z gwiazdką (*args): przechwytują dowolną liczbę pozycyjnych argumentów w postaci krotki (tuple).
# Parametry z podwójną gwiazdką (**kwargs): przechwytują dowolną liczbę nazwanych argumentów w postaci słownika (dict).

# *args – dowolna liczba pozycyjnych argumentów
# „Pozycyjne” oznacza, że argumenty są rozpoznawane według kolejności, w jakiej zostały przekazane do funkcji (np. fun(1, 2, 3)).
# Jeśli w funkcji zadeklarujesz parametr *args, to wszystkie dodatkowe argumenty (których nie przypisano do innych nazwanych parametrów) 
# zostaną zebrane w krotkę (ang. tuple). 

# def wypisz_liczby(*args):
#     print("args to:", args)
#     for liczba in args:
#         print(liczba)

# Wywołanie funkcji:
# wypisz_liczby(1, 2, 3)  
# args to: (1, 2, 3)
# 1
# 2
# 3

# W przykładzie *args przechwytuje (1, 2, 3) jako krotkę (1, 2, 3).
# Możesz użyć args w pętli, sumować go, itp.
# Jeśli nie przekażesz żadnych argumentów, args będzie pustą krotką ().

# Gdzie to się przydaje?
# Gdy nie wiesz z góry, ile liczb (lub innych danych) użytkownik chce wprowadzić do funkcji.
# Możesz np. napisać funkcję suma(*args) i zsumować wszystkie liczby przekazane do funkcji.

# **kwargs – dowolna liczba nazwanych argumentów
# „Nazwane argumenty” (ang. keyword arguments) oznaczają te, które przekazujesz z podaniem nazwy zmiennej, 
# np. funkcja(imie="Jan", wiek=30).
# Jeśli w funkcji zadeklarujesz parametr **kwargs, to wszystkie dodatkowe, niewymienione wcześniej w definicji 
# funkcji nazwane argumenty zostaną zebrane w słownik (ang. dict).

# def wypisz_dane(**kwargs):
#     print("kwargs to:", kwargs)
#     for klucz, wartosc in kwargs.items():
#         print(f"{klucz} = {wartosc}")

# # Wywołanie funkcji:
# wypisz_dane(imie="Jan", wiek=30, miasto="Warszawa")
# # kwargs to: {'imie': 'Jan', 'wiek': 30, 'miasto': 'Warszawa'}
# # imie = Jan
# # wiek = 30
# # miasto = Warszawa


# Zwracanie wartości (return)
# Instrukcja return kończy działanie funkcji i (opcjonalnie) przekazuje wartość wywołującemu (kodowi, który funkcję wywołał).

# Jeśli w funkcji nie ma instrukcji return lub występuje samo return (bez wartości), to funkcja zwraca wartość None.
# Można mieć więcej niż jedną instrukcję return w funkcji, ale tylko jedna zostanie wykonana, w zależności od przebiegu kodu 
# (zazwyczaj w różnych warunkach if/else).

# def check_age(age):
#     if age < 18:
#         return "Niepełnoletni"
#     else:
#         return "Pełnoletni"

# print(check_age(16))  # "Niepełnoletni"
# print(check_age(20))  # "Pełnoletni"


# Wywoływanie funkcji:
# Aby wykonać (wywołać) funkcję, piszemy jej nazwę i w nawiasie przekazujemy argumenty. 
# Jeśli funkcja ma zwracać wartość, zazwyczaj przechwytujemy ją w zmiennej lub od razu wyświetlamy.

# Przykład:

# def multiply(a, b):
#     return a * b

# # Wywołanie i zapis do zmiennej
# result = multiply(3, 4)
# print(result)  # 12

# # Wywołanie bezpośrednio w print
# print(multiply(10, 2))  # 20




# -------------------------------------------------------------------------------------------------------------


# Funkcje służące do konwersji typów (tzw. type conversion / type casting)

# int(x) – konwertuje obiekt x na liczbę całkowitą (jeśli to możliwe).
# float(x) – konwertuje obiekt x na liczbę zmiennoprzecinkową.
# str(x) – konwertuje obiekt x na łańcuch znaków.
# bool(x) – konwertuje obiekt x na typ logiczny (True/False).
# list(x) – konwertuje obiekt x na listę.
# tuple(x) – konwertuje obiekt x na krotkę (tuple).
# set(x) – konwertuje obiekt x na zbiór (set).
# dict(...) – tworzy słownik (dictionary). Zazwyczaj z par (klucz, wartość).
# complex(x, y) – tworzy liczbę zespoloną z części rzeczywistej x i urojonej y.


# Funkcje do obsługi ciągów, list, kolekcji

# len(x) – zwraca długość obiektu (np. długość listy, łańcucha znaków).
# range(start, stop, step) – generuje sekwencję liczb całkowitych od start do stop-1 (co step krok).
# sorted(iterable) – zwraca posortowaną listę na podstawie przekazanego obiektu iterowalnego.
# min(iterable) / max(iterable) – zwracają najmniejszą/największą wartość z przekazanego obiektu iterowalnego.
# sum(iterable) – zwraca sumę elementów obiektu iterowalnego (np. listy liczb).
# enumerate(iterable) – zwraca obiekt pozwalający iterować (przechodzić) przez elementy wraz z ich indeksami.


# Funkcje pomocnicze (logiczne, matematyczne, itp.)

# abs(x) – zwraca wartość bezwzględną liczby x.
# round(number, ndigits) – zaokrągla liczbę number do określonej liczby miejsc po przecinku ndigits.
# pow(x, y) – oblicza x do potęgi y.
# divmod(a, b) – zwraca krotkę (iloraz, reszta) dzielenia a przez b.
# all(iterable) – zwraca True, jeśli wszystkie elementy w obiekcie iterowalnym są prawdziwe (lub obiekt jest pusty).
# any(iterable) – zwraca True, jeśli przynajmniej jeden element w obiekcie iterowalnym jest prawdziwy.


# Funkcje do debugowania, wykonania kodu, systemowe

# print(...) – wypisuje przekazane argumenty na standardowe wyjście (np. konsolę).
# input(...) – wczytuje dane wejściowe od użytkownika jako łańcuch znaków.
# type(x) – zwraca typ obiektu x.
# id(x) – zwraca unikatowy identyfikator obiektu x w pamięci.
# help(x) – wyświetla pomoc na temat obiektu x (np. funkcji, modułu).
# dir(x) – zwraca listę atrybutów i metod obiektu x.
# isinstance(x, typ) – sprawdza, czy obiekt x jest instancją typu typ.
# exit(), quit() – kończą działanie interpretera (głównie w środowiskach interaktywnych).


# Link do dokumentacji: https://docs.python.org/3/library/functions.html


# Math i operacje matematyczne
# Moduł math w Pythonie oferuje bogaty zestaw funkcji matematycznych, przydatnych w różnych dziedzinach, 
# takich jak algebra, analiza matematyczna, geometria czy statystyka. Rozszerza on możliwości prostych operacji arytmetycznych, 
# dostępnych za pomocą operatorów i wbudowanych funkcji Pythona, oferując zaawansowane metody i funkcje ułatwiające obliczenia.

# Moduł math jest częścią biblioteki standardowej Pythona, co oznacza, że nie wymaga dodatkowej instalacji. 
# Aby uzyskać dostęp do jego funkcji i stałych, wystarczy zaimportować go poleceniem import math. 
# Po zaimportowaniu mamy do dyspozycji szeroką gamę funkcji i stałych matematycznych, które sprawiają, 
# że obliczenia stają się prostsze i bardziej przejrzyste. Funkcje zaokrąglania, takie jak math.ceil i math.floor, 
# już poznaliśmy – teraz przyjrzymy się kilku innym przydatnym metodom. Pamiętaj, że ta wiedza przyda się przede wszystkim wtedy, 
# jeśli kiedyś będziesz zgłębiać bardziej zaawansowane zagadnienia matematyczne.

