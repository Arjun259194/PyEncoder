import colorama
import sys
from maps import encode_map, decode_map
from functions import *


def encode(string) -> str:
    encode_string = ""
    for char in string:
        encode_string += encode_map[char]
    return encode_string


def decode(string) -> str:
    decode_string = ""
    for char in string:
        decode_string += decode_map[char]
    return decode_string


def main():
    if len(sys.argv) <= 1:
        print_welcome_message()
    elif sys.argv[1] == '-h':
        print_help_message()
    elif sys.argv[1] == '-e' and sys.argv[2]:
        e_message = encode(sys.argv[2])
        display_encoded_message(sys.argv[2], e_message)
    elif sys.argv[1] == '-d' and sys.argv[2]:
        d_message = decode(sys.argv[2])
        display_decoded_message(sys.argv[2], d_message)


if __name__ == "__main__":
    main()
