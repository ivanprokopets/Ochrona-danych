from Crypto.PublicKey import RSA
from client import Client

c = Client("http://0.0.0.0:5000")

###ZADANIE 3!!!!!!!!!!!!
# 1 uzytkownik
# rsa_keys = RSA.generate(1024)
# key = rsa_keys.publickey().exportKey()
# c.send_key("user1", key)
# print(c)
# f = open("keypub1.txt", "w")
# f.write(key.decode())
#
# f1 = open("keyprivate1.txt", "w")
# f1.write(rsa_keys.exportKey().decode())


def odszyfruj():
    f = open("keyprivate1.txt", "r")
    key = f.read()
    r = RSA.importKey(key)
    messeg = r.decrypt(c.get_binary_message("user1"))
    print(messeg)


def send():
    key = c.get_key("user2").decode()
    r = RSA.importKey(key)
    c.send_binary_message("user2", r.encrypt("hello user2".encode(), "hello")[0])


send()
odszyfruj()