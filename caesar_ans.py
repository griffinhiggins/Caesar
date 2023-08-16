# {{{ Array Method

def encrypt_array_verbose(plaintext, key):
    lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    ciphertext = ""
    for character in plaintext:
        if character.isupper():
            character = character.lower()
            index = lower.index(character) + key
            index = index + 26 * (index // 26)
            character = lower[index]
            character = character.upper()
        elif character.islower():
            index = lower.index(character) + key
            index = index - 26 * (index // 26)
            character = lower[index]
        ciphertext = ciphertext + character
    return ciphertext

def decrypt_array_verbose(ciphertext, key):
    lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    plaintext = ""
    for character in ciphertext:
        if character.isupper():
            character = character.lower()
            index = lower.index(character) - key
            index = index - 26 * (index // 26)
            character = lower[index]
            character = character.upper()
        elif character.islower():
            index = lower.index(character) - key
            index = index - 26 * (index // 26)
            character = lower[index]
        plaintext = plaintext + character
    return plaintext

# }}}
# {{{ Dictionary Method

def encrypt_dictionary_verbose(plaintext, key):
    dictionary = {}
    lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    number_of_characters = len(lower)
    for i in range(0, number_of_characters, 1):
        character = lower[i]
        index = i + key
        index = index - 26 * (index // 26)
        dictionary[character] = lower[index]
        dictionary[character.upper()] = lower[index].upper()

    ciphertext = ""
    number_of_characters = len(plaintext)
    for i in range(0, number_of_characters, 1):
        character = plaintext[i]
        if character in dictionary:
            character = dictionary[character]
        ciphertext = ciphertext + character
    return ciphertext


def decrypt_dictionary_verbose(ciphertext, key):
    dictionary = {}
    lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    number_of_characters = len(lower)
    for i in range(0, number_of_characters, 1):
        character = lower[i]
        index = i - key
        index = index - 26 * (index // 26)
        dictionary[character] = lower[index]
        dictionary[character.upper()] = lower[index].upper()

    plaintext = ""
    number_of_characters = len(ciphertext)
    for i in range(0, number_of_characters, 1):
        character = ciphertext[i]
        if character in dictionary:
            character = dictionary[character]
        plaintext = plaintext + character
    return plaintext

# }}}
# {{{ Math Method

def encrypt_math_verbose(plaintext, key):
    ciphertext = ""
    for character in plaintext:
        if character.isupper():
            character = character.lower()
            index = ord(character) - 97 + key
            index = index - 26 * (index // 26)
            character = chr(index + 97)
            character = character.upper()
        elif character.islower(): 
            index = ord(character) - 97 + key
            index = index - 26 * (index // 26)
            character = chr(index + 97)
        ciphertext = ciphertext + character
    return ciphertext

def decrypt_math_verbose(plaintext, key):
    ciphertext = ""
    for character in plaintext:
        if character.isupper():
            character = character.lower()
            index = ord(character) - 97 - key
            index = index - 26 * (index // 26)
            character = chr(index + 97)
            character = character.upper()
        elif character.islower(): 
            index = ord(character) - 97 - key
            index = index - 26 * (index // 26)
            character = chr(index + 97)
        ciphertext = ciphertext + character
    return ciphertext

# }}}
# {{{ Main


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--decrypt', action='store_true')
    parser.add_argument('-k', '--key', type=int, required=True)
    input_mutex = parser.add_mutually_exclusive_group()
    input_mutex.add_argument('-', dest="stdin", action='store_true')
    input_mutex.add_argument('-s', '--string')
    args = parser.parse_args()

    if args.stdin:
        args.string = ""
        while True:
            try:
                args.string += f"{input()}\n"
            except EOFError:
                break

    args.string = args.string.rstrip("\n")

    if args.decrypt:
        print(decrypt_array_verbose(args.string, args.key))
        print(decrypt_dictionary_verbose(args.string, args.key))
        print(decrypt_math_verbose(args.string, args.key))
    else:
        print(encrypt_array_verbose(args.string, args.key))
        print(encrypt_dictionary_verbose(args.string, args.key))
        print(encrypt_math_verbose(args.string, args.key))

# }}}

# vim: set foldmethod=marker foldlevel=0:
