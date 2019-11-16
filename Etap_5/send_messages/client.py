import requests, base64
from Crypto.PublicKey import RSA

STATUS_OK = 200


class Client:
    def __init__(self, server_url):
        self.server_url = server_url

    def send_key(self, uid, key):
        url = self.server_url + '/key/' + uid
        data = {'key': key.decode()}
        response = requests.post(url, json=data)
        if response.status_code != STATUS_OK:
            a = response.status_code
            b = response.text
            raise Exception('FAIL({a}): {b}'.format(a=a, b=b))
        b = response.text
        print('SUCCESS: {b}'.format(b=b))

    def get_key(self, uid):
        url = self.server_url + '/key/' + uid
        response = requests.get(url)
        if response.status_code != STATUS_OK:
            a = response.status_code
            b = response.text
            raise Exception('FAIL({a}): {b}'.format(a=a, b=b))

        key = response.text.encode()
        return key

    def send_binary_message(self, uid, msg):
        txt = base64.encodebytes(msg).decode()
        self.send_text_message(uid, txt)

    def send_text_message(self, uid, msg):
        url = self.server_url + '/message/' + uid
        data = {'message': msg}
        response = requests.post(url, json=data)
        if response.status_code != STATUS_OK:
            a = response.status_code
            b = response.text
            raise Exception('FAIL({a}): {b}'.format(a=a, b=b))
        b = response.text
        print('SUCCESS: {b}'.format(b=b))

    def get_text_message(self, uid):
        url = self.server_url + '/message/' + uid
        response = requests.get(url)
        if response.status_code != STATUS_OK:
            a = response.status_code
            b = response.text
            raise Exception('FAIL({a}): {b}'.format(a=a, b=b))

        txt = response.text
        return txt

    def get_binary_message(self, uid):
        txt = self.get_text_message(uid)
        msg = base64.decodebytes(txt.encode())
        return msg