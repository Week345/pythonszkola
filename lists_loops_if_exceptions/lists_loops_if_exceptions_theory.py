# https://docs.python.org/pl/3/tutorial/datastructures.html


############################### LISTY #######################

# Listy (ang. lists) to uporządkowane, mutowalne sekwencje w Pythonie. 
# Oznacza to, że możesz modyfikować ich zawartość po utworzeniu. 
# Python oferuje wiele metod, które pozwalają na łatwe operowanie na listach.


# Najważniejsze metody listowe:

# append(x)
# Dodaje element x na końcu listy.

# Przykład:
# liczby = [1, 2, 3]
# liczby.append(4)
# print(liczby)  # Wynik: [1, 2, 3, 4]

# extend(iterable)
# Rozszerza listę o elementy z podanego iterowalnego obiektu (np. innej listy).

# Przykład:
# liczby = [1, 2, 3]
# liczby.extend([4, 5])
# print(liczby)  # Wynik: [1, 2, 3, 4, 5]

# insert(index, x)
# Wstawia element x na pozycji index

# Przykład:
# liczby = [1, 2, 3]
# liczby.insert(1, 10)
# print(liczby)  # Wynik: [1, 10, 2, 3]

# remove(x)
# Usuwa pierwsze wystąpienie elementu x z listy.

# Przykład:
# liczby = [1, 2, 3, 2]
# liczby.remove(2)
# print(liczby)  # Wynik: [1, 3, 2]

# pop([index])
# Usuwa i zwraca element z podanego indeksu (domyślnie ostatni element).

# Przykład:
# liczby = [1, 2, 3]
# ostatni = liczby.pop()
# print(ostatni)   # Wynik: 3
# print(liczby)    # Wynik: [1, 2]

# index(x[, start[, end]])
# Zwraca indeks pierwszego wystąpienia elementu x w liście.

# count(x)
# Zlicza, ile razy element x występuje w liście.

# sort()
# Sortuje listę (modyfikuje oryginalną listę).

# reverse()
# Odwraca kolejność elementów w liście.


######################## Metody na stringach #####################

# upper()
# Zwraca łańcuch z wszystkimi literami zamienionymi na wielkie.

# Przykład:
# tekst = "python"
# print(tekst.upper())  # Wynik: "PYTHON"

# lower()
# Zwraca łańcuch z wszystkimi literami zamienionymi na małe.

# capitalize()
# Zwraca łańcuch, w którym pierwsza litera jest wielka, a reszta mała.

# find(sub)
# Zwraca indeks pierwszego wystąpienia podłańcucha sub lub -1, jeśli nie zostanie znaleziony.

# replace(old, new)
# Zwraca nowy łańcuch, w którym wszystkie wystąpienia old zostały zastąpione przez new.

# split(sep)
# Dzieli łańcuch na listę mniejszych łańcuchów według podanego separatora.

# Przykład:
# tekst = "a,b,c"
# print(tekst.split(","))  # Wynik: ['a', 'b', 'c']

# join(iterable)
# Łączy elementy iterowalnego obiektu (np. listy) w jeden łańcuch, umieszczając pomiędzy nimi dany separator.

# Przykład:
# slowa = ["Hello", "world"]
# print(" ".join(slowa))  # Wynik: "Hello world"

# strip()
# Usuwa białe znaki (np. spacje, znaki nowej linii) z początku i końca łańcucha.

# startswith(prefix) i endswith(suffix)
# Sprawdzają, czy łańcuch zaczyna się lub kończy określonym ciągiem znaków.


###################### Instrukcje warunkowe ################################


# Instrukcje warunkowe pozwalają na wykonywanie różnych fragmentów kodu w zależności od spełnienia 
# określonych warunków. W Pythonie używamy do tego konstrukcji:

# if warunek1:
#     # blok kodu wykonany, gdy warunek1 jest True
# elif warunek2:
#     # blok kodu wykonany, gdy warunek1 jest False, a warunek2 jest True
# else:
#     # blok kodu wykonany, gdy wszystkie wcześniejsze warunki są False



# W wielu językach programowania istnieje konstrukcja switch-case, która pozwala na sprawdzanie 
# wielu możliwych wartości zmiennej i wykonanie odpowiadającego fragmentu kodu.
# Od Pythona 3.10 dostępna jest nowa konstrukcja match-case, która działa na zasadzie porównania 
# wzorców.

# match zmienna:
#     case wartość1:
#         # kod dla przypadku wartość1
#     case wartość2:
#         # kod dla przypadku wartość2
#     case _:
#         # kod, gdy żaden z powyższych przypadków nie pasuje (domyślny)

# Znak podkreślenia _ działa jako „catch-all” (domyślny przypadek).


######################## Obsługa wyjątków #####################

# W trakcie działania programu mogą wystąpić błędy, które przerywają jego 
# normalne działanie. Aby je obsłużyć, używamy konstrukcji:

# try – blok, w którym umieszczamy kod, który może wygenerować wyjątek.
# except – blok, w którym definiujemy sposób obsługi wyjątku.
# raise – służy do ręcznego zgłoszenia wyjątku, jeśli spełniony jest pewien warunek 
# (np. nieprawidłowe dane).


########################## Slicing list #############################


# # slicing 

# lista = [10, 20, 30, 40, 50, 60]

# # Podlisty
# print(lista[1:4])    # od indeksu 1 do 3 -> [20, 30, 40]
# print(lista[:3])     # od początku do indeksu 2 -> [10, 20, 30]
# print(lista[2:])     # od indeksu 2 do końca -> [30, 40, 50, 60]

# # Krok
# print(lista[1:6:2])  # od indeksu 1 do 5 co 2 -> [20, 40, 60]

# # Odwrócenie listy
# print(lista[::-1])   # [60, 50, 40, 30, 20, 10]


# tekst = "Python"

# print(tekst[0:3])  # "Pyt"
# print(tekst[:4])   # "Pyth"
# print(tekst[2:])   # "thon"
# print(tekst[::-1]) # "nohtyP"  (odwrócony łańcuch)

