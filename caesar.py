# to run the program execute 
#     python3 caesar.py -k 3 -s "the quick brown fox jumps over the lazy dog"
#     python3 caesar.py -d -k 3 -s "wkh txlfn eurzq ira mxpsv ryhu wkh odcb grj""

def encrypt(plaintext, key):
    # encryption code here
    return ciphertext

def decrypt(ciphertext, key):
    # decryption code here
    return plaintext

# Don't worry about this code down here, it just reads in arguments and flags
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
        print(decrypt(args.string, args.key))
    else:
        print(encrypt(args.string, args.key))
