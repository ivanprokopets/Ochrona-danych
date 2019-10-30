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
Zapoznanie z blokowymi algorytmami szyfrowania symetrycznego oraz metodami przekształcania hasła na dobry klucz kryptograficzny.

#### Opis zadań
Informacja o zadań składających się z projektu.
- [x] 1. Napisz algorytm obliczający entropię. [Kode_1](./Etap_2/1.py)
- [x] 2. Porównaj entropie tekstu naturalnego z entropia kryptogramu. [Kode_2](./Etap_2/2.py)
- [x] 3. Porównaj wynik szyfrowania w trybach ECB i CBC. Jaka jest entropia kryptogramów? [Kode_3](./Etap_2/3.py)
- [x] 4. Zaproponuj algorytm tworzenia klucza na podstawie hasła podawanego przez człowieka. [Kode_4](./Etap_2/4.py)
- [x] 5. Określ ile znaków `[a-z]` należy podać, żeby entropia hasła zbliżyła się do 256-bitowego klucza AES. [Kode_5](./Etap_2/5.py)
- [x] 6. Napisz program do ataku brutalnej siły na kryptogram przy wykorzystaniu entropii jako uniwersalnego kryterium zakończenia algorytmu. [Kode_6](./Etap_2/6.py)

##### Przydatne materiały dla etapu 2
* Hasła dla Google: DES, AES, key derivation, entropy
----------------------


