import multiprocessing
import time
import ctypes
from Crypto.Cipher import AES
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes


def xor64(a, b):
    block = bytearray(a, 'utf-8')
    for j in range(8):
        block[j] = ord(a[j]) ^ b[j]
    return block


def encrypt_ECB_serial(key, plain_text):
    vector = bytearray(plain_text, 'utf-8')
    des = AES.new(key, AES.MODE_ECB)
    for i in range(no_blocks):
        offset = i * block_size
        block = plain_text[offset:offset + block_size]
        for j in range(1000):
            encrypted = des.encrypt(block)
            block = encrypted
        vector[offset:offset + block_size] = bytearray(encrypted)
    return bytes(vector)


def decrypt_ECB_serial(key, encrypted_block):
    vector = bytearray(encrypted_block)
    des = AES.new(key, AES.MODE_ECB)
    for i in range(no_blocks):
        offset = i * block_size
        block = encrypted_block[offset:offset + block_size]
        for j in range(1000):
            decrypted = des.decrypt(block)
            block = decrypted
        vector[offset:offset + block_size] = bytearray(decrypted)
    return bytes(vector)


plain_text = "alamakot" * 1000
key = "key4567890123456"
iv = get_random_bytes(16)
block_size = 16
no_blocks = int(len(plain_text) / block_size)

starttime = time.time()
encryptedECB = encrypt_ECB_serial(key, plain_text)
print('ECB Encrypt time serial: ', (time.time() - starttime))
print(encryptedECB)
starttime = time.time()
decrypted = decrypt_ECB_serial(key, encryptedECB)
print('ECB Decrypt time serial: ', (time.time() - starttime))


def mapper(i):
    offset = i * block_size
    block = bytes(shared_data[offset:offset + block_size])
    for j in range(1000):
        decrypted = des.encrypt(block)
        block = decrypted
    output_data[offset:offset + block_size] = bytearray(decrypted)
    return i


des = AES.new(key, AES.MODE_ECB)
shared_data = multiprocessing.RawArray(ctypes.c_ubyte, plain_text.encode())
output_data = multiprocessing.RawArray(ctypes.c_ubyte, plain_text.encode())
pool = multiprocessing.Pool(4)
starttime = time.time()
pool.map(mapper, range(no_blocks))
print('ECB Encrypt time parallel: ', (time.time() - starttime))
decrypted = bytes(output_data)
print(decrypted)


