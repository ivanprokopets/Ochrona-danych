from Crypto.PublicKey import RSA
from client import Client

c = Client("http://0.0.0.0:5000")

###ZADANIE 3!!!!!!!!!!!!
# 2 user
# rsa_keys = RSA.generate(1024)
# key = rsa_keys.publickey().exportKey()
# c.send_key("user2", key)
# print(c)
# f = open("keypub2.txt", "w")
# f.write(key.decode())
#
# f1 = open("keyprivate2.txt", "w")
# f1.write(rsa_keys.exportKey().decode())


def odszyfruj():
    f = open("keyprivate2.txt", "r")
    key = f.read()
    r = RSA.importKey(key)
    messeg = r.decrypt(c.get_binary_message("user2"))
    print(messeg)


def send():
    key = c.get_key("user1").decode()
    r = RSA.importKey(key)
    c.send_binary_message("user1", r.encrypt("hello user1".encode(), "hello")[0])

odszyfruj()
send()