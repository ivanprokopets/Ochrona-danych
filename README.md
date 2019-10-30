# Ochrona_danych
Znajdziesz tutaj omówienie algorytmów kryptologicznych, które stanowią fundamenty zabezpieczeń.

### Etap 1 - Kryptografia historyczna
Zapoznanie się z historycznymi algorytmami kryptograficznych (m.in. szyfrem Cezara, szyfrem strumieniowym RC4) i słabościami związanymi z ich stosowaniem. Zostanie wykorzystany język skryptowy Python umożliwiający szybkie rozwiązanie nawet skomplikowanego problemu. Ten etap to wprowadzanie do tematyki trybów pracy szyfrów blokowych, a także ataków brutalnej siły.

#### Opis zadań
Informacja o zadań składających się z projektu.
Przed uruchomieniem zainstaluj biblioteki:   
`pip3 install pycrypto`
- [x] 1. Za pomocą analizy statystycznej postaraj się odszyfrować tekst zaszyfrowany algorytmem przesunięcia cyklicznego o nieznanym kluczu (crypto.rot). Szyfrowane zostały wszystkie znaki o kodach z przedziału 0-255. POMINIĘTO znak spacji.
`(ord(c) + k) % 256 if c != ' '` 
frequency taken from http://en.wikipedia.org/wiki/Letter_frequency [Kode_1](./Etap_1/1.py)
- [x] 2. Porównaj rozkłady statystyczne tekstów w dwóch różnych językach. Należy wypisać co najmniej słownik z liczbą wystąpień każdego znaku tekstu. [Kode_2](./Etap_1/2.py)
- [x] 3. Szyforwanie oraz deszyfrowanie alogorytmem Cezara. [Kode_3](./Etap_1/3.py)
- [x] 4. Procent wystąpienia znaku w tekscie. [Kode_4](./Etap_1/4.py)
- [x] 5. Napisz program przeprowadzający atak brutalnej siły na kryptogram crypto.rc4. Został on zaszyfrowany trzyznakowym kluczem `3x ['a'-'z']` [Kode_5](./Etap_1/5.py)
##### Przydatne materiały dla etapu 1
* Hasła dla Google: Cezar, ROT13, Vigenere, RC4, entropy
----------------------

### Etap 2 - Szyfrowanie blokowe
