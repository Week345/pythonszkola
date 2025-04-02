# Zad. 1
# Napisz program, który:

# Utworzy listę zawierającą liczby od 1 do 5.
# Doda liczbę 6 na końcu listy.
# Wstawi liczbę 0 na początek listy.
# Usunie liczbę 3 z listy.
# Wypisze wynikową listę.

def tabular_opertations():
    numbers = [1, 2, 3, 4, 5]
    numbers.append(6)
    numbers.insert(0, 0)
    numbers.remove(3)
    print(numbers)

tabular_opertations()

# Zad. 2
# Napisz program, który:

# Pobierze od użytkownika dowolny tekst.
# Zamieni cały tekst na wielkie litery.
# Sprawdzi, czy tekst zaczyna się od litery "A" (po zamianie na wielkie litery).
# Podzieli tekst na słowa i wypisze liczbę słów.

def string_operations():
    usertext = str(input("Wpisz dowolny tekst: "))
    usertext.upper()
    usertext.startswith("A")
    words = len(usertext.split())
    print(f"Liczba słów: {words}")

string_operations()

# zad.3
# Napisz program, który:

# Utworzy krotkę z kilkoma elementami (np. liczby od 10 do 15, z powtórzeniem niektórych wartości).
# Wypisze pierwszy i ostatni element krotki.
# Sprawdzi, ile razy występuje w krotce liczba 12.

def tuple_check():
    tuple = (10, 11, 12, 13, 14, 15)
    print(f"Najmniejsza wartość: {tuple[0]}\nNajwiększa wartość: {tuple[-1]}") 
    num_check = tuple.count(12)
    count_tuple(num_check)

def count_tuple(num_check):
    if num_check >= 2:
        krotnosc = "razy"
    else:
        krotnosc = "raz"
    print(f"Liczba 12 znajduje się w krotce {num_check} {krotnosc}.")

tuple_check()

# zad.4 
# Napisz program, który:

# Wypisze liczby od 1 do 10 za pomocą pętli for.
# Wypisze liczby od 10 do 1 (malejąco) za pomocą pętli while.
# W pętli for:
# Przerywaj iterację (break), gdy napotkasz liczbę 5.
# Pomijaj (continue) wypisywanie liczby 3.

def loops():
    num_1_to_10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in range(1, 10):
        if i == 3:
            continue
        if i == 5:
            break
        print(i)
    while True:
        reversesort = num_1_to_10[::-1]
        print(reversesort)
        break
loops()
# zad.5
# Napisz program, który:

# Poprosi użytkownika o podanie nazwy dnia tygodnia (np. „poniedziałek”).
# Używając match-case, określi czy podany dzień jest dniem roboczym czy weekendem.
# Dla soboty i niedzieli wypisz „Weekend”.
# Dla pozostałych dni wypisz „Dzień roboczy”.
# Jeśli użytkownik poda niepoprawną nazwę, wypisz „Niepoprawny dzień”.

def days_of_the_week():
    userday = str(input("Podaj dzień tygodnia: "))
    mon_to_fri = "Dzień roboczy"
    sat_n_sun = "Weekend"
    wrong_day = "Niepoprawny dzień"
    match userday:
        case "poniedziałek":
            result = mon_to_fri
        case "wtorek":
            result = mon_to_fri
        case "środa":
            result = mon_to_fri
        case "czwartek":
            result = mon_to_fri
        case "piątek":
            result = mon_to_fri
        case "sobota":
            result = sat_n_sun
        case "niedziela":
            result = sat_n_sun
        case _:
            result = wrong_day
    print(result)

days_of_the_week()

# zad.6 
# Napisz program, który:

# Prosi użytkownika o podanie liczby.
# Próbuje przekonwertować wartość wejściową na liczbę całkowitą.
# Jeśli konwersja się nie powiedzie (użytkownik poda np. litery), zgłoś wyjątek ValueError 
# z komunikatem 
# „Podana wartość nie jest liczbą!” i wyświetl ten komunikat.
# W przeciwnym razie wypisz komunikat „Podano poprawną liczbę: X”.

def convert_num():
    usernum = input("Podaj liczbę: ")
    try:
        converted = int(usernum)
        positive = f"Podano poprawną liczbę: {converted}"
        print(positive)
    except ValueError:
        negative = "Podana wartość nie jest liczbą!"
        print(negative)

convert_num()


# zad.7
# Utwórz kilka zmiennych o różnych typach (np. liczba, tekst, lista, krotka, słownik, zbiór) 
# i wypisz ich wartość oraz typ, korzystając z funkcji type().

