# 1. Za pomocą analizy statystycznej postaraj się odszyfrować tekst zaszyfrowany algorytmem przesunięcia cyklicznego o
# nieznanym kluczu (crypto.rot). Szyfrowane zostały wszystkie znaki o kodach z przedziału 0-255. P
# OMINIĘTO znak spacji.
# (ord(c) + k) % 256 if c != ' '
# frequency taken from http://en.wikipedia.org/wiki/Letter_frequency
with open('crypto.rot', 'rb') as file:
    data = file.read()
    alf= {c: 0 for c in range(256)}
    for b in data:
        alf[b] = alf[b] + 1
    sortedFrequency = sorted(alf.items(), key=lambda l: l[1], reverse=True)
    diff = 50
    recovered = [chr((b - diff) % 255) for b in data]
    for a in recovered:
        try:
            recovered.remove('')
        except ValueError:
            pass
    print(''.join(recovered))
