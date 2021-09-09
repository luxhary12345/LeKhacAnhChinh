alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def decipher(text_input,shift_input):
  cipher_text=""
  for letters in text_input:
    position=alphabet.index(letters)
    if direction=="encode":
      new_position=position+shift_input
    else:
      new_position=position-shift_input
    new_letter=alphabet[new_position]
    cipher_text+=new_letter
  print(f"it is {cipher_text}")
decipher(text_input=text,shift_input=shift)
