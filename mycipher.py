# imports the sys module
import sys

# function that encrypts text 
def caesar_cipher(shift):
    for line in sys.stdin:
        plain_text = line.strip().upper()
        cipher_text = ""
        block_count = 0
        for letter in plain_text:
            # makes sure only alphabets can go through 
            if letter.isalpha():
                # converts charcaters to ascii code and then uses that to compute 
                new_code = (ord(letter) - 65 + shift) % 26 + 65

                # converts the ascii code back to text 
                cipher_text += chr(new_code)
                block_count += 1

                # formats in blocks of five letters 
                if block_count == 5:
                    cipher_text += " "
                    block_count = 0
            else:
                # Skips a character if its not a letter 
                continue

            
        return cipher_text



# gets the shift value from the terminal
shift = int(sys.argv[1])
cipher_text = caesar_cipher(shift)

# Print the ciphertext in blocks of ten blocks per line.
for i in range(0, len(cipher_text), 60):
    print(cipher_text[i:i+60])

