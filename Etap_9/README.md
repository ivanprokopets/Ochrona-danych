# Cel

Celem jest zapoznanie z potencjalnymi błędami i zagrożeniami na które narażone są aplikacje internetowe. W czasie zajęć zostaną zaprezentowane przykładowe ataki XSS oraz sposoby naprawy aplikacji, aby była na nie odporna.

## Mod_python

Jedną z metod pozwalających na korzystanie z języka Python do tworzenia aplikacji internetowych jest wykorzystanie modułu Apache `mod_python`. Do realizacji zadań wystarczy jego uruchomienie, oraz konfiguracja poprzez dodanie kilku linii w konfiguracji serwera Apache dotyczącej określonego katalogu.
 
`AddHandler mod_python .py`  
`PythonHandler mod_python.publisher`  
`PythonDebug On`  

## Przykładowe zadania:

 1. Zmodyfikować prezentowany atak XSS, tak, aby przekazywał on skryptowi ciasteczka użytkownika i zapamiętywał je w pliku.  
 2. Zmodyfikować prezentowany atak XSS, tak, aby wydobywał on tajną notatkę użytkownika   
 3. Zmodyfikować ciastka przeglądarki tak, aby zostać zalogowanym przez użytkownika  
 4. zmiana tła strony,  
 5. automatyczne przełączenie na dowolną inną stronę,  
 6. wyświetlenie reklamy (obrazka zewnętrznego),  
 7. przesłanie cookie na zewnętrzny serwer,  
 8. zaproponuj poprawioną wersję skryptu.  
