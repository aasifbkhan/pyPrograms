#password encryption and decryption
import base64, os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

def password_cryptography(password):
	password_provided = password.encode()
	salt = b'salt_'
	kdf = PBKDF2HMAC(
		algorithm = hashes.SHA256(),
		length = 32,
		salt = salt,
		iterations = 100000,
		backend = default_backend()
		)
	key = base64.urlsafe_b64encode(kdf.derive(password_provided))
	print("Key = ",key)
	#encryption
	f = Fernet(key)
	encrypted = f.encrypt(password_provided)
	print("encrypted = ",encrypted)
	#decryption
	decrypted = f.decrypt(encrypted)
	print("decrypted = ",decrypted.decode())

password = input("Enter Your password : ")
password_cryptography(password)