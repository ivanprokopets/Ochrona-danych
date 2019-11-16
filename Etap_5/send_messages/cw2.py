import requests, base64
from Crypto.PublicKey import RSA
from client import Client

c = Client("http://0.0.0.0:5000")
###ZADANIE 2!!!!!!!!!!!!

rs = RSA.importKey(c.get_key("deadbeef").decode())
messeg = rs.encrypt("test".encode(), "some randomness")
print(messeg)
data = {"message": base64.encodebytes(messeg[0]).decode('utf-8')}
print(data)
c.send_binary_message("deadbeef",messeg[0])
