# Dynamic Command-Line Caesar Cipher Tool
import sys


def caesar_cipher(text, displacement, mode):
    """
    Encrypts or decrypts text using the Caesar Cipher.

    mode:
        'e' -> encryption
        'd' -> decryption
    """

    # For decryption, reverse the displacement
    if mode == "d":
        displacement = -displacement

    result = []

    # Process each character in the input text
    for char in text:

        # Check if the character is an uppercase letter
        if char.isupper():
            # Convert character to 0-25 range
            shifted = (ord(char) - ord('A') + displacement) % 26

            # Convert shifted value back to a character
            result.append(chr(shifted + ord('A')))

        # Check if the character is a lowercase letter
        elif char.islower():
            # Convert character to 0-25 range
            shifted = (ord(char) - ord('a') + displacement) % 26

            # Convert shifted value back to a character
            result.append(chr(shifted + ord('a')))

        else:
            # Keep spaces, numbers and special characters unchanged
            result.append(char)

    # Join all characters to form the final result
    return ''.join(result)


def main():
    """
    Main function that reads command-line arguments.
    """

    # Check whether the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: python caesar.py <text> <displacement> <mode>")
        print("Mode: e = encrypt, d = decrypt")
        return

    # Get values from command-line arguments
    text = sys.argv[1]

    try:
        displacement = int(sys.argv[2])
    except ValueError:
        print("Error: Displacement must be an integer.")
        return

    mode = sys.argv[3].lower()

    # Validate the mode
    if mode not in ("e", "d"):
        print("Error: Mode must be 'e' for encryption or 'd' for decryption.")
        return

    # Perform encryption/decryption
    result = caesar_cipher(text, displacement, mode)

    # Display the result
    if mode == "e":
        print("Encrypted text:", result)
    else:
        print("Decrypted text:", result)


# Program execution starts here
if __name__ == "__main__":
    main()