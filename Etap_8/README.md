## Cel zajęć
Uruchomienie i skonfigurowanie usług działających z wykorzystaniem protokołu SSL. Generowanie certyfikatów i ich podpisywanie.  


## Ceryfikat samopodpisany
Do wygenerowania odpowiednich kluczy kryptograficznych i certyfikatów wykorzystamy program openssl.  

Zaczynamy od poleceń potrzebnych do wygenerowania klucza:  

### Tworzenie klucza RSA  
`openssl genrsa -des3 -out testowy.key 1024`  

### Podglad klucza  
`openssl rsa -noout -text -in testowy.key`      
Następującym poleceniem stworzymy samopodpisany certyfikat:  

`openssl req -new -x509 -days 365 -key testowy.key -out testowy.crt`  

### Podgląd certyfikatu  
`openssl x509 -noout -text -in testowy.crt`  
### Certyfikacja pełna  
Proces uzyskania certyfikatu podpisanego przez zewnętrzną organizację rozpoczyna się podobnie jak w przypadku certyfikatu samopodpisanego - od wygenerowania kluczy. Następnie należy wygenerować prośbę o certyfikat:

### Stworzenie pliku prosby o certyfikacje  
`openssl req -new -key test.key -out test.csr`  

#### Podglad prosby
`openssl req -noout -text -in test.csr`
Plik prośby *.csr powinien być przekazany do urzędu certyfikującego (CA). Urząd certyfikujący korzystając ze swojego klucza i certyfikatu podpisuje prośbę, która od tego momentu staje się podpisanym certyfikatem. Podpisywanie prośby nie jest już jednolinijkowym wywołaniem openssl, a więc wykorzystamy skrypt sign.shSkrypt ten zakłada, że klucz urzędu certyfikującego znajduje się w pliku ca.key, a jego certyfikat w pliku ca.crt. Jeśli tak będzie, to jego wywołanie jest proste:

`./sign.sh test.csr`
