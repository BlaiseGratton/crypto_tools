from cryptography.fernet import Fernet
from sys import argv


key = Fernet.generate_key()
f = Fernet(key)

script, filename = argv
encrypted_filename = filename.split('.')[0] + "_enc.txt"

file_contents = open(filename).read()
encrypted_contents = f.encrypt(file_contents)

encrypted_file = open(encrypted_filename, 'wb')
encrypted_file.write(encrypted_contents)
encrypted_file.close()

print key

