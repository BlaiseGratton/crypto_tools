from cryptography.fernet import Fernet
from sys import argv


try:
    script, encrypted_filename, key, file_extension = argv
except ValueError:
    raise ValueError, "incorrect arguments"
try:
    open(encrypted_filename)
except IOError:
    raise ValueError, "{} is not a valid file name".format(encrypted_filename)

encrypted_contents = open(encrypted_filename).read()
output_filename = encrypted_filename.replace('_enc.txt', '.') + file_extension

f = Fernet(key)
output_contents = f.decrypt(encrypted_contents)

open(output_filename, 'w').write(output_contents)
