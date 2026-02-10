import random
import string
chars=string.ascii_letters+string.digits+string.punctuation
password=""
for i in range(8):
    password+=random.choice(chars)
print(password)