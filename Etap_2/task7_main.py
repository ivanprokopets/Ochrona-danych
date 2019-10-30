import datetime

from PIL import Image

img_in = Image.open("we800_CBC_encrypted.bmp")
data = img_in.convert("RGB").tobytes()
print(type(data))
print(len(data))
data = data[:160]
keyAlphabet = range(ord('a'), ord('z') + 1)
from task7 import bruteforce

start = datetime.datetime.now()
bruteforce(data, 3, keyAlphabet)
duration = datetime.datetime.now() - start
print(duration)
