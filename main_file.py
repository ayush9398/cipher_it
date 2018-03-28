import argparse
from Morse_code.morse import morse

def main():
    parser=argparse.ArgumentParser(description="Cipher your text")
    parser.add_argument('-t',"--text", help="text you want to enter", type=str)
    parser.add_argument("cipher", help="enter the cipher to encode to")
    parser.add_argument("-f","--file", help="enter file to encode, .txt only")
    args=parser.parse_args()
    if (args.file):
        with open(args.file,'r') as filem:
            if(args.cipher=='morse'):
                crypt=morse(filem.read())
                print(crypt)
    else:
        if (args.cipher == 'morse'):
            crypt = morse(args.text)
            print(crypt)


if __name__== "__main__":
    main()