def return_value_and_type():
    text = "Testowy string"
    number = 4
    listtest = ["wartosc1","wartosc2","wartosc3"]
    tupletest = (1, 2, 3, 4, 5)
    print(f"{type(text)} {text} {type(number)} {number} {type(listtest)} {listtest} {type(tupletest)} {tupletest}")

return_value_and_type()
# zad.8
# Napisz program, który:

# Pobierze od użytkownika wartość (jako tekst).
# Spróbuje przekonwertować tę wartość na typ int.
# Wypisze wynik konwersji oraz typ zmiennej.
# Jeśli konwersja się nie powiedzie, wypisze komunikat o błędzie.

def convert_uinput():
    userinput = str(input("Podaj tekst: "))
    try:
        converted = int(userinput)
        print(f"{type(converted)} {converted}")
    except ValueError:
        print("Błąd konwersji")

convert_uinput()


# zad.9 
#  Wykorzystaj funkcję input() wbudowaną w python do
# pobrania informacji od użytkownika z konsoli.
# Poproś użytkownika o podanie imienia, nazwiska, miasta
# Zapisz te informacje w zmiennych name, surname i city
# Wyświetl w konsoli tekst podsumowujący pobrane dane.
# Przykładowe dane do wyświetlenia:
# # "Nazywasz się Ania Kowalska i mieszkasz w mieście: Krk"

def user_info():
    name = str(input("Podaj imie: "))
    surname = str(input("Podaj nazwisko: "))
    city = str(input("Podaj miasto: "))
    print(f"Nazywasz się {name} {surname} i mieszkasz w mieście: {city}.")

user_info()

# zad.10

# Zadanie - operacje na rachunku bankowym, skorzystaj 
# z skróconych operatorów przypisania z operacją
# matematyczną np:  +=  -=  *=  /=  itd
# Uwaga, po każdej operacji wyświetl saldo w konsoli
# Stwórz zmienną balance z wartością początkową 1000
# Dodaj wartość nowej pensji 7000
# Odejmij 2000 kosztów za mieszkanie
# Błąd banku pomnożył Twoje saldo trzykrotnie
# Odejmij 4000 na komputer
# Bank zorientował się że powstał błąd i cofa ostatnie           
# transakcje. Dodaj do salda 4000, podziel je przez 3
# i dopiero teraz odejmij 4000
# Pokaż saldo końcowe
def show_bal(desc, balance):
    print(f"{desc}: {balance}")

def bank_operations():
    balance = 1000
    show_bal("Saldo początkowe", balance)
    balance += 7000
    show_bal("Saldo po dodaniu nowej pensji", balance)
    balance -= 2000
    show_bal("Saldo po odjęciu kosztów mieszkania", balance)
    balance *= 3
    show_bal("Saldo po błędzie banku (razy 3)", balance)
    balance -= 4000
    show_bal("Saldo po zakupie komputera", balance)
    balance += 4000; balance /= 3; balance -= 4000
    show_bal("Saldo po korekcie banku", balance)
    show_bal("Saldo koncowe wynosi", balance)

bank_operations()
# zad.11

# Napisz program sprawdzający wymagania potencjalnego kandydata na programistę
#Dodaj zmienną experience z wartością 2, kolejną languages z listą elementów:
# "python", "typescript", "javascript", "java"
# Ostatnią zmienną będzie contract_type o wartości "b2b" jaką chce kandydat
#Wykorzystaj instrukcję if z operatorem and do sprawdzenia czy
# doświadczenie kandydata to dwa lub więcej lat oraz czy zna język python 
#i java. Pamiętaj o wykorzystaniu operatora in do sprawdzenia czy 
#wartość jest w liście
#Jeśli powyższe warunki są spełnione zrób kolejny if i sprawdź czy
# typ kontraktu jest "b2b" lub "employment", pamiętaj o użyciu operatora or.
#Zaprezentuj w terminalu informację że kandydat jest przyjęty, gdy warunki
#są spełnione.
#W przypadku, gdy warunki w if nie są spełnione pokaż w konsoli po else 
# odpowiednią informację

def candidate_qualities():
    experience = 2
    languages = ["python","typescript","javascript","java"]
    contract_type = "b2b"
    if experience >= 2 and "python" in languages and "java" in languages:
        if contract_type == "b2b" or contract_type == "employment":
            print("Kandydat przyjęty")
        else:
            print("Kandydat nie spełnia warunków kontraktu")
    else: 
        print("Kandydat nie spełnia warunków doświadczenia i znajomości języków")

candidate_qualities()

# zad.12

# Skorzystaj z pętli while aby dodać wartości od 1 do 100
#Dodaj zmienną i równą 0, która będzie inkrementowana w pętli o 1.
#Kolejną zmienną bęzie sum z wartością początkową 0
#W pętli while sprawdź czy i jest mniejsze równe 100
#Wewnątrz pętli dodaj do sum wartość i, następnie
#zrób inkrementację i o jeden
#Dodaj else po pętli while z tekstem w konsoli "Koniec pętli while"
#Zapisz podsumowanie "Suma wartości:" oraz wynik sumy

