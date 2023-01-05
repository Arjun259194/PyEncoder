import colorama


def print_welcome_message():
    print(colorama.Fore.GREEN + "Welcome to py-encoder\n")
    print(colorama.Fore.GREEN + "- PyEncoder helps you encode and decode messages")
    print(colorama.Fore.GREEN + "- It takes 2 arguments")
    print(colorama.Fore.GREEN + "  1. Mode")
    print(colorama.Fore.GREEN + "    - If you are encoding a message then use '-e'")
    print(colorama.Fore.GREEN + "    - If you are decoding a message then use '-d'")
    print(colorama.Fore.GREEN + "  2. Message")
    print(colorama.Fore.GREEN +
          "    - It is the message that you want to encode/decode\n")
    print(colorama.Fore.RED +
          "NOTE:- PyEncoder can only decode messages encoded by PyEncoder")
    print(colorama.Fore.RED +
          "NOTE:- If you face any error while encoding or decoding use -h to get help")


def print_help_message():
    print(colorama.Fore.GREEN + '''
Hello!, glad to help you

How to give input?
  - PyEncoder takes data from command-line arguments.
  
  
What is a command-line argument?
  - command-line arguments are arguments passed by the user (you) when they execute the program from the command line.
  
How to execute a program from the command line?
  - open your terminal in the directory in which your PyEncoder is.
  - now how to run PyEncoder is based on what you are using
  
  => If you are using a raw python file
    -> Use the python command to execute the main.py file
    ex. `python ./main.py`
  
  => If you are using the executable file
    -> just execute it normally 
    ex(windows). `./main.exe` 

How to pass arguments?
  - after the executing command you can type your arguments
  - to know which arguments to use or to know their order just run the program and read the welcome message.

Useful notes
  - use "" or '' while passing message
    ex. ` python ./main.py -d "+^&=_" `
''')


def display_decoded_message(et, dt):
    print(colorama.Fore.GREEN + "✅✅Decoding successfully")
    print(colorama.Fore.RESET + "Your encrypted text was", end=" ")
    print(colorama.Fore.YELLOW + et, end="\n")
    print(colorama.Fore.RESET + "Your Decoded message is", end=" ")
    print(colorama.Fore.GREEN + dt)


def display_encoded_message(pt, ct):
    print(colorama.Fore.GREEN + "✅✅Encoding successfully")
    print(colorama.Fore.RESET + "Your text input was", end=" ")
    print(colorama.Fore.YELLOW + pt, end="\n")
    print(colorama.Fore.RESET + "Your Encoded message is", end=" ")
    print(colorama.Fore.GREEN + ct)
    print(colorama.Fore.RED +
          "\nNOTE:- This encryption can only be decoded in PyEncoder")
