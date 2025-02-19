def caesar_cipher_encrypt(text,shift):
	encrypted_text = ""
	for char in text:
		if char.isalpha():
			shift_base = 65 if char.isupper() else 97
			encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
		else:
			encrypted_text += print("{} is Not Text Value".format(text))
	return encrypted_text

def caesar_cipher_decrypt(text,shift):
	decrypted_text = ""
	for char in text:
		if char.isalpha():
			shift_base = 65 if char.isupper() else 97
			decrypted_text += chr((ord(char) - shift_base - shift ) % 26 + shift_base)
		else:
			decrypted_text += print("{} is Not Text Value".format(text))
	return decrypted_text

action = str(input("Type (E) to Encrypt text OR Type (D) to Decrypt text: ")).strip().lower()
message = input("Enter Text: ").strip()
shift = int(input("Enter the Shift Value (integer): ").strip())

if action == 'e' :
	encrypted_string = caesar_cipher_encrypt(message,shift)
	print("Encrypted Text: ",encrypted_string)
elif action == 'd':
	decrypted_string = caesar_cipher_decrypt(message,shift)
	print("Decrypted Text: ",decrypted_string)
else:
	print("Invalid action. Please choose either 'E' To Encrypt or 'D' To Decrypt ")