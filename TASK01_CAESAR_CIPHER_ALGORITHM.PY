import tkinter as tk
from tkinter import messagebox

def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char  # Non-alphabetic characters are not changed
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_text += char  # Non-alphabetic characters are not changed
    return decrypted_text

# Function to handle the encryption/decryption process
def process_cipher():
    action = action_var.get()
    message = text_entry.get()
    try:
        shift = int(shift_entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid integer for the shift value.")
        return

    if not message:
        messagebox.showerror("Input Error", "Please enter text to encrypt or decrypt.")
        return

    if action == 'e':
        result = caesar_cipher_encrypt(message, shift)
        result_label.config(text="Encrypted Text: " + result)
    elif action == 'd':
        result = caesar_cipher_decrypt(message, shift)
        result_label.config(text="Decrypted Text: " + result)
    else:
        messagebox.showerror("Input Error", "Invalid action. Please choose either 'Encrypt' or 'Decrypt'.")

# Set up the main window
root = tk.Tk()
root.title("Caesar Cipher")

# Create and place labels, entries, and buttons
action_var = tk.StringVar(value='e')  # Default to encrypt

action_label = tk.Label(root, text="Choose Action:")
action_label.grid(row=0, column=0, padx=10, pady=10)

encrypt_radio = tk.Radiobutton(root, text="Encrypt", variable=action_var, value='e')
encrypt_radio.grid(row=0, column=1, padx=10, pady=10)

decrypt_radio = tk.Radiobutton(root, text="Decrypt", variable=action_var, value='d')
decrypt_radio.grid(row=0, column=2, padx=10, pady=10)

text_label = tk.Label(root, text="Enter Text:")
text_label.grid(row=1, column=0, padx=10, pady=10)

text_entry = tk.Entry(root, width=40)
text_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

shift_label = tk.Label(root, text="Enter Shift Value:")
shift_label.grid(row=2, column=0, padx=10, pady=10)

shift_entry = tk.Entry(root, width=40)
shift_entry.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

process_button = tk.Button(root, text="Process", command=process_cipher)
process_button.grid(row=3, column=1, padx=10, pady=20)

result_label = tk.Label(root, text="Result will appear here")
result_label.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
