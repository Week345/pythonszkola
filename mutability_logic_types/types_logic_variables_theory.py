# # https://docs.python.org/pl/3/tutorial/datastructures.html

# Filmik od ByteGrad - polecam sprawdzić. Ci, którzy obawiają się
# bariery językowej zawsze mogą włączyć automatyczne napisy po polsku.
# Link do filmiku poniżej:

# https://www.youtube.com/watch?v=-ilAEL7vfTs

# # Podstawowe typy danych:

# # int – liczby całkowite (np. 10, -5)
# # float – liczby zmiennoprzecinkowe (np. 3.14, -0.001)
# # complex – liczby zespolone (np. 2+3j)

# # string - (łańcuch znaków), reprezentowane przez str (np. "Hello", 'Python')
# # bool - typ logiczny, przyjmujący wartości True lub False

# # lista - mutowalna sekwencja (możesz ją modyfikować np. dodawać, usuwać, zmieniać elementy)
# # krotka - niemutowalna sekwencja (po utworzeniu nie możesz zmieniać jej zawartośći metodami)
# # słownik - zbiór par klucz-wartość
# # zbiór - nieuporządkowany zbiór unikalnych elementów.

# # liczba = 42
# # tekst = "Python"
# # lista = [1, 2, 3]
# # krotka = (4, 5, 6)
# # slownik = {"klucz": "wartość"}
# # zbior = {1, 2, 3}

# --------------------------------------------------------------

# # Mutowalność vs. Niemutowalność

# # Niemutowalne:
# # Typy takie jak int, float, bool, str, tuple są niemutowalne. Oznacza to, że po utworzeniu obiektu nie możesz zmienić jego zawartości.

# Przykład:
# # x = 10
# # print(id(x))  # ID obiektu w pamięci
# # x += 1
# # print(id(x))  # Nowe ID → powstał nowy obiekt!
# Każda operacja na int tworzy nowy obiekt w pamięci.

# # Mutowalne:
# # Typy takie jak list, dict, set są mutowalne, co oznacza, że możesz modyfikować ich zawartość (np. zmieniać, dodawać lub usuwać elementy).

# Przykład:
# # lst = [1, 2, 3]
# # print(id(lst))  # ID listy w pamięci
# # lst.append(4)
# # print(id(lst))  # ID się nie zmieniło! Modyfikujemy zawartość, nie referencję
# Lista się zmieniła, ale nie powstał nowy obiekt.

# Podsumowanie
# Niemutowalne (np. int, str, tuple) → każda zmiana tworzy nowy obiekt.
# Mutowalne (np. list, dict, set, obiekty klas) → można zmieniać zawartość, ale referencja zostaje.

# -------------------------------------------------------------------------

# # Wartości, które są False:
# # 0  - liczby całkowite i zmiennoprzecinkowe
# # "" - pusty string,
# # () - pusta krotka
# # [] - pusta lista,
# # {} - pusty słownik,
# # None - obiekt NoneType