def loop_value_operations():
    i=0
    sum = 0
    while i<=100:
        sum += i
        i += 1
    else:
        print("Koniec pętli while")
    print(f"Suma wartości: {sum}")

loop_value_operations()

# zad.13 

#Napisz program, który tworzy i wyświetla listę zakupów na podstawie
#wprowadzonych przez użytkownika produktów.
#Program nie będzie zwracał żadnej wartości, ale bezpośrednio wyświetli listę zakupów w konsoli.
#
#Kroki do wykonania:
#Zdefiniuj funkcję show_products_list, która przyjmuje jeden parametr: shopping_list.
#Funkcja ta powinna wyświetlać wszystkie elementy listy zakupów, każdy element w nowej linii.
#Stwórz pustą listę zakupów.
#W pętli, poproś użytkownika o wprowadzenie nazw produktów do listy zakupów, 
#aż do wpisania słowa "koniec".
#Po zakończeniu wprowadzania, wywołaj funkcję show_products_list przekazując jej listę zakupów.
#

def add_products():
    shopping_list = []
    while True:
        userinput = str(input("Podaj element listy zakupów (wpisz koniec aby zakończyć):"))
        shopping_list.append(userinput)
        if userinput == "koniec":
            shopping_list.remove("koniec")
            break
    show_products_list(shopping_list)

def show_products_list(shopping_list):
    print("\nLista zakupów:")
    for item in shopping_list:
        print(item)

add_products()

# zad.14 

# Napisz dwie funkcje konwertujące temperaturę:
# 1 Funkcja skonwertuje stopnie Celsjusza na Fahrenheita z wzoru:
#   fahrenheit = celsius * 9 / 5 + 32
# 2 Funkcja konwertuje stopnie Fahrenheita na Celsjusza z wzoru:
#   celsius = (fahrenheit - 32) * 5 / 9;
#Dodatkowo w konsoli pokaż wynik konwersji np:
#"20 stopni Celsjusza to 68 stopni Fahrenheita" itd.
#Jeśli chcesz, użyj w string specjalnego znaku stopni ° za pomocą \xB0 
#
#Skonwertuj 20°C na Fahrenheita (68°F)
#Skonwertuj 86°F na Celsjusza (30°C)

def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    print(f"{celsius} stopni Celsjusza to {fahrenheit} stopni Fahrenheita")

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{fahrenheit} stopni Fahrenheita to {celsius} stopni Celsjusza")

celsius_to_fahrenheit(20)
fahrenheit_to_celsius(86)
# # zad.15
# Napisz program, który będzie sprawdzał poprawność adresu email. 
# Określ minmalną liczbę znaków na 6.
# Sprawdzaj, czy użytkownik podał @ w adresie.
# Informuj użytkownika o tym, jakie błędy popełnił podając niezgodny email.
# Przykład informacji:
# "Twój adres jest za krótki. Minimalna liczba znaków to 6."

def email_validity():
    useremail = input("Podaj adres email: ")
    if length_check(useremail):
        if at_check(useremail):
            print(f"Poprawnie podano adres email: {useremail}")
        else:
            print("Nie podano znaku @ w adresie email")
    else:
        print("Twój adres email jest za krótki. Minimalna liczba znaków to 6.")

def length_check(useremail):
    min_len = 6
    is_matching_len = len(useremail) >= min_len
    return bool(is_matching_len)

def at_check(useremail):
    is_matching_at = ("@" in useremail)
    return bool(is_matching_at)

email_validity()

# import re

# def email_validity():
#     useremail = input("Podaj adres email: ")
#     min_len = 6
#     if length_check(useremail):
#         if at_check(useremail):
#             if domain_check(useremail):
#                 print(f"Poprawnie podano adres email: {useremail}")
#             else:
#                 print("Nie podano poprawnej domeny mailowej.")
#         else:
#             print("Nie podano znaku @ w adresie email")
#     else:
#         print("Twój adres email jest za krótki. Minimalna liczba znaków to 6.")

# def length_check(useremail):
#     min_len = 6
#     is_matching_len = len(useremail) >= min_len
#     return bool(is_matching_len)

# def at_check(useremail):
#     is_matching_at = ("@" in useremail)
#     return bool(is_matching_at)

# def domain_check(useremail):
#     domain_pattern = r'@[a-zA-Z0-9.-]+[.][a-zA-Z]{2,}'
#     is_matching_domain = re.search(domain_pattern, useremail)
#     return bool(is_matching_domain)

# email_validity()