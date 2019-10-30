def szyfruj(txt, klucz):
    zaszyfrowny = ""
    for i in range(len(txt)):
        if ord(txt[i]) > 122 - klucz:
            zaszyfrowny += chr(ord(txt[i]) + klucz - 26)
        elif ord(txt[i]) == 32:
            zaszyfrowny += txt[i]
        else:
            zaszyfrowny += chr(ord(txt[i]) + klucz)
    return zaszyfrowny

def deszyfruj(tekst, start, stop):
    odszyfrowany = ""
    for i in range(start,stop):
        KLUCZM = i % 26
        for znak in tekst:
            if ord(znak) == 32:
                odszyfrowany += znak
            elif (ord(znak) - KLUCZM < 97):
                odszyfrowany += chr(ord(znak) - KLUCZM + 26)
            else:
                odszyfrowany += chr(ord(znak) - KLUCZM)
        print(odszyfrowany + " " + str(i))
        odszyfrowany=""

print(szyfruj("when the data source produces a low probability value", 5))
deszyfruj("bmjs ymj ifyf xtzwhj uwtizhjx f qtb uwtgfgnqnyd afqzj", 3, 10)
