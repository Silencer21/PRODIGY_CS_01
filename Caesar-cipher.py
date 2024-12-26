# Function to encrypt or decrypt the input text based on the Caesar cipher

def encrypt_decrypt(text, mode, key):
    result = ''  # Initialize an empty string to store the result
    if mode == 'd':  # If the mode is decryption, reverse the key
        key = -key
    for letter in text:  # Iterate over each letter in the input text
        letter = letter.lower()  # Convert the letter to lowercase
        if not letter == ' ':  # Skip spaces (do not encrypt/decrypt spaces)
            index = letters.find(letter)  # Find the index of the letter in the 'letters' string
            if index == -1:  # If the letter is not found (e.g., punctuation), add it unchanged to result
                result += letter
            else:
                new_index = index + key  # Apply the key to shift the index
                if new_index >= num_letters:  # Wrap around if new_index exceeds the number of letters
                    new_index -= num_letters
                elif new_index < 0:  # Wrap around if new_index is negative
                    new_index += num_letters
                result += letters[new_index]  # Add the shifted letter to the result
    return result  # Return the final encrypted or decrypted result


letters = 'abcdefghijklmnopqrstuvwxyz'  # The alphabet used for encryption/decryption
num_letters = len(letters)  # The total number of letters in the alphabet

# Print the program title
print()
print('***CAESAR CIPHER PROGRAM***')
print()

# Prompt user to choose between encryption or decryption
while True:
    print('Encrypt or Decrypt? ')
    user_input = input('e/d: ').lower()  # Get user input and convert to lowercase
    if user_input in ['e', 'd']:  # Check if the input is valid
        break
    else:
        print("Invalid input! Please enter 'e' for encryption or 'd' for decryption.")
        print()

print()

# Set the mode based on user input and print the mode selected
if user_input == 'e':
    print('ENCRYPTION MODE SELECTED')
elif user_input == 'd':
    print('DECRYPTION MODE SELECTED')

print()

# Validate the encryption key to ensure it is between 1 and 26
while True:
    try:
        key = int(input('Enter the key (1 - 26): '))  # Get user input for the key
        if 1 <= key <= 26:  # Check if the key is valid
            break
        else:
            print("Invalid key! Please enter a number between 1 and 26.")
    except ValueError:  # Handle invalid input (non-integer values)
        print("Invalid input! Please enter a valid number between 1 and 26.")

print()

# Prompt user for text input and apply the encryption or decryption function
if user_input == 'e':
    text = input('Enter text to encrypt: ')  # Get text to encrypt
    ciphertext = encrypt_decrypt(text, user_input, key)  # Encrypt the text
    print(f'CIPHERTEXT: {ciphertext}')  # Print the encrypted text
elif user_input == 'd':
    text = input('Enter text to decrypt: ')  # Get text to decrypt
    plaintext = encrypt_decrypt(text, user_input, key)  # Decrypt the text
    print(f'PLAINTEXT: {plaintext}')  # Print the decrypted text
