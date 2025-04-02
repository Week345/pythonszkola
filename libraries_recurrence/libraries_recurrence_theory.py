# Biblioteka – zbiór gotowych funkcji i klas, które można używać w kodzie 
# bez konieczności ich samodzielnej implementacji. W Pythonie biblioteki 
# mogą być wbudowane (np. math, random, datetime) 
# lub zewnętrzne (np. numpy, pandas).


# Framework – bardziej rozbudowana struktura niż biblioteka. Framework 
# narzuca sposób organizacji kodu i często wymaga stosowania określonych 
# zasad (np. Django dla aplikacji webowych).

# Przykład różnicy:

# Biblioteka math oferuje funkcje matematyczne, ale to Ty decydujesz, 
# kiedy i jak je wywołać.

# Framework Django wymusza strukturę aplikacji webowej, 
# np. jak zarządzać widokami czy bazą danych.


# --------------------------------------------------------------------

# Rekurencja

# https://www.python.info.pl/rekurencja/

# Rekurencja - technika w programowaniu, w której funkcja wywołuje samą siebie, 
# aby rozwiązać mniejsze podproblemy będące częścią większego problemu. Jest to 
# szczególnie użyteczne, gdy problem można podzielić na identyczne, 
# ale mniejsze podproblemy.

# W rekurencji kluczowe są dwa elementy:

# Warunek podstawowy (base case) – punkt, w którym funkcja przestaje wywoływać samą siebie. 
# To warunek, który musi zostać spełniony, aby zatrzymać rekurencję.
# Wywołanie rekurencyjne – funkcja wywołuje samą siebie z innymi 
# (zwykle mniejszymi) danymi wejściowymi.

# Jak działa rekurencja?
# Funkcja rozwiązuje problem przez:

# Rozbicie go na prostsze wersje tego samego problemu.
# Rozwiązanie tych prostszych problemów w sposób rekurencyjny.
# Po osiągnięciu warunku podstawowego funkcja wraca krok po kroku, scalając wyniki.